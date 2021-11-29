import requests_html
import re
import os

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
session = requests_html.HTMLSession()

links = []
#: Add links for BOM Title page and witnesses
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/bofm-title?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/introduction?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/three?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/eight?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/js?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/explanation?lang=kek")

#: links with links to 1 Nefi
i = 0
while i < 22:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/1-ne/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to 2 Nefi
i = 0
while i < 33:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/2-ne/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Jakob
i = 0
while i < 7:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/jacob/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Add links to Enos, Jarom, Omni, Raatin laj Mormon
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/enos/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/jarom/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/omni/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/w-of-m/1?lang=kek")

#: Populate links with links to Mosiah
i = 0
while i < 29:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/mosiah/"+ str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Alma
i = 0
while i < 63:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/alma/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Helaman
i = 0
while i < 16:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/hel/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to 3 Nefi
i = 0
while i < 30:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/3-ne/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Add link to 4 Nefi
links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/4-ne/1?lang=kek")

#: Populate links with links to Mormon
i = 0
while i < 9:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/morm/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Eter
i = 0
while i < 15:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/ether/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Moroni
i = 0
while i < 10:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/bofm/moro/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to D&C
i = 0
while i < 138:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/dc-testament/dc/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Add Links to official declarations and Pearl of Great Price Title page
links.append("https://www.churchofjesuschrist.org/study/scriptures/dc-testament/od/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/dc-testament/od/2?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/introduction?lang=kek")

#: Populate links with links to Moses
i = 0
while i < 8:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/moses/" + str(1+i) + "?lang=kek")
    i = i + 1

#: Populate links with links to Abraham
i = 0
while i < 5:
    links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/abr/" + str(1+i) + "?lang=kek")
    i = i + 1

#: add links to Joseph Smith Matthew and History and Articles of Faith
links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/js-m/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/js-h/1?lang=kek")
links.append("https://www.churchofjesuschrist.org/study/scriptures/pgp/a-of-f/1?lang=kek")

# with open("scraped_links.txt", "a", encoding="utf8") as link_file:
#     for link in links:
#         link_file.write(link + "\n")

# eng_links = []
# for link in links:
#     eng_links.append(re.sub(r"\?lang=kek$", "?lang=eng", link))

for link in links:
    print(f"Getting text from {link}...")
    r = session.get(link, headers=headers)
    kek_text = r.html.find(".body-block")
    kek_text = [i.text for i in kek_text]

    try:
        kek_text = kek_text[0]
    except:
        print("This link contains no text, continuing....")
        continue
    
    english_link = re.sub(r"\?lang=kek$", "?lang=eng", link)

    print(f"Getting English text from {english_link}...")
    
    r = session.get(english_link, headers=headers)
    eng_text = r.html.find(".body-block")
    eng_text = [i.text for i in eng_text]
    eng_text = eng_text[0]

    kek_filename = re.sub(r"https://www.churchofjesuschrist.org/study/scriptures/", "", link)
    kek_filename = re.sub(r"\?lang=kek$", "-kek", kek_filename)
    kek_filename = re.sub(r"/", "-", kek_filename)
    with open("KEK_TRIPLE\\" + kek_filename + ".txt", "w", encoding="utf8") as outfile:
        outfile.write(kek_text)

    eng_filename = re.sub(r"https://www.churchofjesuschrist.org/study/scriptures/", "", english_link)
    eng_filename = re.sub(r"\?lang=eng$", "-eng", eng_filename)
    eng_filename = re.sub("/", "-", eng_filename)
    with open("ENG_TRIPLE\\" + eng_filename + ".txt", "w", encoding="utf8") as outfile:
        outfile.write(eng_text)