'''
Factory Pattern Implementation

Contains the GainerFactory class
	Responsible for creating the appropriate downloader and processor objects based on user choice
'''

from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ

class GainerFactory:
    '''
    Factory class return the appropriate downloader and processor based on the gainer choice
    '''
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        if self.choice == 'yahoo':
            return GainerProcessYahoo(input_file="ygainers.csv")
        elif self.choice == 'wsj':
            return GainerProcessWSJ(input_file="wjsgainers.csv")
