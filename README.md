# Twitter Scrape

bot untuk scrapping twitter

## Installasi

### Persiapan

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

## Run

Sebelum kita menjalankan program kita edit dahulu main.py

```python

from scrape import Scrape


if __name__ == "__main__":
    # Ganti Keyword dengan keyword yng anda cari
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
        #ganti username dan password twitter anda
        scrape = Scrape(username="<username twitter>", password="<password twitter>", keywords=keyword)
        scrape.run()
```

baru bisa kita jalankan program

```bash
python main.py
```
