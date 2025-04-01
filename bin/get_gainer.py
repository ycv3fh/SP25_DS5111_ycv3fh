'''
It takes user input, selects the appropriate factory-generated classes, and runs the processing pipeline.

'''

import sys
from bin.gainers.factory import GainerFactory

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
