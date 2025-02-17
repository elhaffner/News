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
from countries.Rwanda import getRwanda
from countries.Saudi_Arabia import getSaudiArabia
from countries.Turkey import getTurkey
from countries.Turkmenistan import getTurkmenistan
from countries.Uganda import getUganda
from countries.Zimbabwe import getZimbabwe

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

@app.route("/Angola")
def Angola():
        website = "https://novojornal.co.ao/"
        articlePath = "//div[contains(@class, 'column-n2')]//div[@class='articles-panel']//div[@class='title']//a"
        paragraphPath = "//div[contains(@class, 'article-body')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Belize")
def Belize():
        website = "https://amandala.com.bz/news/"
        articlePath = "(//div[contains(@class, 'vc_row tdi_75  wpb_row td-pb-row tdc-element-style')])[1]//h3//a"
        paragraphPath = "//div[contains(@class, 'tdb-block-inner')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Benin")
def Benin():
        website = "https://lanation.bj/actualites"
        articlePath = "//div[@id='contenu']/div/a"
        paragraphPath = "//div[contains(@class, 'content-para')]"
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

@app.route("/Burkina Faso")
def Burkina_Faso():
        website = "https://www.lobservateur.bf/"
        articlePath = "//div[@class='nspArtScroll1']//div[@class='nspArtPage nspCol10']//h4//a"
        paragraphPath = "//div[@class='itemFullText']//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Burundi")
def Burundi():
    return summarise(getBurundi(driver=driver))

@app.route("/Cameroon")
def Cameroon():
        website = "https://actucameroun.com/"
        articlePath = "//div[contains(@class, 'ac-most-popular')]//div[@class='ac-most-popular-content']/a"
        paragraphPath = "//div[contains(@class, 'post-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

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

@app.route("/Central African Republic")
def Central_African_Republic():
        website = "https://www.radiondekeluka.org/"
        articlePath = "//div[contains(@class, 'featuredArticles')]//div[@class='slick-slide']//a[@class='ModulePost-title']"
        paragraphPath = "//div[contains(@class, 'articleText')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Chad")
def Chad():
        website = "https://www.alwihdainfo.com/"
        articlePath = "//div[@class='eau']//td//h3[@class='titre']//a"
        paragraphPath = "//div[contains(@class, 'texte')]"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Comoros")
def Comoros():
        website = "https://www.comoresinfos.net/"
        articlePath = "//div[@id='mh_magazine_posts_stacked-6']//article//h3//a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Costa Rica")
def Costa_Rica():
        website = "https://www.diarioextra.com/"
        articlePath = "(//div[contains(@class, 'splash-featured__container')])[1]//div[contains(@class, 'swiper-slide')]/a"
        paragraphPath = "//div[contains(@class, 'single-layout__article')]/p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Côte d'Ivoire")
def Côte_dIvoire():
        website = "https://www.abidjan.net/"
        articlePath = "//div[@class='grid3-3-2-1']//div[@class='card-article-body']//a[@class='card-article-title']"
        paragraphPath = "//div[contains(@class, 'article-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Democratic Republic of the Congo")
def Democratic_Republic_Of_The_Congo():
        website = "https://actualite.cd"
        articlePath = "//div[@id='flexslider-2']/ul/li//h2//a | //div[@id='block-views-block-accueil-la-une-2023-block-3']//h4//a | //div[@id='block-views-block-accueil-la-une-2023-block-2']//h4//a"
        paragraphPath = "//div[@class='field-content']//p"
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

@app.route("/Equatorial Guinea")
def Equatorial_Guinea():
        website = "https://diariorombe.es/"
        articlePath = "(//div[contains(@class, 'anwp-pg-classic-grid anwp-pg-posts-wrapper')]//div[contains(@class, 'anwp-pg-post-teaser__content')]//a)[position() <= 3]"
        paragraphPath = "//div[@data-widget_type='theme-post-content.default']//p"
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

@app.route("/Eswatini")
def Eswatini():
        website = "https://swazidailynews.com/"
        articlePath = "//div[contains(@class, 'owl-stage-outer')]//div[@class='owl-item']/div/div/a | //div[contains(@class, 'owl-stage-outer')]//div[contains(@class, 'owl-item active')]/div/div/a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Ethiopia")
def Ethiopia():
        website = "https://www.thereporterethiopia.com/"
        articlePath = "(//div[@class='td-module-meta-info']//h3//a)[position() <= 4]"
        paragraphPath = "//div[contains(@class, 'tdb-block-inner')]//p"
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

