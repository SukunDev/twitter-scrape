# Twitter Scrape

Bot untuk scraping data dari Twitter.

## Installasi

### Persiapan

Sebelum memulai, pastikan Anda telah menginstal dan menambahkan ke dalam environment variable:

- [MongoDB](https://www.mongodb.com/try/download/community)
- [Mongo Shell](https://www.mongodb.com/try/download/shell)
- [Mongo Database Tools](https://www.mongodb.com/try/download/database-tools)

### Cloning Repository

```bash
git clone https://github.com/SukunDev/twitter-scrape.git
cd twitter-scrape
```

### Instalasi di Command Prompt (CMD)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Instalasi di Git Bash

```bash
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

## Migrasi Database

### Import Database

```bash
mongorestore ./database_backup/bot_scrape --db bot_scrape
```

### Export Database

```bash
mongodump -d bot_scrape -o database_backup
```

### Export ke CSV

```bash
mongoexport --host localhost --db bot_scrape --collection tweet --type=csv \
--out film_horor_collection.csv --fields tweet_link,full_text,bookmark_count, \
favorite_count,quote_count,reply_count,retweet_count,lang,user,entities, \
extended_entities,created_at
```

## Menjalankan Program

Sebelum menjalankan program, edit terlebih dahulu file `main.py`:

```python
from scrape import Scrape

if __name__ == "__main__":
    # Ganti dengan username dan password Twitter Anda
    scrape = Scrape(username="<username_twitter>", password="<password_twitter>", keywords="film horor")
    scrape.run()
```

Setelah itu, jalankan program dengan perintah:

```bash
python main.py
```

## Kontribusi

Kami menerima kontribusi dari siapa saja! Jika Anda ingin berkontribusi, ikuti langkah berikut:

1. Fork repository ini.
2. Buat branch baru untuk fitur atau perbaikan Anda.
3. Commit perubahan Anda dengan deskripsi yang jelas.
4. Push ke repository Anda dan buat pull request ke repository utama.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).
