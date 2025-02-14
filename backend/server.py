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
from countries.Ghana import getGhana
from countries.Mali import getMali
from countries.Mongolia import getMongolia
from countries.Nigeria import getNigeria
from countries.Nepal import getNepal
from countries.Saudi_Arabia import getSaudiArabia
from countries.Turkey import getTurkey
from countries.Turkmenistan import getTurkmenistan
from countries.Uganda import getUganda

app = Flask(__name__)


API_KEY = "AIzaSyAZ_y74Vwb453PU4VKuooxpwlhbB0uEL7o"
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)

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

@app.route("/American Samoa")
def American_Samoa():
    website="https://www.samoaobserver.ws/"
    articlePath = "//div[@class='row flex flex-col-reverse md:flex-row']//a[@class='block flex-grow flex flex-col no-underline mb-6']"
    paragraphPath = "//div[contains(@class, 'article__content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Andorra")
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

@app.route("/Brunei")
def Brunei():
        website = "https://borneobulletin.com.bn/"
        articlePath = "(//div[contains(@class, 'vc_column-inner')]//h3//a)[position() <= 6]"
        paragraphPath = "//div[contains(@class, 'tdb_single_content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Burundi")
def Burundi():
    return summarise(getBurundi(driver=driver))

@app.route("/Canada")
def Canada():
    website = "https://nationalpost.com/"
    articlePath = "//div[contains(@class, 'hero-feed__hero-col')]//a[@class='article-card__link']"
    paragraphPath = "//article[contains(@class, 'article-content-story')]//section[contains(@class, 'article-content__content-group')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Cape Verde")
def Cape_Verde():
    website = "https://expressodasilhas.cv/"
    articlePath = "//div[@id='home1']//div[@class='content']/a"
    paragraphPath = "//div[contains(@class, 'articleText')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Costa Rica")
def Costa_Rica():
        website = "https://www.diarioextra.com/"
        articlePath = "(//div[contains(@class, 'splash-featured__container')])[1]//div[contains(@class, 'swiper-slide')]/a"
        paragraphPath = "//div[contains(@class, 'single-layout__article')]/p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

# @app.route("/Dem. Rep. Korea")
# def NKorea():
#     return summarise(getNKorea(driver))

@app.route("/Denmark")
def Denmark():
    return summarise(getDenmark(driver=driver))

@app.route("/Djibouti")
def Djibouti():
    website = "https://www.lanation.dj/"
    articlePath = "(//div[@class='wpb_wrapper'])[1]//div[@class='td-module-thumb']//a"
    paragraphPath = "//div[contains(@class, 'td-post-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))


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

@app.route("/Gabon")
def Gabon():
    website = "https://www.gabonews.com/"
    articlePath = "(//div[contains(@class, 'layout_3')])[1]//h4//a | (//div[contains(@class, 'layout_2')])[1]//h4//a"
    paragraphPath = "//div[contains(@class, 'blog-excerpt')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Germany")
def Germany():
    website = "https://www.dw.com/en/germany/s-1432"
    articlePath = "//div[@class='news s4zlaoh']//a"
    paragraphPath = "//div[contains(@class, 'content-area')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Ghana")
def Ghana():
    return summarise(getGhana())

@app.route("/Ireland")
def Ireland():
    website = "https://www.irishtimes.com/politics/"
    articlePath = "(//div[@class='b-flex-chain'])[1]//article//h3//a"
    paragraphPath = "//article//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Israel")
def Israel():
    website = "https://www.israelnationalnews.com/"
    articlePath = "//div[@class='home']/a | (//div[@class='home-top-article']/article/a)[1]"
    paragraphPath = "//div[contains(@class, 'article-content-inside')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Libya")
def Libya():
    website = "https://libyaobserver.ly/"
    articlePath = "(//div[@class='pbs-content'])[1]//article//h4//a"
    paragraphPath = "//div[contains(@class, 'node__content')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Mali")
def Mali():
    return summarise(getMali(driver=driver))

