from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
website = 'https://www.elkhabar.com/press/category/223/'

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

git_credential ="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"

driver.get(website)
elements = driver.find_elements(By.CLASS_NAME, "title-link")
title_links = {}
for element in elements:
    title_links[element.get_attribute("href")] = element

#print(title_links)
article_text = []
for articles in title_links.keys():
    driver.get(articles)
    article_text.append(driver.find_element(By.XPATH, '//div[@id="article_body_content"]').get_attribute("textContent"))



