from scrape import Scrape


if __name__ == "__main__":
    scrape = Scrape(username="<username_twitter>", password="<password_twitter>", keywords="film horor")
    scrape.run()