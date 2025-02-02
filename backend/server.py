from flask import Flask
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from countries.Burundi import getBurundi
from countries.Algeria import getAlgeria


app = Flask(__name__)
API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)



def summarise(text):
    prompt='''
    Can you summarise the following news article in a small summary to depict what is happening currently in that country?
    Every new article will start with 'New article: '
    ''' + text
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

#Members API route
@app.route("/Burundi")
def Burundi():
    return summarise(getBurundi())

@app.route("/Algeria")
def Algeria():
    return summarise(getAlgeria(driver=driver))

if __name__ == "__main__":
    app.run(debug=True)
