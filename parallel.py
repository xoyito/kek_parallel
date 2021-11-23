from nltk.tokenize import sent_tokenize
import re, os

eng_files = os.listdir("ENG_TXT")
kek_files= os.listdir("KEK_TXT")

eng = []
kek = []

for file in eng_files:
    with open("ENG_TXT\\" + file, "r", encoding="utf8") as eng_file:
        eng_temp = eng_file.read()
        eng_temp = re.sub(r"\n", "", eng_temp)
        eng_temp_tokens = sent_tokenize(eng_temp)
    print(f"Loading {file}...")
    
    kek_file = re.sub(r"\-eng.txt$", "-kek.txt", file)
    print(f"Loading {kek_file}...")
    with open("KEK_TXT\\" + kek_file, "r", encoding="utf8") as queq_file:
        kek_temp = queq_file.read()
        kek_temp = re.sub(r"\n", "", kek_temp)
        kek_temp_tokens = sent_tokenize(kek_temp)

    if len(kek_temp_tokens) == len(eng_temp_tokens):
        print("Adding files to parallel corpus...")
        for token in kek_temp_tokens:
            kek.append(token)

        for token in eng_temp_tokens:
            eng.append(token)
    
    else:
        print("These files have an allignment issue moving on...")
        continue

    

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
# eng = re.sub(r"\n", " ", eng)
# eng = re.sub(r"[0-9]", "", eng)
# eng = re.sub(r"“|”", "", eng)
# eng = re.sub(r"\t", "", eng)
# eng = re.sub(r"\.\.\.", "", eng)
# eng = re.sub(r"…", "", eng)

# kek = re.sub(r"\n", " ", kek)
# kek = re.sub(r"[0-9]", "", kek)
# kek = re.sub(r"“|”", "", kek)
# kek = re.sub(r"\t", "", kek)
# kek = re.sub(r"\.\.\.", "", kek)
# kek = re.sub(r"…", "", kek)

with open("eng.txt", "w", encoding="utf8") as corp_file:
        for eng_sentence in eng:
            corp_file.write(eng_sentence + "\n")

with open("kek.txt", "w", encoding="utf8") as kek_file:
    for kek_sentence in kek:
        kek_file.write(kek_sentence + "\n")
        
