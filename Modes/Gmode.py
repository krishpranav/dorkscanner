#!/usr/bin/env/python3

#imports
import requests
import proxybroker
from googlesearch import search
import sys
from termcolor import colored, cprint
import warnings
import random
from http import cookiejar
class BlockAll(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False