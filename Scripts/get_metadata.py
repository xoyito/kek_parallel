import nltk
from nltk.tokenize import word_tokenize

with open("Corpus\\eng.txt", "r", encoding="utf8") as eng_in:
    eng_text = eng_in.read()

with open("Corpus\\kek.txt", "r", encoding="utf8") as kek_in:
    kek_text = kek_in.read()

with open("Corpus\\kek.txt", "r", encoding="utf8") as sentences_file:
    sentences = sentences_file.readlines()

with open("Scraped\\english_links.txt", "r", encoding="utf8") as eng_linkfile:
    eng_links = eng_linkfile.readlines()

with open("Scraped\\kek_links.txt", "r", encoding="utf8") as kek_linkfile:
    kek_links = kek_linkfile.readlines()

with open("corpus_metadata.txt", "w", encoding="utf8") as meta_data:
    meta_data.write(f"This is the Q'eqchi'-English Parallel Corpus\nThe corpus contains Q'eqchi' text scraped from {len(kek_links)} URLs and English text scraped from {len(eng_links)} URLs.\n")
    meta_data.write("Lists of URLS that were scraped can be found in the Scraped directory as english_links.txt and kek_links.txt.\n\n\n")
    
    eng_text = eng_text.lower()
    kek_text = kek_text.lower()

    eng_words = word_tokenize(eng_text)
    kek_words = word_tokenize(kek_text)

    eng_dict = {}
    kek_dict = {}

    for word in eng_words:
        if word not in eng_dict:
            eng_dict[word] = 1
        else:
            eng_dict[word] = eng_dict[word] + 1

    for word in kek_words:
        if word not in kek_dict:
            kek_dict[word] = 1
        else:
            kek_dict[word] = kek_dict[word] + 1

    meta_data.write(f"The full scraped text can be found in the Scraped directory, a script called parallel.py lines up the sentences that can be easily alligned into the files in the corpus directory.\nThe parallel sentences are available in plain text and .json format in the Corpus directory.\n\n")
    meta_data.write(f"The parallel corpus contains:\n\n\t{len(sentences)} parallel sentences.\n\n\t{len(eng_words)} English words and {len(eng_dict)} unique English tokens.\n\n\t{len(kek_words)} Q'eqchi' words and {len(kek_dict)} unique Q'eqchi' tokens.")