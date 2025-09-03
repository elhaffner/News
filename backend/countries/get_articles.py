from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import google.generativeai as genai


class GetArticles:
    def __init__(self):
        self.API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
        genai.configure(api_key=self.API_KEY)
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction=[
                """
                You are an article detection tool. Your job is to identify which links, from a given list of links, 
                link directly to news articles. Once you have identified the links that link to news articles, print them
                to the screen. The links might not all be in english, so you must be able to identify links in other languages as well. 
                Only print the links themselves and nothing else, with each link separated by a newline. Also, don't
                print duplicates."
                """
            ],
        )
    
    def get_article_list(self, driver, link):
        driver.get(link)
        body_html = driver.find_element("tag name", "body").get_attribute("innerHTML")
        links = driver.find_elements("tag name", "a")

        prompt_text = ""
        for link in links:
            linkText = link.get_attribute("href")
            if linkText is not None:
                prompt_text += linkText
                prompt_text += "\n"

        article_links = self.model.generate_content(prompt_text).text.strip()
        return  article_links.splitlines()

    def getAPI_key(self):
        return self.API_KEY
