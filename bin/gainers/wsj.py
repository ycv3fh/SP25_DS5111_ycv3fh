'''
This file contains the WSJ-specific implementations of both the downloader and processor.

Classes:
    GainerDownloadWSJ (WSJ-specific implementation of GainerDownload)
    GainerProcessWSJ (WSJ-specific implementation of GainerProcess)
'''

from .base import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self):
        print("Downloading WSJ gainers")

class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")

