from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def getNigeria():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=chrome_options)

    WEBSITE = "https://thenationonlineng.net/"
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='featured__breaking']//div[@class='featured__breaking__content']//a | //div[@class='featured__breaking']//div[@class='featured__breaking__more__news']//a")
    articles = []
    for element in elements:
        articles.append(element.get_attribute("href"))

    
    article_text = ""
    for article in articles:
        driver2 = webdriver.Chrome(options=chrome_options)
        driver2.get(article)
        paragraphs = driver2.find_elements(By.XPATH, "//div[@class='article__content']//p")
        for p in paragraphs:
            article_text += p.get_attribute("textContent")
    return article_text
