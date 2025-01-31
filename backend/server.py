from flask import Flask
import google.generativeai as genai
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)
API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"



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
    api_key = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'
    }
    url = "https://www.iwacu-burundi.org/englishnews/"
    result = requests.get(url, headers=headers)
    doc = BeautifulSoup(result.text, "html.parser")
    title_link = {}
    for element in doc.find_all(class_="title_loop_home"):
        title = element.find("a")['title']
        href = element.find("a")['href']
        article = ""
        for paragraph in BeautifulSoup(requests.get(href, headers=headers).text, "html.parser").find(class_="article").find_all("p"):
            article += paragraph.get_text()
        
        title_link[title] = article

    text = ""
    for title in title_link.keys():
        text += "New article: " + title_link[title]

    return summarise(text)

if __name__ == "__main__":
    app.run(debug=True)
