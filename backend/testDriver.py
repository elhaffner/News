from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import google.generativeai as genai

API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    system_instruction=[
        """
        You are an article detection tool. Your job is to identify which links, from a given list of links, 
        link directly to news articles. Once you have identified the links that link to news articles, print them
        to the screen. Only print the links themselves and nothing else, with each link separated by a newline. Also, don't
        print duplicates."
        """
    ],
)

def summarise(text):
    response = model.generate_content(text)
    return response.text

chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.samoaobserver.ws/")
body_html = driver.find_element("tag name", "body").get_attribute("innerHTML")
links = driver.find_elements("tag name", "a")

prompt_text = ""
for link in links:
    html = link.get_attribute("href")
    if html is not None:
        prompt_text += html
        prompt_text += "\n"
print(summarise(prompt_text))

