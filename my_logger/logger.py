#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys

from loguru import logger


def main():
    logger.debug("This is DEBUG")
    logger.info("This is INFO")
    logger.warning("This is WARNING")
    logger.critical("This is CRITICAL")
    logger.error("This is ERROR")
    logger.success("This is SUCCESS")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Set the LOG_LEVEL to DEBUG.",
    )
    args = parser.parse_args()
    # Remove all handlers
    logger.remove()
    # Set loguru format
    fmt = "<green>{time:YYYY-MM-DD hh:mm:ss A}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>"

    if args.debug:
        logger.add(sys.stderr, format=fmt, level="DEBUG")
    else:
        logger.add(sys.stderr, format=fmt, level="INFO")

    main()
