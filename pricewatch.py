import datetime as dt 
from BybitWebsocket import BybitWebsocket
import time
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import asyncio
import requests
import json

ws = BybitWebsocket(wsURL="wss://stream.bytick.com/realtime",api_key="", api_secret="")

ws.subscribe_trade()

class pricewatch():
	async def watch(self, bot):
		while(1):
			eth_data = ws.get_data("trade.ETHUSD")
			btc_data = ws.get_data("trade.BTCUSD")
			if eth_data:
				print("-")
			for trade in eth_data:
				ethprice = trade["price"]
				ethprice = round(float(ethprice),2)
				ethprice = "${:,.2f} USD".format(float(ethprice))
			if btc_data:
				print("-")
			for trade in btc_data:
				btcprice = trade["price"]
				btcprice = round(float(btcprice),2)
				btcprice = "${:,.2f} USD".format(float(btcprice))
			print("Eth: " + ethprice)
			print("Btc: " + btcprice)
			bothprice = "ETH: " + ethprice + " " + "BTC: " + btcprice
			await asyncio.sleep(4)
			await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=bothprice))


		

	def __init__(self):
		print("Started Price Watch")
	
