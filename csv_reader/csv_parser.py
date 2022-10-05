#!/usr/bin/env python

import csv
import sys


def check_input():
    if not sys.stdin.isatty():
        data = sys.stdin.readlines()
        return data
    else:
        print("No data provided")
        print("Expected format: python csv_reader.py < data.csv")
        print("Note: CSV file must have a header row")
        sys.exit(1)


def parse_csv(data):
    reader = csv.DictReader(data)
    parsed_data = [row for row in reader]
    return parsed_data


print(parse_csv(check_input()))
