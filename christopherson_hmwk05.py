import requests_html
import random, re, os
from time import sleep

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
url = "https://www.churchofjesuschrist.org/study/general-conference/2021/04?lang=kek"

session = requests_html.HTMLSession()

r = session.get(url, headers=headers)

talks = r.html.find('body')

links = [i.absolute_links for i in talks]

print(type(links[0]))
links = sorted(list(links[0]))

links = [i for i in links if not re.search(r"session\?lang=kek", i)] #: Remove whole session pages without text
links = [i for i in links if re.search(r"lang=kek$", i)]

with open("links.txt", 'a') as lnkfile:
    for link in links:
        lnkfile.write(link + "\n")

#filenumber = 1
for link in links:
    print(link)
    r = session.get(link, headers=headers)
    text = r.html.find(".body-block")
    text = [i.text for i in text]
    
    try:
        text = text[0]
    except:
        print("This link contains no text, continuing....")
        continue 	

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

    with open("TXT\\" + str(filename) + ".txt", "w", encoding = "utf8") as outfile:
        outfile.write(link + "\n")
        outfile.write(title + "\n")
        outfile.write(speaker + "\n")
        outfile.write(text + "\n")

    nap = random.uniform(0.5, 1.5)
    print("\t taking a nap for " + str(nap) + " seconds...")
    sleep(nap)

