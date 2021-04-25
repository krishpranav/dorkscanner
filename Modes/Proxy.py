#!/usr/bin/env/python3
# -*- coding: utf-8 -*-
# imports
import asyncio
from proxybroker import Broker
from termcolor import colored, cprint
import sys
import os

B = "PROXY MODE"
print ("B")
print ("")
print(colored('[+] This will find 25 Different working proxy server each time : ', 'green'))
print(colored('[+] Starting..', 'green'))

async def show(proxies):
    while True:
        proxy = await proxies.get()
        if proxy is None:
            break
        print('Found Proxy: %s' % proxy)

proxies = asyncio.Queue()
broker = Broker(proxies)
tasks = asyncio.gather(
    broker.find(types=['HTTP', 'HTTPS'], limit=100 ), show(proxies)
)
loop = asyncio.get_event_loop()
loop.run_until_complete(tasks)
print(colored('[+] Done', 'green'))
