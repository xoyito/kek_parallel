from nltk.tokenize import sent_tokenize
import re

with open("TXT\\11nelson-eng.txt", "r", encoding="utf8") as infile:
    eng = infile.read()

with open("TXT\\11nelson-kek.txt", "r", encoding="utf8") as infile:
    kek = infile.read()
    
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
        # tuple = f"(\"{eng_sentence}\", \"{kek_tokens[i]}\")"
        tuple = eng_sentence + "\t" + kek_tokens[i]
        corp_file.write(tuple + "\n")
