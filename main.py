"""
speedtest fake results
author: xdcd (xdcdmaybe)
https://github.com/xdcdmaybe
"""

import hashlib
import requests
import re


down = int(input("download (mbps): ")) * 1000
up = int(input("upload (mbps): ")) * 1000
ping = int(input("ping (ms): "))


server = '47590'  # serverid

accuracy = 9 #accuracy

hashv = hashlib.md5(f"{ping}-{up}-{down}-297aae72".encode()).hexdigest()
headers = {
    'Host': 'www.speedtest.net',
    'User-Agent': 'DrWhat Speedtest',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'http://c.speedtest.net',
    'Referer': 'http://c.speedtest.net/flash/speedtest.swf',
    'Cookie': '', ## ur cookie, if need link results to an account
    'Connection': 'Close'
}

data = {
    'startmode': 'recommendedselect',
    'promo': '',
    'upload': up,
    'accuracy': accuracy,
    'recommendedserverid': server,
    'serverid': server,
    'ping': ping,
    'hash': hashv,
    'download': down
}
response = requests.post('https://www.speedtest.net/api/api.php', headers=headers, data=data)
resultid = re.search(r"resultid=(\d+)", response.text)
print('Result is ready. Link: https://www.speedtest.net/result/' + resultid.group(1))