@app.route("/Gambia")
def Gambia():
        website = "https://thepoint.gm/"
        articlePath = "//div[@class='headlines']//div[contains(@class, 'headline-item')]/a"
        paragraphPath = "//div[@class='container']//div[contains(@class, 'justify-content-center')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Georgia")
def Georgia():
        website = "https://georgiatoday.ge/"
        articlePath = "(//h3[contains(@class, 'jeg_post_title')]//a)[position() <= 3]"
        paragraphPath = "//div[contains(@class, 'content-inner')]//p"
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

@app.route("/Guinea")
def Guinea():
        website = "https://guineenews.org/"
        articlePath = "(//div[contains(@class, 'listing-grid-1')])[2]/article[contains(@class, 'main-term-7002')]//h2//a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Guinea-Bissau")
def Guinea_Bissau():
        website = "https://www.odemocratagb.com/"
        articlePath = "//div[@class='elegantwp-posts-container']//h3//a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Honduras")
def Honduras():
        website = "https://www.laprensa.hn/honduras"
        articlePath = "//div[@id='nota-b']//div[@class='card-title title']//a | (//section[@class='noticias'])[1]//div[@class='card-title title']//a"
        paragraphPath = "//div[contains(@class, 'text')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

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

@app.route("/Kenya")
def Kenya():
        website = "https://www.standardmedia.co.ke"
        articlePath = "//div[@class='col-12 col-md-9']//div[@class='col-12 col-md-8']/a | //div[@class='col-12 col-md-9']//div[@class='col-12 col-md-8']/div[@class='row']//div[contains(@class, 'sub-title')]/a | //div[@class='col-12 col-md-9']//div[@class='col-12 col-md-4 boda-left']//div[contains(@class, 'sub-title')]/a"
        paragraphPath = "//div[@class='col-12 col-md-8']//div[contains(@class, 'content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Latvia")
def Latvia():
        website = "https://www.diena.lv/"
        articlePath = "//section[contains(@class, 'articleblock__2-3')]//h4//a"
        paragraphPath = "//section[contains(@class, 'article__body')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Lesotho")
def Lesotho():
        website = "https://informativenews.co.ls/?234d12_page=1"
        articlePath = "//ul[contains(@class, 'wp-block-latest-posts__list')]//li//a"
        paragraphPath = "//article//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Liberia")
def Liberia():
        website = "https://www.liberianobserver.com/"
        articlePath = "(//div[contains(@class, 'main-content')])[1]//article//h3//a | (//div[contains(@class, 'main-content')])[1]//article//h2//a"
        paragraphPath = "//div[@id='article-body']//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Libya")
def Libya():
    website = "https://libyaobserver.ly/"
    articlePath = "(//div[@class='pbs-content'])[1]//article//h4//a"
    paragraphPath = "//div[contains(@class, 'node__content')]/p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Madagascar")
def Madagascar():
        website = "https://www.lexpress.mg/"
        articlePath = "//div[contains(@class, 'featured-items')]//a[@class='entry-inner']"
        paragraphPath = "//div[contains(@class, 'post-body')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Malawi")
def Malawi():
        website = "https://mwnation.com/"
        articlePath = "(//div[@class='slick-track']//div[contains(@class, 'slick-current')])[1]/div/a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
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

@app.route("/Mauritania")
def Mauritania():
        website = "https://www.lecalame.info/"
        articlePath = "//div[contains(@class, 'view-top-news')]//div[contains(@class, 'views-field-title')]//a"
        paragraphPath = "//div[contains(@class, 'field-items')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Mauritius")
def Mauritius():
        website = "https://www.lemauricien.com/"
        articlePath = "(//div[@class='td-module-meta-info']//h3//a)[position() <= 2]"
        paragraphPath = "//div[contains(@class, 'tdb-block-inner')]//p"
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

@app.route("/Namibia")
def Namibia():
        website = "https://neweralive.na/"
        articlePath = "//div[contains(@class, 'entry-summary')]//div[contains(@class, 'cmsmasters_3')]//article//header[@class='headline_text']//a"
        paragraphPath = "//div[contains(@class, 'cmsmasters_post_content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Niger")
def Niger():
        website = "https://www.actuniger.com/"
        articlePath = "//div[@id='Mod111']//div[@class='news-item']//a[@class='intro_title'] | //div[@id='Mod111']//div[@class='news-item']//a[@class='lead_title'] "
        paragraphPath = "//section[@itemprop='articleBody']//p"
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

