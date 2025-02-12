from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.okaz.com.sa/"
def getSaudiArabia(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='slide']//a")
    articles = []
    for element in elements:
        link = element.get_attribute("href")
        if "video" not in link:
            articles.append(link)

    article_text = ""
    for article in articles:
        driver.get(article)
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='bodyText']")

        for paragraph in paragraphs:
            article_text += paragraph.get_attribute("textContent")
    return article_text
