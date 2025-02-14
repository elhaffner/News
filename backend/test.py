from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
# chrome_options.add_argument('--ignore-ssl-errors=yes')
# chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

country = "Uganda"
WEBSITE = "https://www.monitor.co.ug/"
driver.get(WEBSITE)
#print(driver.page_source)
articlePath = "(//ol[@class='nested-cols'])[1]//li[contains(@class, 'headline-teasers_item')]//a"
elements = driver.find_elements(By.XPATH, articlePath)
print(len(elements))
articles = []
for element in elements:
    articles.append(element.get_attribute("href"))
    print(element.get_attribute("href"))

article_text = ""
for article in articles:
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(article)
    #print(driver.page_source)
    paragraphPath = "//div[@class='text-block blk-txt']//p"
    paragraphs = driver.find_elements(By.XPATH, paragraphPath)
    print(len(paragraphs))
    for p in paragraphs:
        try:
            article_text += p.get_attribute("textContent")
            print(p.get_attribute("textContent"))
        except:
            pass
print(
    '@app.route("/' + country + '")\n'
    "def " + country + "():\n"
    '\twebsite = "' + WEBSITE + '"\n'
    '\tarticlePath = "' + articlePath + '"\n'
    '\tparagraphPath = "' + paragraphPath + '"\n'
    "\treturn summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))"
)


# WEBSITE = "https://www.pyongyangtimes.com.kp/"
# driver.get(WEBSITE)
# elements = driver.find_elements(By.XPATH, "//div[@class='d-flex']//h3[@class='title']")
# article_text = ""
# for i in range(len(elements)):
#     driver.get(WEBSITE)
#     elements = driver.find_elements(By.XPATH, "//div[@class='d-flex']//h3[@class='title']")
#     ActionChains(driver).move_to_element(elements[i]).click().perform()
#     WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='content']//p")))
#     paragraphs = driver.find_elements(By.XPATH, "//div[@class='content']//p")
#     print(len(paragraphs))
#     for paragraph in paragraphs:
#         article_text += paragraph.get_attribute("textContent")
    
    