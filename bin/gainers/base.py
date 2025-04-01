'''
This file contains the abstract base classes (ABC) for both the downloader and processor, ensuring a consistent interface.

Contains:
    GainerDownload (Abstract base class for downloading gainers)
    GainerProcess (Abstract base class for processing gainers)
'''

from abc import ABC, abstractmethod

# Downloader Base Class
class GainerDownload(ABC):
    def __init__(self):
        self.url = None  # Placeholder for actual URLs

    @abstractmethod
    def download(self):
        pass

# Processor Base Class
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

