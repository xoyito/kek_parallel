from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
from time import sleep

driver = webdriver.Chrome("chromedriver.exe")

urls = []

gn_chap = 1
while gn_chap <= 50:
    url = "https://www.bible.com/bible/545/GEN." + str(gn_chap)+ ".QQC"
    urls.append(url)
    gn_chap += 1

file_num = 1
for url in urls:
    driver.get(url)
    
    page = driver.find_element_by_css_selector(".reader")
    page = page.text

    sleep(5)

    with open("BIBLE//file_" + str(file_num) + ".txt", "w", encoding="utf8") as active:
        active.write(page)    

    file_num += 1


driver.close()
driver.quit()