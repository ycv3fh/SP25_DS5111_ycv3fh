'''
This file contains the Yahoo-specific implementations of both the downloader and process

Classes:
    GainerDownloadYahoo (Yahoo-specific implementation of GainerDownload)
    GainerProcessYahoo (Yahoo-specific implementation of GainerProcess)
'''
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self):
        # you can move your bash execution line here.
        # use the os system call to execute something at the command line
        # import os
        # os.system("< same command we use in the makefile >")
        print("Downloading Yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()

    def normalize(self):
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
