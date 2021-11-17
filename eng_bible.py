from selenium import webdriver
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")

urls = []

abreviations = ["GEN", "EXO", "LEV", "NUM", "DEU", "JOS", "JDG", "RUT", "1SA", "2SA", "1KI", "2KI", "1CH", "2CH", "EZR", "NEH", "EST", "JOB", "PSA", "PRO", "ECC", "SNG", "ISA", "JER", "LAM", "EZK", "DAN", "HOS", "JOL", "AMO", "OBA", "JON", "MIC", "NAM", "HAB", "ZEP", "HAG", "ZEC", "MAL", "MAT", "MRK", "LUK", "JHN", "ACT", "ROM", "1CO", "2CO", "GAL", "EPH", "PHP", "KOL", "1TH", "2TH", "1TI", "2TI", "TIT", "PHM", "HEB", "JAS", "1PE", "2PE", "1JN", "2JN", "3JN", "JUD", "REV"]
num_chapters = [50, 40, 27, 36, 34, 24, 21, 4, 31, 24, 22, 25, 29, 36, 10, 13, 10, 42, 150, 31, 12, 8, 66, 52, 5, 48, 12, 14, 3, 9, 1, 4, 7, 3, 3, 3, 2, 14, 4, 28, 16, 24, 21, 28, 16, 16, 13, 6, 6, 4, 4, 5, 3, 6, 4, 3, 1, 13, 5, 5, 3, 5, 1, 1, 1, 22]

for i, book in enumerate(abreviations):
    for chapter in range(num_chapters[i]):
        url = "https://www.bible.com/bible/111/" + book + "." + str(chapter + 1) + ".NIV"
        urls.append(url)

for i, url in enumerate(urls):
    driver.get(url)
    
    page = driver.find_element_by_css_selector(".reader")
    page = page.text

    sleep(5)

    with open("ENG_BIBLE//file_" + str(i+1) + ".txt", "w", encoding="utf8") as active:
        active.write(page)


driver.close()
driver.quit()