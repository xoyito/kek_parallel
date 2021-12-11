import requests_html
import re
import os
# LOOK AT THIS LINK https://www.churchofjesuschrist.org/study/general-conference/2016/10/look-to-the-book-look-to-the-lord?lang=kek I don't think this is Q'eqchi'
# links = ["https://www.churchofjesuschrist.org/study/general-conference/2021/04/11nelson?lang=eng", "https://www.churchofjesuschrist.org/study/general-conference/2021/04/11nelson?lang=kek"]
links = ["https://www.churchofjesuschrist.org/study/general-conference/2021/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2021/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2020/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2020/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2019/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2019/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2018/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2018/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2017/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2016/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2016/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2015/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2015/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2014/04?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2007/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2006/10?lang=kek",
        "https://www.churchofjesuschrist.org/study/general-conference/2003/04?lang=kek"]

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
session = requests_html.HTMLSession()

talk_links = []

# get all links from conference session homepages
for link in links:
    print(f"Getting talk links from {link}")
    r = session.get(link, headers=headers)
    talks = r.html.find('body')
    temp_links = [i.absolute_links for i in talks]
    temp_links = sorted(list(temp_links[0]))
    
    for temp in temp_links:
        talk_links.append(temp)

talk_links = [i for i in talk_links if not re.search(r"session\?lang=kek", i)] #: Remove whole session pages without text
talk_links = [i for i in talk_links if re.search(r"lang=kek$", i)] #: include only Q'eqchi' links in list

eng_links = []

for link in talk_links:
    eng_links.append(re.sub(r"\?lang=kek$", "?lang=eng", link))

# document scraped links
# with open("Scraped\\kek_links.txt", "a", encoding="utf8") as link_file:
#     for link in talk_links:
#         link_file.write(link + "\n")

# with open("Scraped\\english_links.txt", "a", encoding="utf8") as link_file:
#     for link in eng_links:
#         link_file.write(link + "\n")

print(f"Links collected for {str(len(talk_links))} LDS General Conference talks in Q'eqchi'!")

# loop though links to talkks and get text
for link in talk_links:
    print(f"Getting text from {link}...")
    # get text from Q'eqchi' link
    r = session.get(link, headers=headers)
    kek_text = r.html.find(".body-block")
    kek_text = [i.text for i in kek_text]
    
    # handle textless links
    try:
        kek_text = kek_text[0]
    except:
        print("This link contains no text, continuing....")
        continue
    
    english_link = re.sub(r"\?lang=kek$", "?lang=eng", link)

    print(f"Getting English text from {english_link}...")
    
    # get text from English link
    r = session.get(english_link, headers=headers)
    eng_text = r.html.find(".body-block")
    eng_text = [i.text for i in eng_text]
    eng_text = eng_text[0]

    # generate Q'eqchi' filename and write to file
    kek_filename = os.path.basename(link)
    kek_filename = re.sub(r"\?lang=kek$", "-kek", kek_filename)
    with open("Scraped\\KEK_GC\\" + kek_filename + ".txt", "w", encoding="utf8") as outfile:
        outfile.write(kek_text)

    # generate English filename and write to file
    eng_filename = os.path.basename(english_link)
    eng_filename = re.sub(r"\?lang=eng$", "-eng", eng_filename)
    with open("Scraped\\ENG_GC\\" + eng_filename + ".txt", "w", encoding="utf8") as outfile:
        outfile.write(eng_text)
