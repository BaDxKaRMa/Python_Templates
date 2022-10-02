#!/usr/bin/env python

import argparse
import sys

import requests

from loguru import logger

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
        logger.add(sys.stderr, level="INFO")

    ## START HERE
    s = requests.session()
    user = get_user()

    # Place user data into variables
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    email = user["email"]
    phone = user["phone"]
    city = user["location"]["city"]
    state = user["location"]["state"]

    # Print user data
    logger.info(f"First Name: {first_name}")
    logger.info(f"Last Name: {last_name}")
    logger.info(f"Email: {email}")
    logger.info(f"Phone: {phone}")
    logger.info(f"City: {city}")
    logger.info(f"State: {state}")

    # Close the session
    s.close()
else:
    pass
