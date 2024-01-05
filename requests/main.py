#!/usr/bin/env python

import argparse
import sys
from tabulate import tabulate

from loguru import logger

import requests

url = "https://randomuser.me/api/"


@logger.catch
def get_user():
    try:
        logger.debug(f"Querying {url}")
        r = s.get(url)
        r.raise_for_status()
        json_response = r.json()
        logger.success(
            f"Success found [{json_response['results'][0]['name']['first']}]"
        )
        logger.debug(json_response)
        return json_response["results"][0]
    except requests.exceptions.ConnectionError as err:
        logger.critical(f"Connection error: {err}")
        raise SystemExit()
    except requests.exceptions.HTTPError as err:
        logger.error(f"HTTP error: {err}")
        raise SystemExit()
    except requests.exceptions.RequestException as err:
        logger.error(f"Catch All Error: {err}")
        raise SystemExit()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Set the LOG_LEVEL to DEBUG.",
    )
    args = parser.parse_args()
    logger.remove()
    if args.debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="ERROR")

    # START HERE
    try:
        s = requests.session()
        user = get_user()

        # Place user data into variables
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        email = user["email"]
        phone = user["phone"]
        city = user["location"]["city"]
        state = user["location"]["state"]

        logger.debug(
            f"First Name: {first_name}, Last Name: {last_name}, Email: {email}, Phone: {phone}, City: {city}, State: {state}"
        )
        print(
            tabulate(
                [[first_name, last_name, email, phone, city, state]],
                headers=["First", "Last", "Email", "Phone", "City", "State"],
            )
        )

        # Close the session
        s.close()
    except requests.exceptions.ConnectionError as err:
        logger.critical(f"Connection error: {err}")
        raise SystemExit()
else:
    pass
