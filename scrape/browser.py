from .utils import helper
from typing import Optional, Dict, List, Any
from playwright.async_api import async_playwright


class Browser:
    def __init__(self, username: Optional[str] = None, password: Optional[str] = None):
        if not username:
            raise Exception("parameter 'username' not found")
        if not password:
            raise Exception("parameter 'password' not found")
        
        self.__username = username
        self.__password = password

        self.__browser = None
        self.__context = None
        self.__page = None
        self.__context = None
        self.__base_url = "https://x.com"
        
        self.headers_auth = None

    async def __start_browser(self):
        playwright = await async_playwright().start()
        self.__browser = await playwright.chromium.launch(headless=False)
        self.__context = await self.__browser.new_context()
        cookies = helper.load_cookies(cookies_name=self.__username)
        if cookies is not None:
            await self.__context.add_cookies(cookies=cookies)
        self.__page = await self.__context.new_page()
        self.__page.on("request", self.__callback)

    async def __goto_page(self, url):
        await self.__page.goto(url)
    
    async def __click_handler(self, locator):
        await self.__page.wait_for_selector(locator)
        button = await self.__page.query_selector(locator)
        await button.click()

    async def __fill_handler(self, locator, value):
        await self.__page.wait_for_selector(locator)
        input = await self.__page.query_selector(locator)
        await input.fill(value=value)

    async def __close_browser(self):
        await self.__browser.close()
    
    async def __login(self):
        await self.__goto_page(f"{self.__base_url}")
        sign_locator = "//a[@role='link' and @data-testid='loginButton']"
        await self.__click_handler(sign_locator)
        username_locator = "//input[@autocomplete='username' and @type='text']"
        await self.__fill_handler(locator=username_locator, value=self.__username)
        next_username_locator = "//button[@role='button' and div/span/span/text()='Next']"
        await self.__click_handler(next_username_locator)
        password_locator = "//input[@type='password' and @name='password']"
        await self.__fill_handler(locator=password_locator, value=self.__password)
        login_button_locator = "//button[@role='button' and @data-testid='LoginForm_Login_Button']"
        await self.__click_handler(login_button_locator)
        tweet_input_locator = "//div[@data-testid='tweetTextarea_0' and @role='textbox']"
        await self.__page.wait_for_selector(tweet_input_locator)
        cookies = await self.__context.cookies()
        helper.save_cookies(cookies=cookies, cookies_name=self.__username)
    
    async def __callback(self, req):
        if f"{self.__base_url}/i/api/graphql/" in req.url and "SearchTimeline" in req.url:
            self.headers_auth = await req.headers_array()
            

    async def __search_topic(self, keyword: Optional[str] = None):
        if not keyword:
            raise Exception("keyword not found")
        await self.__goto_page(f"{self.__base_url}/search?q={helper.url_encode(keyword)}&src=typed_query&f=live")
        last_element_text = None
        while True:
            if self.headers_auth is not None:
                break
            await self.__page.wait_for_selector("(//div[@data-testid='cellInnerDiv'])[last()]")
            last_element = await self.__page.query_selector("(//div[@data-testid='cellInnerDiv'])[last()]")
            await last_element.scroll_into_view_if_needed()
            new_last_element_text = await last_element.inner_text()
            if new_last_element_text == last_element_text:
                break
            else:
                last_element_text = new_last_element_text

    async def run(self, keyword = None):
        await self.__start_browser()
        cookies = helper.load_cookies(cookies_name=self.__username)
        if cookies is None:
            await self.__login()
        await self.__search_topic(keyword=keyword)
        await self.__close_browser()