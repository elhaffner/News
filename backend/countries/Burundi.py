from bs4 import BeautifulSoup
import requests
import google.generativeai as genai


def getBurundi():
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

    return text

