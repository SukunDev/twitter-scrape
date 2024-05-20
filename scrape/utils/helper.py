import os
import json
import time
import pickle
import requests
import urllib.parse
from colorama import *

init(autoreset=True)

merah = Fore.LIGHTRED_EX
putih = Fore.LIGHTWHITE_EX
hijau = Fore.LIGHTGREEN_EX
kuning = Fore.LIGHTYELLOW_EX
biru = Fore.LIGHTBLUE_EX

def request(url, data = None, headers = None):
    if not data:
        response = requests.get(url=url, headers=headers)
    else:
        response = requests.post(url=url, headers=headers, data=data)
    return response

def convert_to_int(value):
    value = value.lower()
    if value.endswith('k'):
        return int(float(value[:-1]) * 1000)
    elif value.endswith('m'):
        return int(float(value[:-1]) * 1000000)
    elif value.endswith('b'):
        return int(float(value[:-1]) * 1000000000)
    else:
        return int(value)

def url_encode(string):
    url_encoded = urllib.parse.quote(string)
    return  url_encoded

def url_decode(string):
    url_decoded = urllib.parse.unquote(string)
    return  url_decoded

def split_url(url):
    parsed_url = urllib.parse.urlsplit(url)
    path = parsed_url.path
    params = urllib.parse.parse_qs(parsed_url.query)
    for key, value in params.items():
        if isinstance(value, list) and len(value) == 1:
            try:
                params[key] = json.loads(value[0])
            except json.JSONDecodeError:
                params[key] = value[0]

    return path, params

def join_url(path, params):
    for key, value in params.items():
        if isinstance(value, dict):
            params[key] = json.dumps(value)

    query_string = urllib.parse.urlencode(params)
    full_url = urllib.parse.urlunsplit(('', '', path, query_string, ''))
    return full_url

def save_cookies(cookies, cookies_name):
    if not os.path.exists(os.path.join(os.getcwd(), ".temp")):
        os.makedirs(os.path.join(os.getcwd(), ".temp"))
    with open(os.path.join(os.getcwd(), ".temp", f'{cookies_name}_cookies'), 'wb') as f:
        pickle.dump(cookies, f)

def load_cookies(cookies_name):
    try:
        if not os.path.exists(os.path.join(os.getcwd(), ".temp")):
            os.makedirs(os.path.join(os.getcwd(), ".temp"))
        with open(os.path.join(os.getcwd(), ".temp", f'{cookies_name}_cookies'), 'rb') as f:
            cookies = pickle.load(f)
    except Exception as e:
        cookies = None
    return cookies

def countdown(t, tweet_count, max_data):
        while t:
            menit, detik = divmod(t, 60)
            jam, menit = divmod(menit, 60)
            jam = str(jam).zfill(2)
            menit = str(menit).zfill(2)
            detik = str(detik).zfill(2)
            print(f"{hijau}[{putih}{jam}:{menit}:{detik}{hijau}] {kuning}Sleeping {putih}{tweet_count}/{max_data}", flush=True, end="\r")
            t -= 1
            time.sleep(1)
        print("                                        ", flush=True, end="\r")