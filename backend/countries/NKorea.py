from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


WEBSITE = "https://www.pyongyangtimes.com.kp/"
def getNkorea(driver):
    driver.get(WEBSITE)
    elements = driver.find_elements(By.XPATH, "//div[@class='d-flex']//h3[@class='title']")
    for element in elements:
        print(element.get_attribute("textContent"))
    