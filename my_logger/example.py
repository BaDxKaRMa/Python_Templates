#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
from loguru import logger
import requests
import json
from dataclasses import dataclass

@logger.catch
def get_user():
    '''
    logger.debug("This is DEBUG")
    logger.info("This is INFO")
    logger.warning("This is WARNING")
    logger.critical("This is CRITICAL")
    logger.error("This is ERROR")
    '''
    try:
        r = requests.get("https://randomuser.me/api/")
        r.raise_for_status()
        results = r.json()['results'][0]
        logger.debug(results)
        logger.success(f"Successfully found {results['name']['first']}")
        return results
    except requests.exceptions.HTTPError as error:
        logger.error(f"{error}")
        exit()

@dataclass
class Person:
    first: str
    last: str
    username: str
    password: str

def main() -> Person:
    user = get_user()
    person = Person(user['name']['first'], user['name']['last'], user['login']['username'], user['login']['password'])
    logger.debug(f"{person}")
    return person



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False, help="Set the LOG_LEVEL to DEBUG.")
    args = parser.parse_args()
    logger.remove()
    if args.debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="INFO", format="<level>{time}</level> | <level>{level}</level> | <level>{message}</level>")

    people = []
    for i in range(3):
        people.append(main())
    logger.info(f"Found {len(people)} people.")
