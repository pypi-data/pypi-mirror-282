import os
import sys
from urllib.parse import urlparse

project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from Parser4LLM.pdf_converter import PDFConverter
from Parser4LLM.word_converter import DOCXConverter
from Parser4LLM.ppt_converter import PPTXConverter
from Parser4LLM.url_converter import URLConverter
from Parser4LLM.notification import Notification, DefaultNotification

class Parser4LLM:
    def __init__(self, isPollingEnable: bool = True, isCleaningRequired: bool = True, notification: Notification = DefaultNotification()):
        self.notification = notification
        self.isPollingEnable = isPollingEnable
        self.isCleaningRequired = isCleaningRequired
        
    def check_file_type(self, path):
        parsed_url = urlparse(path)
        if parsed_url.scheme in ['http', 'https']:
            _, file_extension = os.path.splitext(parsed_url.path)
            file_extension = file_extension.lower()
            if file_extension == '.pdf':
                return 'PDF (URL)'
            else:
                return 'URL'
        
        _, file_extension = os.path.splitext(path)
        file_extension = file_extension.lower()

        if file_extension == '.docx':
            return 'Word'
        elif file_extension == '.pptx':
            return 'PowerPoint'
        elif file_extension == '.pdf':
            return 'PDF'
        else:
            return 'Unknown'
        
    async def convert(self, file_path):
        file_type = self.check_file_type(file_path)
        await self.notification.notify(f"Converting {file_type} file: {file_path}")
        if file_type == 'Word':
            converter = DOCXConverter(self.notification)
            md_content = converter.convert(file_path)
            return md_content
        elif file_type == 'PDF':
            converter = PDFConverter(file_path, self.isPollingEnable, self.isCleaningRequired, self.notification)
            md_content = await converter.convert()
            return md_content
        elif file_type == 'PowerPoint':
            converter = PPTXConverter(self.notification)
            md_content = converter.convert(file_path)
            return md_content
        elif file_type == 'URL':
            converter = URLConverter(self.notification)
            md_html, md_url = converter.convert(file_path)
            return md_html, md_url
        else:
            await self.notification.notify("Please check the file type")
            print("Please check the file...")
            return "Please Check the file type..."