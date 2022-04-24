import sys
import argparse
import requests
import json
from loguru import logger

url = "https://randomuser.me/api/"

@logger.catch
def get_user():
    try:
        logger.debug(f"Querying {url}")
        r = s.get(url)
        r.raise_for_status()
        jsonResponse = r.json()
        logger.success(f"Success found [{jsonResponse['results'][0]['name']['first']}]")
        logger.debug(jsonResponse)
        return jsonResponse['results'][0]
    except requests.exceptions.ConnectionError as err:
        logger.critical(f"Connection error: {err}")
        raise SystemExit()
    except requests.exceptions.HTTPError as err:
        logger.error(err)
        raise SystemExit()
    except requests.exceptions.RequestException as err:
        logger.error(f"Catch All Error: {err}")
        raise SystemExit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", default=False, help="Set the LOG_LEVEL to DEBUG.")
    args = parser.parse_args()
    logger.remove()
    if args.debug:
        logger.add(sys.stderr, level="DEBUG")
    else:
        logger.add(sys.stderr, level="INFO")

    s = requests.session()
    get_user()