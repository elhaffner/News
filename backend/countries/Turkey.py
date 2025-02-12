from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.hurriyetdailynews.com/turkiye/"
def getTurkey(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='news']//a")

    title_links = {}
    for element in elements:
        title_links[element.get_attribute("href")] = element

    article_text = ""
    for articles in title_links.keys():
        driver.get(articles)
        paragraphs = driver.find_elements(By.XPATH, "//div[@class='content']//p")
        for paragraph in paragraphs:
            article_text += paragraph.get_attribute("textContent")
    
    return article_text
