import json

with open("Corpus\\eng.txt", "r", encoding="utf8") as eng_train:
    eng_lines = eng_train.readlines()
    eng_lines = [line.rstrip() for line in eng_lines]

with open("Corpus\\kek.txt", "r", encoding="utf8") as kek_train:
    kek_lines = kek_train.readlines()
    kek_lines = [line.rstrip() for line in kek_lines]

with open("Corpus\\kek_eng.json", "w", encoding="utf8") as corp_file:
    for i in range(len(kek_lines)):
        dictionary = {}
        dictionary["qeqchi"] = kek_lines[i]
        dictionary["english"] = eng_lines[i]        
        corp_file.write(json.dumps(dictionary) + "\n")