@app.route("/Marshall Islands")
def Marshall_Islands():
    website = "https://marshallislandsjournal.com/"
    articlePath = "//article[contains(@class, 'cycle-slide')]/a"
    paragraphPath = "//div[contains(@class, 'entry-content')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Mongolia")
def Mongolia():
    return summarise(getMongolia(driver=driver))

@app.route("/Morocco")
def Morocco():
    website = "https://lematin.ma/"
    articlePath = "//div[contains(@class, 'main-article')]//a[@class='article-title'] | //div[contains(@class, 'article-left')]//a[@class='article-title'] | //div[contains(@class, 'article-right')]//a[@class='article-title']"
    paragraphPath = "//div[contains(@class, 'article-desc')]"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

app.route("/Mozambique")
def Mozambique():
    website = "https://www.jornalnoticias.co.mz/"
    articlePath = "(//div[@class='penci-wrapper-smalllist'])[1]//div[@class='pcsl-title']//a | //div[@class='tabs-content']//div[contains(@class, 'tab-recent')]//h4//a"
    paragraphPath = "//div[contains(@class, 'entry-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Nigeria")
def Nigeria():
    return summarise(getNigeria())

@app.route("/Nepal")
def Nepal():
    return summarise(getNepal(driver=driver))

@app.route("/Palestine")
def Palestine():
    website = "https://english.pnn.ps/"
    articlePath = "//div[@class='col-lg-9']//h3//a | //div[@class='col-lg-9']//h1//a"
    paragraphPath = "//div[contains(@class, 'news-content')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Paraguay")
def Paraguay():
    website = "https://www.ultimahora.com/"
    articlePath = "//div[@class='PageListStandardH'][1]//div[contains(@class, 'PagePromo-title')]//a"
    paragraphPath = "//div[contains(@class, 'Page-articleBody')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Peru")
def Peru():
    website = "https://elperuano.pe/"
    articlePath = "//div[@id='noticiaDestacadas']//article//span[@class='card-title2']//a"
    paragraphPath = "//div[contains(@class, 'contenido')]//div"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Poland")
def Poland():
    website = "https://polanddaily24.com/"
    articlePath = "//h2[contains(@class, 'td-module-title')]//a | //div[@id='tdi_33']//h3[contains(@class, td-module-title)]//a"
    paragraphPath = "//div[contains(@class, 'td-post-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Qatar")
def Qatar():
    website = "https://thepeninsulaqatar.com/"
    articlePath = "//div[contains(@class, 'col-sm-3 item')]//div[@class='content']//a[contains(@class, 'title')] | //div[contains(@class, 'col-sm-3 item')]//div[@class='townews']//a[contains(@class, 'title')] | //div[contains(@class, 'col-sm-6 item')]/a[contains(@class, 'title')]"
    paragraphPath = "//div[@class='con-text']//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Republic of Korea")
def Republic_Of_Korea():
    website = "https://www.koreaherald.com/"
    articlePath = "//article[@class='headline']//a[@class='txt_area']"
    paragraphPath = "//article[contains(@class, 'news_content')]//p"
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

@app.route("/Saint Kitts and Nevis")
def St_Kitts_And_Nevis():
    website = "https://zizonline.com"
    articlePath = "(//div[@class='bs-vc-wrapper'])[2]//article//h2//a"
    paragraphPath = "//div[contains(@class, 'continue-reading-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Slovakia")
def Slovakia():
        website = "https://spectator.sme.sk/politics-and-society/today-in-slovakia"
        articlePath = "(//div[contains(@class, 'article-tile--hero')])[1]//h2//a"
        paragraphPath = "//div[contains(@class, 'article-body')]/p"
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

@app.route("/Uganda")
def Uganda():
    return summarise(getUganda())

@app.route("/Venezuela")
def Venezuela():
    website = "https://www.elnacional.com/venezuela/?utm_source=menu&utm_medium=recirculation&utm_campaign=internal_links"
    articlePath = "//div[@class='list-articles']//div[@class='title']//a"
    paragraphPath = "//article//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

if __name__ == "__main__":
    app.run(debug=False)
