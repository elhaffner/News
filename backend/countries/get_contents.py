from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import google.generativeai as genai
from bs4 import BeautifulSoup


class GetArticles:

    def __init__(self):
        self.API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
        genai.configure(api_key=self.API_KEY)
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction=[
                """
                You are an expert article extractor. Given the html body for a website that contains a news article, I want you
                to extract the text content of the main article on that site. These might not necessarily be in English, so you
                will have to be able to detect articles in multiple languages.  
                """
            ],
        )
    

    def remove_tags(html):
        soup = BeautifulSoup(html, "html.parser")

        for tag in soup.find_all(True): 
            tag.unwrap()
        
        sp = str(soup)
        return "\n".join([s for s in sp.split("\n") if s])
    
    def get_article_contents(self, driver, link):
        driver.get(link)
        body_html = driver.find_element("tag name", "body").get_attribute("innerHTML")
        text_content = self.remove_tags(body_html)
        article_contents = self.model.generate_content(text_content).text.strip()
        return article_contents

    def getAPI_key(self):
        return self.API_KEY
