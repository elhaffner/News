from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
import google.generativeai as genai
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from countries.generalCountry import getGeneralCountry

from countries.Algeria import getAlgeria
from countries.Bolivia import getBolivia
from countries.Burundi import getBurundi
from countries.Denmark import getDenmark
from countries.Mali import getMali
from countries.Mongolia import getMongolia
from countries.Nigeria import getNigeria
from countries.Nepal import getNepal
from countries.Saudi_Arabia import getSaudiArabia
from countries.Turkey import getTurkey
from countries.Turkmenistan import getTurkmenistan

app = Flask(__name__)


API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

information = {}
#Chron Job
def run_all_countries(driver, information):
    information['Algeria'] = getAlgeria(driver=driver)
    information['Mongolia'] = getMongolia(driver=driver)


sched = BackgroundScheduler(daemon=True)
sched.add_job(func=run_all_countries, args=[driver, information], trigger='interval',hours=1)
sched.start()


def summarise(text):
    prompt='''
    Can you summarise the following news article in a small summary to depict what is happening currently in that country?
    ''' + text
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

#Members API route
@app.route("/Algeria")
def Algeria():
    return summarise(getAlgeria(driver=driver))

@app.route("Andorra")
def Andorra():
    website = "https://www.diariandorra.ad/"
    articlePath = "//div[@id='m47873-47872-47874']//article[contains(@class, 'c-article')]//h2[@class='c-article__title']//a"
    paragraphPath = "//div[contains(@class, 'c-detail-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Bolivia")
def Bolivia():
    return summarise(getBolivia(driver=driver))

@app.route("/Botswana")
def Botswana():
    return summarise(getGeneralCountry(driver=driver, website='https://guardiansun.co.bw/', articlePath="//article[@class='article-main']//h6//a | //div[@class='article']//h2//a", paragraphPath="//div[@class='single-content']"))

@app.route("/Burundi")
def Burundi():
    return summarise(getBurundi(driver=driver))

@app.route("/Canada")
def Canada():
    website = "https://nationalpost.com/"
    articlePath = "//div[contains(@class, 'hero-feed__hero-col')]//a[@class='article-card__link']"
    paragraphPath = "//article[contains(@class, 'article-content-story')]//section[contains(@class, 'article-content__content-group')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

# @app.route("/Dem. Rep. Korea")
# def NKorea():
#     return summarise(getNKorea(driver))

@app.route("/Denmark")
def Denmark():
    return summarise(getDenmark(driver=driver))

@app.route("/Egypt")
def Egypt():
    website = "https://www.egypttoday.com/"
    articlePath = "//div[contains(@class, 'swiper-container')]//a | //div[@class='top-news-item']/a"
    paragraphPath = "//div[@class='ArticleDescription']//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Eritrea")
def Eritrea():
    website = "https://shabait.com/"
    articlePath = "(//div[@class='bs-vc-wrapper'])[1]//div[@class='item-content']/a"
    paragraphPath = "//div[contains(@class, 'single-post-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Estonia")
def Estonia():
    website = "https://estonianworld.com/"
    articlePath = "(//div[@class='jeg_posts_wrap'])[1]//article//h3//a"
    paragraphPath = "//div[contains(@class, 'entry-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Fiji")
def Fiji():
    website = "https://www.fijitimes.com.fj/"
    articlePath = "//div[contains(@id, 'trending-posts-block')]//article//a"
    paragraphPath = "//div[contains(@class, 'entry-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Finland")
def Finland():
    website = "https://www.dailyfinland.fi/"
    articlePath = "//div[@class='Homepage-Top']//div[contains(@class, 'col')]//div[(@class='sub_lead_more' or @class='sub_lead' or @class='lead_headline p-2')]//a"
    paragraphPath = "//div[contains(@class, 'dtl_news')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Germany")
def Germany():
    website = "https://www.dw.com/en/germany/s-1432"
    articlePath = "//div[@class='news s4zlaoh']//a"
    paragraphPath = "//div[contains(@class, 'content-area')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Ireland")
def Ireland():
    website = "https://www.irishtimes.com/politics/"
    articlePath = "(//div[@class='b-flex-chain'])[1]//article//h3//a"
    paragraphPath = "//article//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Mali")
def Mali():
    return summarise(getMali(driver=driver))

@app.route("/Mongolia")
def Mongolia():
    return summarise(getMongolia(driver=driver))

@app.route("/Morocco")
def Morocco():
    website = "https://lematin.ma/"
    articlePath = "//div[contains(@class, 'main-article')]//a[@class='article-title'] | //div[contains(@class, 'article-left')]//a[@class='article-title'] | //div[contains(@class, 'article-right')]//a[@class='article-title']"
    paragraphPath = "//div[contains(@class, 'article-desc')]"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Nigeria")
def Nigeria():
    return summarise(getNigeria())

@app.route("/Nepal")
def Nepal():
    return summarise(getNepal(driver=driver))

@app.route("/Paraguay")
def Paraguay():
    website = "https://www.ultimahora.com/"
    articlePath = "//div[@class='PageListStandardH'][1]//div[contains(@class, 'PagePromo-title')]//a"
    paragraphPath = "//div[contains(@class, 'Page-articleBody')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Poland")
def Poland():
    website = "https://polanddaily24.com/"
    articlePath = "//h2[contains(@class, 'td-module-title')]//a | //div[@id='tdi_33']//h3[contains(@class, td-module-title)]//a"
    paragraphPath = "//div[contains(@class, 'td-post-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Saudi Arabia")
def Saudi_Arabia():
    return summarise(getSaudiArabia(driver=driver))

@app.route("/Sri Lanka")
def Sri_Lanka():
    website = "https://lankanewsweb.net/archives/category/news/"
    articlePath = "//div[@id='tdi_89']//div[contains(@class, 'td-cpt-post')]//p//a"
    paragraphPath = "//div[contains(@class, 'tdb-block-inner')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Tunisia")
def Tunisia():
    website = "https://lapresse.tn/"
    articlePath = "//div[contains(@class, 'bdaia-block6')]/div[@class='bdaia-blocks-container']/div[contains(@class, 'block-article')]//h2//a"
    paragraphPath = "//div[@class='bdaia-post-content']//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Turkey")
def Turkey():
    return summarise(getTurkey(driver=driver))

@app.route("/Turkmenistan")
def Turkmenistan():
    return summarise(getTurkmenistan(driver=driver))

@app.route("/Ukraine")
def Ukraine():
    website = "https://www.kyivpost.com/"
    articlePath = "//div[@class='important-news-block']//div[contains(@class, 'small-thumb-xs')]//div[@class='title']//a | //div[@class='important-news-block']//div[contains(@class, 'general-post')]//div[@class='title']//a"
    paragraphPath = "//div[contains(@id, 'post-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

if __name__ == "__main__":
    app.run(debug=False)
