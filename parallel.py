import requests_html
import re
import os

link ="https://www.churchofjesuschrist.org/study/general-conference/2021/04/11nelson?lang=kek"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
session = requests_html.HTMLSession()

r = session.get(link, headers=headers)
text = r.html.find(".body-block")
text = [i.text for i in text]

try:
    text = text[0]
except:
    print("This link contains no text, continuing....")

title = r.html.find("#title1")
title = title[0]
title = title.text
title = "\"" + title +"\""
print(title)

speaker = r.html.find(".byline")
speaker = speaker[0]
speaker = speaker.text
print(speaker)

filename = os.path.basename(link)
filename = re.sub(r"\?lang=kek$", "", filename)