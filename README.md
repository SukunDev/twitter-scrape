# Twitter Scrape

bot untuk scrapping twitter

## Installasi

### Persiapan

Install dan masukkan ke dalam environment variable

- [MongoDB](https://www.mongodb.com/try/download/community)
- [Mongo Shell](https://www.mongodb.com/try/download/shell)
- [Mongo Database Tools](https://www.mongodb.com/try/download/database-tools)

### Cloning Repo

```bash
git clone https://github.com/SukunDev/twitter-scrape.git
cd twitter-scrape
```

### Instalasi di CMD

```bash
python -m venv .venv
cd .venv/Scripts
activate
cd ../..
pip install -r requirements.txt
```

### Installasi di Git Bash

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

### Migrasi Database

Import

```bash
mongorestore ./database_backup/bot_scrape --db bot_scrape
```

Export

```
mongodump -d bot_scrape -o database_backup
```

export to csv

```
mongoexport --host localhost --db bot_scrape --collection tweet --type=csv --out film_horor_collection.csv --fields tweet_link,full_text,bookmark_count,favorite_count,quote_count,reply_count,retweet_count,lang,user,entities,extended_entities,created_at
```

## Run

Sebelum kita menjalankan program kita edit dahulu main.py

```python
from scrape import Scrape


if __name__ == "__main__":
    #ganti username dan password twitter anda
    scrape = Scrape(username="<username_twitter>", password="<password_twitter>", keywords="film horor")
    scrape.run()
```

baru bisa kita jalankan program

```bash
python main.py
```
