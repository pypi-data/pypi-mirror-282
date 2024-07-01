import os
import pymupdf4llm
import PyPDF2
import json
import requests
import uuid
import time
import fitz
import pytesseract
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm
from litellm import acompletion
import asyncio
from Parser4LLM.notification import Notification, DefaultNotification
    
class PDFConverter():
    def __init__(self, file_path, isPollingEnable, isCleaningRequired, notification: Notification = DefaultNotification()):
        self.file_path = file_path
        self.notification = notification
        self.isPollingEnable = isPollingEnable
        self.isCleaningRequired = isCleaningRequired
    
    def analyze_page(self, page):
        pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))  # Increase resolution for better OCR
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        ocr_result = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
        page_text = " ".join(ocr_result["text"])

        page_confidence = sum(ocr_result["conf"]) / len(ocr_result["conf"])
        confident_page = 1 if page_confidence >= 70 else 0
        return page_text, page_confidence, confident_page

    def needs_ocr(self, file_path, num_pages_to_analyze=10, min_text_length=100, min_confidence=70):
        doc = fitz.open(file_path)
        num_pages = doc.page_count
        page_indices = [i * (num_pages // num_pages_to_analyze) for i in range(num_pages_to_analyze)]

        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.analyze_page, doc.load_page(page_num)) for page_num in page_indices]
            with tqdm(total=len(futures), desc="Analyzing pages", unit="page") as pbar:
                total_text = ""
                confidence_sum = 0
                num_confident_pages = 0

                for future in futures:
                    page_text, page_confidence, confident_page = future.result()
                    total_text += page_text
                    confidence_sum += page_confidence
                    num_confident_pages += confident_page
                    pbar.update(1)

        doc.close()

        if len(total_text.strip()) < min_text_length:
            return True

        avg_confidence = confidence_sum / num_pages_to_analyze
        confident_page_ratio = num_confident_pages / num_pages_to_analyze

        print(f"\nExtracted Text Length: {len(total_text.strip())}")
        print(f"Average OCR Confidence: {avg_confidence:.2f}")
        print(f"Confident Page Ratio: {confident_page_ratio:.2f}")

        if avg_confidence < min_confidence or confident_page_ratio < 0.5:
            return True

        return False

    def upload_to_cloudflare(self, file_path):
        os.environ["CLOUDFLARE_API_URL"] = "https://workspace.askjunior2023.workers.dev/upload/"
        os.environ["CLOUDFLARE_CDN_URL"] = "https://pub-cc8438e664ef4d32a54c800c7c408282.r2.dev/"
        unique_id = str(uuid.uuid4())
        upload_url = os.environ["CLOUDFLARE_API_URL"] + unique_id + ".pdf"
        with open(file_path, 'rb') as f:
            headers = {'Content-Type': 'application/pdf'}
            upload_response = requests.put(upload_url, data=f.read(), headers=headers)
            upload_response.raise_for_status()
        new_url = f"{os.environ['CLOUDFLARE_CDN_URL']}{unique_id}.pdf"
        return new_url, unique_id
    
    async def poll_and_get_markdown_text_url(self, file_id):
        url = "https://marker--xata-verification-verifier.modal.run"
        payload = json.dumps({
            "file_id": file_id,
            "workspace_id": "ws123",
            "collection_name": "test_collection"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        for i in range(20):
            response = requests.request("POST", url, headers=headers, data=payload)
            response_text = response.text
            response_json = json.loads(response_text)
            if response_json["status"] == "error":
                return response_json["error_message"]
            if response_json["status"] == "completed":
                await self.notification.notify("Markdown text extraction completed successfully")
                return response_json["content"]
            pending_count = response_json["pending_count"]
            await self.notification.notify(f"OCR processing pending for {pending_count} items.")
            print(response_json["pending_count"], " is pending")
            time.sleep(15)
    
    async def ocr_routing_service(self, pdf_url, file_id):
        url = "https://marker--convertor-convert.modal.run"
        payload = json.dumps({
        "pdf_url": pdf_url,
        "file_id": file_id,
        "workspace_id": "ws123",
        "collection_name": "test_collection",
        "callback_url": "index_url.com"
        })
        headers = {
        'Content-Type': 'application/json'
        }
        await self.notification.notify("Initiating OCR process")
        response = requests.request("POST", url, headers=headers, data=payload)
        return response.text
    
    async def get_cleaned_paragraph(self, markdown_text):
        example_input = """
        IN THE HIGH COURT OF DELHI AT NEW DELHI 
        O:MP (COMM) NO. 259 2018 
        IN THE MATTER OF: 
        -
        DELHI DEVELOPMENT AUTHORJTY ... PETITIONER 
        VERSUS 
        lVI/S AJAB SINGH& CO. . .. RESPONDENT 
        ## INDEX-2
        | S.NO                                 | PARTICULARS                   | PAGES      | C.FEESj         |           |      |      |
        |--------------------------------------|-------------------------------|------------|-----------------|-----------|------|------|
        | 1.                                   | INDEX-2                       | 1-2        |                 |           |      |      |
        | 2.                                   | APPLICATION                   | UNDER      | SECTION         | 3-7       |      |      |
        | I                                    | 36(3) OF                      | THE        | ARBITRATION AND |           |      |      |
        | I                                    | .                             |            |                 |           |      |      |
        | CONCILATION                          | ACT                           | READ       | WITH            |           |      |      |
        | SECTION                              | 151                           | CPC        | FOR             | STAY      | OF   |      |
        | THE                                  | IMPUGNED                      | AWARD      | DATED           | I         |      |      |
        | I                                    | 17.01.2018                    | ON         | BEHALF          | OF        | THE  | I  I |
        | .                                    |                               |            |                 |           |      |      |
        | PETITIONERJDDA                       | ALONG                         | WITH       |                 |           |      |      |
        | SUPPORTING AFFIDAVIT.                |                               |            |                 |           |      |      |
        | '                                    | .                             | .. '. ·',. | '               |           |      |      |
        the Petitioner/ Applicant above named MOST RESPECTFULLY 
        SHOWETH: 
        1. That the Petitioner has filed this petition under section 34 of the 
        Arbitration and Conciliation Act, 1996 on . behalf of the Delhi 
        Development Authority against the impugned award dated 17.01.2018 .. 
        passed by the Ld .. Arbitrator Sh. H.S. Dogra, contents of which objection 
        Petition are not being repeated herein for the sake of brevity but be read . 
        . as part and parcel of the present Application. 
        :z That a perusal of the contents of the accompanying Petition s];lows that 
        the Petition has been able to make out a good prima facie case against the 
        Award dated 17.01.2018 passed by the Ld. Arbitrator Sh. H.S. Oo~tr.a... 
        """
        example_output = """
        IN THE HIGH COURT OF DELHI AT NEW DELHI 
        OMP (COMM) NO. 259 2018 
        IN THE MATTER OF:
        -----------------
        DELHI DEVELOPMENT AUTHORITY  ...PETITIONER
                    VERSUS
        M/S AJAB SINGH& CO.   ...RESPONDENT
        
        ## INDEX-2
        | S.No. | Particulars | Pages | C.Fees |
        |-------|-------------|-------|--------|
        | 1. | Index | 1-2 | - |
        | 2. | Application under Section 36(3) of the Arbitration and Conciliation Act, read with Section 151 CPC for Stay of the Impugned Award dated 17.01.2018 on behalf of the Petitioner/DDA along with Supporting Affidavit | 3-7 | - |
        
        The Petitioner/ Applicant above named most respectfully showeth: 
        1. That the Petitioner has filed this petition under section 34 of the Arbitration and Conciliation Act, 1996 on . behalf of the Delhi Development Authority against the impugned award dated 17.01.2018 passed by the Ld .. Arbitrator Sh. H.S. Dogra, contents of which objection Petition are not being repeated herein for the sake of brevity but be read as part and parcel of the present Application. 
        2. That a perusal of the contents of the accompanying Petition slows that the Petition has been able to make out a good prima facie case against the Award dated 17.01.2018 passed by the Ld. Arbitrator Sh. H.S. Dogra.
        """
        system_prompt = f"""
        You are an expert in cleaning and formatting markdown text for legal documents.
        
        The user will provide a <Markdown_Text> that contains markdown texts generated by an OCR system, which may have errors or formatting issues. 
        
        Your role is to clean up and format this markdown text so that it can be effectively processed by an NLP system. 
        Please adhere to the following guidelines:
        1. Ensure that the cleaned-up text is properly formatted using Markdown syntax.
        2. Focus solely on cleaning up and formatting the text. Do not include any explanatory notes, comments, or statements about the cleaning process itself in the output.
        3. Do not provide any AI preamble statements or indicate that AI is being used to clean up and format the text.
        
        User is not aware of that AI is used to clean up and format this markdown texts.
        """
        user_prompt = f"""
        <Markdown_Text>
        {markdown_text}
        </Markdown_Text>
        
        Please clean up and format the markdown texts that are enclosed within the <Markdown_Text> according to the guidelines provided in the system prompt. Provide your output in the specified format, ensuring that it is properly formatted using Markdown syntax and skip any explanatory notes or AI preamble statements.
        """
        messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": example_input},
        {"role": "assistant", "content": example_output},
        {"role": "user", "content": user_prompt}
        ]
        response = await acompletion(
                    model = "gpt-4o",
                    temperature=0,
                    messages=messages,
                )
        return response['choices'][0]['message']['content']
    

    async def get_cleaned_markdown_texts(self, markdown_texts):
        tasks = [] 
        for text in markdown_texts:
            result = self.get_cleaned_paragraph(text)
            task = asyncio.create_task(result)
            tasks.append(task)
        cleaned_texts = await asyncio.gather(*tasks)
        cleaned_markdown_text = ""
        for text in cleaned_texts:
            cleaned_markdown_text += text+"\n"
        return cleaned_markdown_text

    async def process_non_ocr_document(self):
        llama_reader = pymupdf4llm.LlamaMarkdownReader()
        llama_docs = llama_reader.load_data(self.file_path)
        texts = ""
        if self.isCleaningRequired:
            markdown_texts = []
            for doc in llama_docs:
                try:
                    text = getattr(doc, 'text', 'No text availabel')
                    metadata = getattr(doc, 'metadata', 'No text available')
                    uncleaned_text = f"### Page Number : {metadata['page']}\n{text}\n"
                    markdown_texts.append(uncleaned_text) 
                except Exception as e:
                    print(f"Error processing document: {e}")
            clean_text = await self.get_cleaned_markdown_texts(markdown_texts)
            return clean_text
        else:
            for doc in llama_docs:
                try:
                    text = getattr(doc, 'text', 'No text available')
                    metadata = getattr(doc, 'metadata', 'No text available')
                    texts += f"### Page Number : {metadata['page']}\n{text}\n"
                except Exception as e:
                    print(f"Error processing document: {e}")
        print(texts)
        return texts

    async def convert(self):
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        await self.notification.notify("Evaluating whether optical character recognition(OCR) is required for the file.")
        need_ocr = self.needs_ocr(self.file_path)
        if need_ocr:
            await self.notification.notify("OCR is necessary")
            pdf_url, file_id = self.upload_to_cloudflare(self.file_path)
            md_content = await self.ocr_routing_service(pdf_url, file_id)
            if self.isPollingEnable:
                md_url = await self.poll_and_get_markdown_text_url(file_id)
                return md_url
            else:
                md_url = os.environ["CLOUDFLARE_CDN_URL"] + file_id + ".md"
                return f"OCR processing has commenced. During this operation, which may take some time, a callback URL will be triggered. Upon completion, your processed content will be accessible at {md_url}"
        else:
            self.isPollingEnable = False
            await self.notification.notify("OCR is not required")
            md_content = await self.process_non_ocr_document()
            await self.notification.notify("Markdown text extraction completed successfully")
            return md_content