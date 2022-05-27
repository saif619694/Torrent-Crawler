

from get_values import value_scrape
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from concurrent.futures import ThreadPoolExecutor

a_dict = value_scrape(2)


def get_urls():
    url_l = []
    for url in a_dict:
        b = url['Url']
        url_l.append(b)
    return url_l


url_list = get_urls()


def scraped_downloads(url):
    options = Options()
    # options.headless = True
    browser = webdriver.Chrome(executable_path="../Chrome_driver/chromedriver.exe", options=options)

    browser.get(url)
    html_source = browser.page_source
    browser.close()

    soup = BeautifulSoup(html_source, 'html.parser')
    div = soup.find_all("td", class_="tlista", id="downloads")
    for e in div:
        e = e.get_text()
        e = e.replace("\n", '').strip()
    for sub in a_dict:
        if sub['Url'] == url:
            sub['Downloads'] = e


def rarbg():
    with ThreadPoolExecutor(max_workers=15) as executor:
        executor.map(scraped_downloads, url_list)
