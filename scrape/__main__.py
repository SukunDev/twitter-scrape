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
        # self.__browser.headers_auth = [{'name': ':authority', 'value': 'x.com'}, {'name': ':method', 'value': 'GET'}, {'name': ':path', 'value': '/i/api/graphql/Ow4YOCqr4TR1W5vDqb0HAw/SearchTimeline?variables=%7B%22rawQuery%22%3A%22film%20horor%22%2C%22count%22%3A20%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Top%22%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'}, {'name': ':scheme', 'value': 'https'}, {'name': 'accept', 'value': '*/*'}, {'name': 'accept-encoding', 'value': 'gzip, deflate, br, zstd'}, {'name': 'accept-language', 'value': 'en-US,en;q=0.9'}, {'name': 'authorization', 'value': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA'}, {'name': 'content-type', 'value': 'application/json'}, {'name': 'cookie', 'value': 'guest_id=171612827660471060; night_mode=2; guest_id_marketing=v1%3A171612827660471060; guest_id_ads=v1%3A171612827660471060; _ga=GA1.2.237836962.1716128290; _gid=GA1.2.274402834.1716128290; kdt=FXtz3ShPZQY6sXEoDZ0J7U0K0zlv0aVr3gNaZxCy; auth_token=de17bba4acd07b46f47c3b157dad4bc63835f48e; ct0=49696fa6ce86cf068fe83fe268a0744e73c18f1682b6fa387c3c9639cde3f905619b151749142e2a87ce23b6e733d37df6e1270c7e026273a0afeee5cc08d3407b6b004c969d24b853245bd44579bcbe; att=1-bKuK09ZWJcOsSfBt98198Gc1Ymu5QyQcH6oqjjE6; lang=en; twid=u%3D1792020109340598272; personalization_id="v1_sgkfIt1/sxgyl6nRQbEsyw=="'}, {'name': 'priority', 'value': 'u=1, i'}, {'name': 'referer', 'value': 'https://x.com/search?q=film%20horor&src=typed_query&f=top'}, {'name': 'sec-ch-ua', 'value': '"Chromium";v="125", "Not.A/Brand";v="24"'}, {'name': 'sec-ch-ua-mobile', 'value': '?0'}, {'name': 'sec-ch-ua-platform', 'value': '"Windows"'}, {'name': 'sec-fetch-dest', 'value': 'empty'}, {'name': 'sec-fetch-mode', 'value': 'cors'}, {'name': 'sec-fetch-site', 'value': 'same-origin'}, {'name': 'user-agent', 'value': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}, {'name': 'x-client-transaction-id', 'value': 'yrVumRgZECCVJhGXE3igl9Qv6EYJYbC1GR7e7w7rfpQD3kYCZX/Xh9cpTMsvf46ECbwEMMsrY4T9luFI5Nvj8fnoLdHfyQ'}, {'name': 'x-csrf-token', 'value': '49696fa6ce86cf068fe83fe268a0744e73c18f1682b6fa387c3c9639cde3f905619b151749142e2a87ce23b6e733d37df6e1270c7e026273a0afeee5cc08d3407b6b004c969d24b853245bd44579bcbe'}, {'name': 'x-twitter-active-user', 'value': 'yes'}, {'name': 'x-twitter-auth-type', 'value': 'OAuth2Session'}, {'name': 'x-twitter-client-language', 'value': 'en'}]
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
