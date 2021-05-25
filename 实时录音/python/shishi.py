# -*- encoding:utf-8 -*-

import sys
import hashlib
from hashlib import sha1
import hmac
import base64
from socket import *
import json, time, threading
from websocket import create_connection
import websocket
from urllib.parse import quote
import requests
base_url = "ws://rtasr.xfyun.cn/v1/ws"
app_id = "6e3c02b8"
api_key = "e41099b7083027eb85c21bbe0d5f2897"

ts = str(int(time.time()))
tt = (app_id + ts).encode('utf-8')
md5 = hashlib.md5()
md5.update(tt)
baseString = md5.hexdigest()
baseString = bytes(baseString, encoding='utf-8')

apiKey = api_key.encode('utf-8')
signa = hmac.new(apiKey, baseString, hashlib.sha1).digest()
signa = base64.b64encode(signa)
signa = str(signa, 'utf-8')

create_connection(base_url + "?appid=" + app_id + "&ts=" + ts + "&signa=" + quote(signa))



