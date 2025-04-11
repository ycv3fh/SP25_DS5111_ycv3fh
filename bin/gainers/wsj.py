'''
This file contains the WSJ-specific implementations of both the downloader and processor.

Classes:
    GainerDownloadWSJ (WSJ-specific implementation of GainerDownload)
    GainerProcessWSJ (WSJ-specific implementation of GainerProcess)
'''
import os
from .base import GainerDownload, GainerProcess
from ..normalize_csv import normalize_csv

class GainerDownloadWSJ(GainerDownload):
    '''
    Handles the downloading the list of gainers from the WSJ
    '''
    def __init__(self):
        super().__init__()

    def download(self):
        os.system("make wsj.csv")
        print("Downloading WSJ gainers")

class GainerProcessWSJ(GainerProcess):
    '''
    Normalizes and saves the WSJ gainer data
    '''
    def __init__(self,data):
        super().__init__()
        self.raw_data = raw_data
        self.norm_data = None

    def normalize(self):
        self.normalized_file = normalize_csv(self.raw_data)
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H$M%S")
        new_filename = f"wsj_gainers_{timestamp}.csv"
        os.rename(self.normalized_file, new_filename)
        print("Saving WSJ gainers")

