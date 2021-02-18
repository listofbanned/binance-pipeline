# pip install python-binance
# python-binance.readthedocs.io
# pip install python-dotenv

"""
	Using python3.7

	System which allows to enter a symbol and a number to monitor market.
	Must provide a symbol and a minimum price to start the process.
"""

# Usage: python bnc_system.py -s [SYMBOL] -p [PRICE]
# ex: python bnc_system.py --symbol=BNBBTC --min_price=0

import os
import argparse
from dotenv import load_dotenv

import bnc_pipeline


# load env data
load_dotenv()
pkey = os.getenv("PUBLIC_KEY")
skey = os.getenv("SECRET_KEY")

# get data from arg
parser = argparse.ArgumentParser(description='Pipeline arguments')
parser.add_argument('--symbol', type=str, help='Cryptocurrency symbol.', required=True)
parser.add_argument('--min_price', type=float, help='Minimum price to monitor market data.', required=True)
args = parser.parse_args()

symbol = args.symbol
min_price = args.min_price

print(f'Processing {symbol}')


# start pipeline
pipeline = bnc_pipeline.Pipeline(symbol, min_price, pkey, skey)
pipeline.run()
