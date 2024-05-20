import sys
import asyncio
from .utils import helper
from .browser import Browser
from typing import Optional, Dict, List, Any
from .database.mongo_db_handler import MongoDBHandler


class Scrape:
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None, keywords : Optional[str] = None):
        if not username:
            raise Exception("parameter 'username' not found")
        if not password:
            raise Exception("parameter 'password' not found")
        if not keywords:
            raise Exception("parameter 'keywords' not found")

        self.__keywords = keywords

        self.__browser = Browser(username=username, password=password)
        asyncio.run(self.__browser.run(keyword=self.__keywords))
        self.__base_url = "https://x.com"
        self.__headers = {}
        self.__path = None
        self.__params = None
        self.__db_handler = MongoDBHandler()

        self.__skip_count = 0
        for header in self.__browser.headers_auth:
            if header['name'] == 'authorization':
                self.__headers.update({"Authorization": header['value']})
            if header['name'] == 'cookie':
                self.__headers.update({"Cookie": header['value']})
            if header['name'] == 'user-agent':
                self.__headers.update({"User-Agent": header['value']})
            # if header['name'] == 'x-client-transaction-id':
            #     self.__headers.update({"X-Client-Transaction-Id": header['value']})
            if header['name'] == 'x-client-uuid':
                self.__headers.update({"X-Client-Uuid": header['value']})
            if header['name'] == 'x-csrf-token':
                self.__headers.update({"X-Csrf-Token": header['value']})
            if header['name'] == 'x-twitter-active-user':
                self.__headers.update({"X-Twitter-Active-User": header['value']})
            if header['name'] == 'x-twitter-auth-type':
                self.__headers.update({"X-Twitter-Auth-Type": header['value']})
            if header['name'] == 'x-twitter-client-language':
                self.__headers.update({"X-Twitter-Client-Language": header['value']})
            if header['name'] == ':path':
                self.__path = header['value']
        self.__path, self.__params = helper.split_url(self.__path)
    
    def __parse_data(self, data):
        results = []
        for instructions in data['data']['search_by_raw_query']['search_timeline']['timeline']['instructions']:
            if instructions['type'] == "TimelineAddEntries":
                for entry in instructions['entries']:
                    if 'tweet-' in entry['entryId']:
                        try:
                            result = entry['content']['itemContent']['tweet_results']['result']
                            user_results = result['core']['user_results']['result']
                            tweet_bucket = {
                                'tweet_link': f"{self.__base_url}/{user_results['legacy']['screen_name']}/status/{result['legacy']['conversation_id_str']}",
                                'full_text': result['legacy']['full_text'],
                                'bookmark_count': result['legacy']['bookmark_count'],
                                'created_at': result['legacy']['created_at'],
                                'entities': result['legacy']['entities'],
                                'favorite_count': result['legacy']['favorite_count'],
                                'lang': result['legacy']['lang'],
                                'quote_count': result['legacy']['quote_count'],
                                'reply_count': result['legacy']['reply_count'],
                                'retweet_count': result['legacy']['retweet_count'],
                            }
                            try:
                                tweet_bucket.update({
                                    'extended_entities': result['legacy']['extended_entities'],
                                })
                            except:
                                tweet_bucket.update({
                                    'extended_entities': None,
                                })
                            results.append({
                                "tweet": tweet_bucket,
                                "user":{
                                    'name': user_results['legacy']['name'],
                                    'username': user_results['legacy']['screen_name'],
                                    'verified': user_results['legacy']['verified'],
                                    'followers_count': user_results['legacy']['followers_count'],
                                    'followers_count': user_results['legacy']['followers_count'],
                                    'profile_image_url_https': user_results['legacy']['profile_image_url_https'],
                                }
                            })
                        except Exception as e:
                            self.__skip_count += 1
                            print(f"{helper.putih}[{self.__skip_count}] Skip {helper.merah}{str(e)}")
                            continue
                    if 'cursor-bottom-' in entry['entryId']:
                        self.__params.update({
                            "variables":{
                                'rawQuery': self.__keywords,
                                'count': 20,
                                "cursor": entry['content']['value'],
                                "querySource": "typed_query",
                                "product": "Latest"
                            }
                        })
            else:
                if 'cursor-bottom-' in instructions['entry']['entryId']:
                    self.__params.update({
                        "variables":{
                            'rawQuery': self.__keywords,
                            'count': 20,
                            "cursor": instructions['entry']['content']['value'],
                            "querySource": "typed_query",
                            "product": "Latest"
                        }
                    })
        return results

    def run(self):
        tweet_count = len(self.__db_handler.find_all(collection_name="tweet"))
        max_data = 10000
        if tweet_count >= max_data:
            print(f"{helper.kuning} Data sudah mencapai target {helper.putih}{tweet_count}/{max_data}")
            sys.exit()
        self.__params.update({
            "variables":{
                'rawQuery': self.__keywords,
                'count': 20,
                "querySource": "typed_query",
                "product": "Latest"
            }
        })
        while True:
            response = helper.request(url=f"{self.__base_url}{helper.join_url(self.__path, self.__params)}", headers=self.__headers)
            if "Rate limit exceeded" in response.text:
                raise Exception(response.text)
            if response.status_code != 200:
                raise Exception("Requests Error")
                
            items = self.__parse_data(response.json())
            if len(items) < 1:
                break
                # helper.countdown(60, tweet_count, max_data)
                # continue
            for item in items:
                if self.__db_handler.find_one('tweet', {"tweet_link": item['tweet']['tweet_link']}) is None:
                    self.__db_handler.insert_one('tweet', {
                        "tweet_link": item['tweet']['tweet_link'],
                        "full_text": item['tweet']['full_text'],
                        "bookmark_count": item['tweet']['bookmark_count'],
                        "entities": item['tweet']['entities'],
                        "extended_entities": item['tweet']['extended_entities'],
                        "favorite_count": item['tweet']['favorite_count'],
                        "quote_count": item['tweet']['quote_count'],
                        "reply_count": item['tweet']['reply_count'],
                        "retweet_count": item['tweet']['retweet_count'],
                        "lang": item['tweet']['lang'],
                        "user": item['user'],
                        "created_at": item['tweet']['created_at'],
                    })
                    tweet_count += 1
                    print(f"{helper.hijau}Berhasil menyimpan{helper.putih} {item['tweet']['tweet_link']}")
                else:
                    print(f"{helper.putih}{item['tweet']['tweet_link']}{helper.kuning} sudah tersimpan")
            if tweet_count >= max_data:
                break
            helper.countdown(30, tweet_count, max_data)


