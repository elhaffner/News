from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.iwacu-burundi.org/"
def getBurundi(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@id='homeslide']//div[@class='titraille']//h2//a")
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//article//p")
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text

