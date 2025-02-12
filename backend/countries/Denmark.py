from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.thelocal.dk/tag/politics"
def getDenmark(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//article[contains(@class, 'article-card')]//a")
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//div[@id='articleBody']//p")
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text
