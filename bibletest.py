import os
import re

bible_files = os.listdir("ENG_BIBLE")

with open("eng_test.txt", "w", encoding="utf8") as eng_out:
    with open("kek_test.txt", "w", encoding="utf8") as kek_out:
        for file in bible_files:
            with open(f"ENG_BIBLE\\{file}", "r", encoding="utf8") as eng_inf:
                eng_chapter = eng_inf.read()

            eng_chapter = re.sub(r"^\D+\d+\D+", "", eng_chapter)
            eng_chapter = re.sub(r"\n+", "", eng_chapter)
            eng_verses = re.split(r"\d", eng_chapter)

            with open(f"KEK_BIBLE\\{file}", "r", encoding="utf8") as kek_inf:
                kek_chapter = kek_inf.read()

            kek_chapter = re.sub(r"^\D+\d+\D+\(.+\)*\D*", "", kek_chapter)
            kek_chapter = re.sub(r"\n+", "", kek_chapter)
            kek_verses = re.split(r"\d", kek_chapter)

            for verse in eng_verses:
                if len(verse) < 5:
                    eng_verses.remove(verse)

            for verse in eng_verses:
                eng_out.write(verse + "\n")

            for verse in kek_verses:
                if len(verse) < 5:
                    kek_verses.remove(verse)

            for verse in kek_verses:
                kek_out.write(verse + "\n")




    
