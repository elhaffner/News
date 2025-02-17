from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


WEBSITE = "https://www.newtimes.co.rw/"
def getRwanda(driver):
    driver.get(WEBSITE)
    ActionChains(driver).scroll_by_amount(0, 200).perform()
    articlePath = "//main[contains(@class, 'home-page')]//div[contains(@class, 'nt-several-articles')]//div[@class='article-title']//a"
    elements = driver.find_elements(By.XPATH, articlePath)
    articlePath2 = "//main[contains(@class, 'home-page')]//div[contains(@class, 'first-article-details')]//div[@class='article-title']//a"
    elements.extend(driver.find_elements(By.XPATH, articlePath2))
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    article_text = ""
    for article in articles:
        driver.get(article)
        ActionChains(driver).scroll_by_amount(0, 200).perform()
        paragraphPath = "//div[@class='article-body']/p"
        paragraphs = driver.find_elements(By.XPATH, paragraphPath)
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text
