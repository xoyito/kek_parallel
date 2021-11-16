import os
from nltk.tokenize import sent_tokenize

with open("TXT\\11nelson-eng.txt", "r", encoding="utf8") as infile:
    eng = infile.read()

with open("TXT\\11nelson-kek.txt", "r", encoding="utf8") as infile:
    kek = infile.read()

eng_tokens = sent_tokenize(eng)
kek_tokens = sent_tokenize(kek)

with open("tuples.txt", "w", encoding="utf8") as corp_file:
    for i, eng_sentence in enumerate(eng_tokens):
        tuple = f"(\"{eng_sentence}\", \"{kek_tokens[i]}\")"
        corp_file.write(tuple + "\n")
