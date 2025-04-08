'''
It takes user input, selects the appropriate factory-generated classes, and runs the processing pipeline.

'''

import sys
from bin.gainers.factory import GainerFactory

# TEMPLATE
class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
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

if __name__ == "__main__":
    # Ensure the user provides a choice
    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py [yahoo|wsj]")
        sys.exit(1)

    choice = sys.argv[1]
    factory = GainerFactory(choice)

    # Get appropriate downloader and processor
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # Process gainers
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
