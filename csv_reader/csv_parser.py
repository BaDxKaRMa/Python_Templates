#!/usr/bin/env python

import csv
import sys


def check_input():
    """Checks if the input is null"""
    if not sys.stdin.isatty():
        data = sys.stdin.readlines()
        return data
    else:
        print("No data provided")
        print("Expected format: python csv_reader.py < data.csv")
        print("Note: CSV file must have a header row")
        sys.exit(1)


def parse_csv(data):
    """
    returns a list of dictionaries using the headers as keys
    """
    reader = csv.DictReader(data)
    parsed_data = [row for row in reader]
    return parsed_data


if __name__ == "__main__":
    print(parse_csv(check_input()))
