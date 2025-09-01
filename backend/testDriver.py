from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import google.generativeai as genai
from bs4 import BeautifulSoup
import re

API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=[
        """
        You are an expert article extractor. Given the html body for a website that contains a news article, I want you
        to extract the text content of the main article on that site.  
        """
    ],
)

def summarise(text):
    return model.generate_content(text).text.strip()

def remove_tags(html):
    soup = BeautifulSoup(html, "html.parser")

    #Remove style components

    style_all = soup.find_all('style')
    [style.decompose() for style in style_all]

    script_all = soup.find_all('script')
    [script.decompose() for script in script_all]

    svg_all = soup.find_all('svg')
    [svg.decompose() for svg in svg_all]

    li_all = soup.find_all('li')
    [li.decompose() for li in li_all]

    img_all = soup.find_all('img')
    [img.decompose() for img in img_all]

    for tag in soup.find_all(True): 
        tag.unwrap()

    #for div in soup.find_all("div"):
    #    div.unwrap()
    
    sp = str(soup)
    return "\n".join([s for s in sp.split("\n") if s])
    



chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.nbcnews.com/news/us-news/bullet-fragment-found-neck-10-year-old-weston-halsne-rcna228280")
body_html = driver.find_element("tag name", "body").get_attribute("innerHTML")


# articles = driver.find_elements("tag name", "article")
# txt = articles[0].get_attribute("innerHTML")
# print(len(txt))
print(len(body_html))
res = remove_tags(body_html)
print(len(res))

