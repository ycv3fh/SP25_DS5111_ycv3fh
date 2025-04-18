'''
It takes user input, selects the appropriate factory-generated classes, and runs the processing pipeline.

'''

import sys
from bin.gainers.factory import GainerFactory
from bin.gainers.base import ProcessGainer

# Make our selection, 'one' choice
choice = sys.argv[1]

# let our factory get select the family of objects for processing
factory = GainerFactory(choice)
downloader = factory.get_downloader()
normalizer = factory.get_processor()

# create our process
runner = ProcessGainer(downloader, normalizer)
runner.process()


