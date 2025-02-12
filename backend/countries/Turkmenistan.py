from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://turkmenportal.com/"
def getTurkmenistan(driver):
    driver.get(WEBSITE)
    elementsMain = driver.find_elements(By.XPATH, "//div[@class='main_news_block']//a[@class='thumb']")
    elementsTwo = driver.find_elements(By.XPATH, "//div[@class='list-item inline-block type-post ']//a[@class='thumb']")
    articles = []
    articles.append(elementsMain[0].get_attribute("href"))
    for i in range(6):
        articles.append(elementsTwo[i].get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='article_text']//p")

        for paragraph in paragraphs:
            article_text += paragraph.get_attribute("textContent")
    return article_text
