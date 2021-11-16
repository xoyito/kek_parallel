import requests_html
import random, re, os
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
url = "https://www.bible.com/bible/543/GEN.1.QQC"

session = requests_html.HTMLSession()

r = session.get(url, headers=headers)
text = r.html.find(".p")
text = [i.text for i in text]

print(text)