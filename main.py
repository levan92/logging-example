import argparse
import logging

from support import funcA
from subdir.utils import util

from deep_sort_realtime.deepsort_tracker import DeepSort

logger = logging.getLogger('logging_example')

if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument('--logfile')
    ap.add_argument('--loglevel', default='INFO')
    args = ap.parse_args()

    format = "[%(asctime)s] [%(levelname)s] [%(name)s] %(message)s"

    # set up logging to file
    logging.basicConfig(filename=args.logfile, level=args.loglevel, format=format)
    # set up logging to console
    console = logging.StreamHandler()
    console.setLevel(args.loglevel)
    formatter = logging.Formatter(format)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logger.warn('Watch out!')  
    logger.info('I told you so') 
    logger.debug('debugging') 

    funcA()
    util()

    tracker = DeepSort()
