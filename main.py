from scrape import Scrape


if __name__ == "__main__":
    keywords = [
        "film horor",
        "pendapat film horor",
        "tanggapan film horor",
        "film horor trending",
        "film horor viral",
        "film horor update",
        "setelah nonton film horor",
        "saat nonton film horor",
        "film horor yg sedang di tunggu",
        "review film horor",
        "horor movie",
        "horor movie trending",
    ]
    for keyword in keywords:
        scrape = Scrape(username="CorpsPakde87790", password="qwertyui32!", keywords=keyword)
        scrape.run()