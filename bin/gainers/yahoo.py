'''
This file contains the Yahoo-specific implementations of both the downloader and process

Classes:
    GainerDownloadYahoo (Yahoo-specific implementation of GainerDownload)
    GainerProcessYahoo (Yahoo-specific implementation of GainerProcess)
'''
import os
from .base import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__()

    def download(self):
        os.system("make ygainers.csv")
        print("Downloading Yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__()
        self.input_file = input_file
        self.normalized_file = None

    def normalize(self):
        self.normalized_file = normalize_csv(self.input_file)
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        new_filename = f"wsj_gainers_{timestamp}.csv"
        os.rename(self.normalized_file, new_filename)
        print("Saving Yahoo gainers")
