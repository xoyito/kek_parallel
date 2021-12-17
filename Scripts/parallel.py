from nltk.tokenize import sent_tokenize
import re, os

# List files in general conference directories
eng_files = os.listdir("Scraped\\ENG_GC")
kek_files= os.listdir("Scraped\\KEK_GC")

# define empty lists to hold tokens
eng = []
kek = []

# loop through english files 
for file in eng_files:
    # open connection to English file
    with open("Scraped\\ENG_GC\\" + file, "r", encoding="utf8") as eng_file:
        eng_temp = eng_file.read()
        eng_temp = re.sub(r"\n", " ", eng_temp) 
        eng_temp_tokens = sent_tokenize(eng_temp) #: divide sentences with nltk to create temporary list of tokens
    print(f"Loading {file}...")
    
    # replace ending to open Q'eqchi' file
    kek_file = re.sub(r"\-eng.txt$", "-kek.txt", file)
    print(f"Loading {kek_file}...")
    with open("Scraped\\KEK_GC\\" + kek_file, "r", encoding="utf8") as queq_file:
        kek_temp = queq_file.read()
        kek_temp = re.sub(r"\n", " ", kek_temp)
        kek_temp_tokens = sent_tokenize(kek_temp) #: divide sentences with nltk to create temporary list of tokens

    # if the sentences are properly aligned add them to the permanent list of sentences
    if len(kek_temp_tokens) == len(eng_temp_tokens):
        print("Adding files to parallel corpus...")
        for token in kek_temp_tokens:
            kek.append(token)

        for token in eng_temp_tokens:
            eng.append(token)
    
    else:
        print("These files have an allignment issue moving on...")
        continue

kek_triple = os.listdir("Scraped\\KEK_TRIPLE")

# Loop through text files from the triple combination
for file in kek_triple:

    # define English file by replacing ending of Q'eqchi' file
    eng_file = re.sub(r"\-kek.txt$", "-eng.txt", file)

    # Open Q'eqchi' file
    with open("Scraped\\KEK_TRIPLE\\" + file, "r", encoding="utf8") as kek_file:
        print(f"Loading {file}...")
        kek_temp = kek_file.read()
        kek_temp = re.sub(r"\n", " ", kek_temp)
        kek_temp_tokens = sent_tokenize(kek_temp) #: divide sentences with nltk to create temporary list of tokens

    with open("Scraped\\ENG_TRIPLE\\" + eng_file, "r", encoding="utf8") as english_file:
        eng_temp = english_file.read()
        eng_temp = re.sub(r"\n", " ", eng_temp)
        eng_temp_tokens = sent_tokenize(eng_temp) #: divide sentences with nltk to create temporary list of tokens

    # if the sentences are properly aligned add them to the permanent list of sentences
    if len(kek_temp_tokens) == len(eng_temp_tokens):
        print("Adding files to parallel corpus...")
        for token in kek_temp_tokens:
            kek.append(token)

        for token in eng_temp_tokens:
            eng.append(token)
    
    else:
        print("These files have an allignment issue moving on...")
        continue

# English post processing
for i, token in enumerate(eng):
    token = re.sub(r"\n", "", token) #: remove excessive newline characters 
    token = re.sub(r"\d+", "", token) #: remove digits (usually verse numbers)
    token = re.sub(r"[,|\.|\"|“|”|\?|!|\(|\)]", "", token)  #: remove punctuation
    token = re.sub(r"’", "\'", token) #: Standardize ' symbol across corpus 
    token = re.sub(r"\A ", "", token) #: remove white space at the beginning of the tokens
    eng[i] = token

# Q'eqchi' post processing
for i, token in enumerate(kek):
    token = re.sub(r"\n", "", token) #: remove excessive newline characters
    token = re.sub(r"\d+", "", token) #: remove digits (usually verse numbers)
    token = re.sub(r"[,|\.|\"|“|”|\?|!|\(|\)]", "", token) #: remove punctuation
    token = re.sub(r"’", "\'", token) #: Standardize ' symbol across corpus
    token = re.sub(r"\A ", "", token) #: remove white space at the beginning of the tokens
    kek[i] = token

# write plain text English corpus file
with open("Corpus\\eng.txt", "w", encoding="utf8") as corp_file:
    for eng_sentence in eng:
        corp_file.write(eng_sentence + "\n")

# write plain text English corpus file
with open("Corpus\\kek.txt", "w", encoding="utf8") as kek_file:
    for kek_sentence in kek:
        kek_file.write(kek_sentence + "\n")
        
