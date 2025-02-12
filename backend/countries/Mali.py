from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.journaldumali.com/"
def getMali(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='news-outer-wrapper']//p[@class='external-link']//a | //div[@class='article']//h1//a")
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='article-content']//p | //div[@class='article-content']//div")
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text

