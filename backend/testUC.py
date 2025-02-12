import undetected_chromedriver as uc

chrome_options = uc.ChromeOptions()
chrome_options.add_argument("--headless=new")  # Use the new headless mode
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = uc.Chrome(options=chrome_options, version_main=132)
driver.get("https://www.google.com")
