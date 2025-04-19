'''
This file contains the abstract base classes (ABC) for both the downloader and processor, ensuring a consistent interface.

Contains:
    GainerDownload (Abstract base class for downloading gainers)
    GainerProcess (Abstract base class for processing gainers)
'''

from abc import ABC, abstractmethod

<<<<<<< HEAD
=======
# Downloader Base Class
class GainerDownload(ABC):
    """
    An absract base class for downloading gainer data from various sources.
    """
    def __init__(self):
        self.url = None  # Placeholder for actual URLs

    @abstractmethod
    def download(self):
        pass

>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
# Processor Base Class
class GainerProcess(ABC):
    """
    An abstract base class for processing gainer data
    """
<<<<<<< HEAD
    def __init__(self,gainer_downloader,gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

class GainerDownload(ABC):

=======
>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
    def __init__(self):
        pass

    @abstractmethod
<<<<<<< HEAD
    def download(self):
        pass
=======
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

>>>>>>> fa44f416df49de1a81d577f446138af5685a2c8c
