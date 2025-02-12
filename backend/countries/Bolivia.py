from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://eldeber.com.bo/"

def getBolivia(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='node__content h-100']//a[@class='position-absolute w-100 h-100']")
    articles = []
    for i in range(5):
        articles.append(elements[i].get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='field field--name-body field--type-text-with-summary field--label-hidden field__item']//p")
        for paragraph in paragraphs:
            article_text += paragraph.get_attribute("textContent")
    return article_text
