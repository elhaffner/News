from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def getGeneralCountry(driver, website, articlePath, paragraphPath):
    driver.get(website)
    elements = driver.find_elements(By.XPATH, articlePath)
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, paragraphPath)
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text



