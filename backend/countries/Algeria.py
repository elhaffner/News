from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

WEBSITE = "https://www.elkhabar.com/press/category/223/"
def getAlgeria(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.CLASS_NAME, "title-link")
    title_links = {}
    for element in elements:
        title_links[element.get_attribute("href")] = element

    article_text = ""
    for articles in title_links.keys():
        driver.get(articles)
        article_text += driver.find_element(By.XPATH, '//div[@id="article_body_content"]').get_attribute("textContent")
    
    return article_text


