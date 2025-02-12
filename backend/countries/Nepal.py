from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://kathmandupost.com/"
def getNepal(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//article[@class='1']//h2//a | //article[contains(@class, 'article-image--left')]//h3//a")
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//section[@class='story-section']//p")
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text