@app.route("/Republic of the Congo")
def Republic_Of_The_Congo():
        website = "https://lesechos-congobrazza.com/"
        articlePath = "//div[@class='sp-slides-container']//div[@class='sp-slide']//h3//a"
        paragraphPath = "//section[contains(@class, 'article-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Rwanda")
def Rwanda():
     return summarise(getRwanda(driver=driver))

@app.route("/São Tomé and Principe")
def São_Tomé_And_Principe():
        website = "https://www.jornaltropical.st/"
        articlePath = "(//div[@id='mvp_catrow_widget-4'])[1]//ul/li/a"
        paragraphPath = "//div[contains(@id, 'content-main')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Saudi Arabia")
def Saudi_Arabia():
    return summarise(getSaudiArabia(driver=driver))

@app.route("/Saint Kitts and Nevis")
def St_Kitts_And_Nevis():
    website = "https://zizonline.com"
    articlePath = "(//div[@class='bs-vc-wrapper'])[2]//article//h2//a"
    paragraphPath = "//div[contains(@class, 'continue-reading-content')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Senegal")
def Senegal():
        website = "https://lequotidien.sn/"
        articlePath = "//div[contains(@class, 'large-post')]//h2//a | //section[@id='latest-posts']//article//h2//a"
        paragraphPath = "//div[contains(@class, 'post-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Seychelles")
def Seychelles():
        website = "https://www.nation.sc/"
        articlePath = "//div[@class='topnews']//h1//a | (//div[contains(@class, 'article_list')])[1]//article//h1//a"
        paragraphPath = "//article//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Sierra Leone")
def Sierra_Leone():
        website = "https://www.thesierraleonetelegraph.com/"
        articlePath = "//div[@class='mh-posts-large-widget']//article//h3//a"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Slovakia")
def Slovakia():
        website = "https://spectator.sme.sk/politics-and-society/today-in-slovakia"
        articlePath = "(//div[contains(@class, 'article-tile--hero')])[1]//h2//a"
        paragraphPath = "//div[contains(@class, 'article-body')]/p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Somalia")
def Somalia():
        website = "https://www.garoweonline.com/en"
        articlePath = "(//div[@class='single-top-news']//div[@class='garowe-news-content']//a)[position() <= 5]"
        paragraphPath = "//div[@class='article-content']//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/South Africa")
def South_Africa():
        website = "https://www.iol.co.za/"
        articlePath = "//div[@class='sc-kkGfuU crpFrt']/div[contains(@class, 'divider-right')]/article/a"
        paragraphPath = "//div[contains(@class, 'article-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Sri Lanka")
def Sri_Lanka():
    website = "https://lankanewsweb.net/archives/category/news/"
    articlePath = "//div[@id='tdi_89']//div[contains(@class, 'td-cpt-post')]//p//a"
    paragraphPath = "//div[contains(@class, 'tdb-block-inner')]//p"
    return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Sudan")
def Sudan():
        website = "https://www.sudanakhbar.com/"
        articlePath = "(//div[@class='main-box-inside']//article//h2//a)[position() <= 20]"
        paragraphPath = "//div[contains(@class, 'entry-content')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))


@app.route("/Tanzania")
def Tanzania():
        website = "https://www.thecitizen.co.tz/"
        articlePath = "//section[@class='headline-teasers']//li[contains(@class, 'headline-teasers_item')]/a"
        paragraphPath = "//div[contains(@class, 'text-block blk-txt')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Togo")
def Togo():
        website = "https://www.togofirst.com/en"
        articlePath = "//div[@class='sppb-column-addons']//div[@id='sppb-addon-1514541741787']//div[@class='aidanews2_k2_title']//a | //div[@class='sppb-column-addons']//div[@id='sppb-addon-1514496612040']//div[@class='aidanews2_k2_title']//a"
        paragraphPath = "//div[contains(@class, 'itemBody')]//p"
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

@app.route("/Zambia")
def Zambia():
        website = "https://www.lusakatimes.com/"
        articlePath = "//div[contains(@class, 'td-tc-page-content-visible')]//h3//a"
        paragraphPath = "//div[contains(@class, 'tdb_single_content')]//div[contains(@class, 'tdb-block-inner')]//p"
        return summarise(getGeneralCountry(driver=driver, website=website, articlePath=articlePath, paragraphPath=paragraphPath))

@app.route("/Zimbabwe")
def Zimbabwe():
     return summarise(getZimbabwe())

if __name__ == "__main__":
    app.run(debug=False)
