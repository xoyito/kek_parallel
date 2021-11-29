import requests_html
import re
import os

kek_issues = ["https://www.jw.org/kek/tojak/eblihu/ajsiaawu-2021-ajl3-nov-dic/"]
eng_issues = ["https://www.jw.org/en/library/magazines/awake-no3-2021-nov-dec/"]

kek_links = []
eng_links = []

css = "#article"

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
session = requests_html.HTMLSession()

for link in kek_issues:
    r = session.get(link, headers=headers)
    link_html = r.html.find(css)

    temp_links = [i.absolute_links for i in link_html]
    temp_links = list(temp_links[0])

    print(temp_links)