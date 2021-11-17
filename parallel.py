from nltk.tokenize import sent_tokenize
import re, os

eng_files = os.listdir("ENG_TXT")
kek_files= os.listdir("KEK_TXT")

eng = ""
kek = ""

for i, file in enumerate(eng_files):
    with open("ENG_TXT\\" + file, "r", encoding="utf8") as eng_file:
        eng = eng + eng_file.read()
    
    with open("KEK_TXT\\" + kek_files[i], "r", encoding="utf8") as kek_file:
        kek = kek + kek_file.read()

#####FIXME ISSUE WITH HOW SENTENCES LINE UP IN THE BIBLE SEE withbible.txt#####
# # bible processing
# bible_files = os.listdir("ENG_BIBLE")
# for file in bible_files:
#     with open("ENG_BIBLE\\" + file, "r", encoding="utf8") as eng_file:
#         eng_chapter = eng_file.read()
    
#     with open("KEK_BIBLE\\" + file, "r", encoding="utf8") as kek_file:
#         kek_chapter = kek_file.read()
    
#     eng_chapter = re.sub(r"\A.+\n*.*\n*.*\n+1", "", eng_chapter)
#     kek_chapter = re.sub(r"\A.+\n*.*\n*.*\n+1", "", kek_chapter)

#     eng = eng + "\n" + eng_chapter
#     kek = kek + "\n" + kek_chapter

# post processing
eng = re.sub(r"\n", " ", eng)
eng = re.sub(r"[0-9]", "", eng)
eng = re.sub(r"“|”", "", eng)
eng = re.sub(r"\t", "", eng)

kek = re.sub(r"\n", " ", kek)
kek = re.sub(r"[0-9]", "", kek)
kek = re.sub(r"“|”", "", kek)
kek = re.sub(r"\t", "", kek)

eng_tokens = sent_tokenize(eng)
kek_tokens = sent_tokenize(kek)

with open("tuples.txt", "w", encoding="utf8") as corp_file:
    for i, eng_sentence in enumerate(eng_tokens):
        tuple = eng_sentence + "\t" + kek_tokens[i]
        corp_file.write(tuple + "\n")
