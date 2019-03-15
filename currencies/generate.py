#!/usr/bin/env python

import json
import random 
import os

CURRENCIES = [
    "USD",
    "EUR",
    "CAD",
    "CHF",
    "GBP",
    "AUD",
    "INR",
    "JPY",
    "CNY",
    "SGD",
    "MYR",
    "NZD",
    "THB",
    "HUF",
    "AED",
    "HKD",
    "SEK",
    "IDR",
    "SAR",
    "BRL",
    "TRY",
    "RUB"
]

def main():
    '''Generates a list of currencies and random fictional conversion rates'''

    with open("list.json", "w") as OUT:
        json.dump({"results":CURRENCIES}, OUT, indent=4)

    for curr1 in CURRENCIES:

        if not os.path.exists(curr1):
            os.makedirs(curr1)

        results = {curr1: 1.0}
        for curr2 in CURRENCIES:
            if curr1 == curr2:
                continue
            results[curr2] = random.randint(1,10000) / 1000.0

        root = {
            "disclaimer": "The numbers are randomly generated",
            "results": results
        }
        with open(os.path.join(curr1, "rates.json"), "w") as OUT:
            json.dump(root, OUT, indent=4)

if __name__ == "__main__":

    main()