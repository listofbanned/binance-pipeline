# python-binance.readthedocs.io/en/latest/websockets.html

from datetime import datetime

import time
from binance.client import Client
from binance.websockets import BinanceSocketManager


class Pipeline:
	"""
		docstring for Pipeline

		Arguments
			symbol: Cryptocurrency symbol.
			min_price: Pipeline returns the data every time price exceeds this number.
			pkey: Binance public key.
			skey: Binance secret key.

	"""
	def __init__(self, symbol, min_price, pkey, skey):
		self.SYMBOL = symbol
		self.PRICE = min_price

		self.PUBLIC = pkey
		self.SECRET = skey

		self.client = Client(api_key=self.PUBLIC, api_secret=self.SECRET)


	"""
		Processes messages received from api

		Arguments
			msg: received message

	"""
	def process_msg(self, msg):
		"""
			msg: {
			  "e": "trade",     // Event type
			  "E": 123456789,   // Event time
			  "s": "BNBBTC",    // Symbol
			  "t": 12345,       // Trade ID
			  "p": "0.001",     // Price
			  "q": "100",       // Quantity
			  "b": 88,          // Buyer order ID
			  "a": 50,          // Seller order ID
			  "T": 123456785,   // Trade time
			  "m": true,        // Is the buyer the market maker?
			  "M": true         // Ignore
			}
		"""
		if msg['e'] == "error":
			print("ERROR: Trade could not be processed.")

		else:
			# https://docs.python.org/3/library/datetime.html#datetime.date.strftime
			timestamp = datetime.fromtimestamp(msg['T']/1000).strftime("%Y-%m-%d %H:%M:%S")

			if float(msg['p']) > self.PRICE:
				print("Time: {}, Symbol: {}, Price: {}, Quantity: {}".format(timestamp, msg['s'], msg['p'], msg['q']))

	"""
		Start
	"""
	def run(self):
		bm = BinanceSocketManager(self.client)
		bm.start_trade_socket(self.SYMBOL, self.process_msg)

		# start socket
		bm.start()



# if __name__ == "__main__":
# 	pipeline = Pipeline()
# 	pipeline.run()
