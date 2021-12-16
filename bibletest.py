import os
import re

bible_files = os.listdir("Scraped\\ENG_BIBLE")

kek_verses=[]
eng_verses= []

for file in bible_files:
    with open(f"Scraped\\ENG_BIBLE\\{file}", "r", encoding="utf8") as eng_in:
        english = eng_in.read()

    with open(f"Scraped\\KEK_BIBLE\\{file}", "r", encoding="utf8") as kek_in:
        qeqchi = kek_in.read()

    english = re.sub(r"\n+", " ", english)
    english = re.sub(r"\(.*?\)", "", english)
    english = re.sub(r"^\D+\d+\D+", "", english)
    english = re.split(r"\d+(?!\d)(?!\s)", english)

    qeqchi = re.sub(r"\n+", " ", qeqchi)
    qeqchi = re.sub(r"\(.*?\)", "", qeqchi)
    qeqchi = re.sub(r"^\D+\d+\D+", "", qeqchi)
    qeqchi = re.split(r"\d+(?!\d)(?!\s)", qeqchi)

    if len(qeqchi) == len(english):
        for verse in qeqchi:
            kek_verses.append(verse)
        
        for verse in english:
            eng_verses.append(verse)

with open("eng_test.txt", "w", encoding="utf8") as eng_out:
    for token in eng_verses:
        token = token.rstrip()
        if len(token) > 5:
            eng_out.write(token + "\n")

with open("kek_test.txt", "w", encoding="utf8") as kek_out:
    for token in kek_verses:
        token = token.rstrip()
        if len(token) > 5:
            kek_out.write(token + "\n")


