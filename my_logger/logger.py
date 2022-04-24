#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from loguru import logger



def main():
    logger.debug("This is DEBUG")
    logger.info("This is INFO")
    logger.warning("This is WARNING")
    logger.critical("This is CRITICAL")
    logger.error("This is ERROR")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False, help="Set the LOG_LEVEL to DEBUG.")
    args = parser.parse_args()
    logger.remove()
    if args.debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="INFO")

    main()
