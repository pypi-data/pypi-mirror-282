from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    async def notify(self, message):
        pass
    
class DefaultNotification(Notification):
    
    async def notify(self, message):
        print(message)