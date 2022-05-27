from thirteen_thirtysevenX.get_values import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

search = search
if "+" in search:
    search = search.replace("+", "%20")


def value_scrape(page_number):
    data = []
    url_list = []
    for pages in range(1, page_number):
        options = Options()
        # options.headless = True
        browser = webdriver.Chrome(executable_path="../Chrome_driver/chromedriver.exe", options= options)
        url = f"https://www.rarbggo.to/search/{pages}/?search={search}"
        browser.get(url)
        html_source = browser.page_source
        browser.close()

        soup = BeautifulSoup(html_source, 'html.parser')

        div = soup.find_all("table", class_="tablelist2")

        for x in div:
            t = x.find_all("td", class_="tlista")
            l = []
            for text in t:
                a = text.get_text()
                l.append(len(a))
        if not l:
            break

        for links in div:
            v = links.find_all("td", class_="tlista")
            str_list = []
            for elem in v:
                a = elem.get_text()
                a = a.replace("\n\n", '').split("\n")
                if a:
                    str_list.append(a)
            str_l = [item for s in str_list for item in s]
            str_l = [i for i in str_l if i]
            str_l = [str_l[n:n + len(str_l)] for n in range(0, len(str_l), len(str_l))]
            [str_l] = str_l
            gb_index = []
            for index, item in enumerate(str_l):
                if " GB" in item:
                    gb_index.append(index)
                if " MB" in item:
                    gb_index.append(index)

            final_list = []
            name_index = 0
            for s in gb_index:
                uploader_index = s + 4
                temp = str_l[name_index:uploader_index]
                name_index = uploader_index
                final_list.append(temp)
            for list_value in final_list:
                if len(list_value) == 7:
                    name = list_value[0]
                    type = list_value[1]
                    date_uploaded = list_value[2]
                    size = list_value[3]
                    seeders = list_value[4]
                    leechers = list_value[5]
                    uploader = list_value[6]
                    dictionary = {"Name": name, "Type": type, "Date_uploaded": date_uploaded,
                                  "Total_size": size, "Seeders": seeders, "Leechers": leechers,
                                  "Uploaded_by": uploader}
                    data.append(dictionary)
                elif len(list_value) == 8:
                    name = list_value[0]
                    genre = list_value[1]
                    type = list_value[2]
                    date_uploaded = list_value[3]
                    size = list_value[4]
                    seeders = list_value[5]
                    leechers = list_value[6]
                    uploader = list_value[7]
                    dictionary = {"Name": name, "Genre": genre, "Type": type, "Date_uploaded": date_uploaded,
                                  "Total_size": size, "Seeders": seeders, "Leechers": leechers,
                                  "Uploaded_by": uploader}
                    data.append(dictionary)
                elif len(list_value) == 6:
                    name = list_value[0]
                    date_uploaded = list_value[1]
                    size = list_value[2]
                    seeders = list_value[3]
                    leechers = list_value[4]
                    uploader = list_value[5]
                    dictionary = {"Name": name, "Date_uploaded": date_uploaded,
                                  "Total_size": size, "Seeders": seeders, "Leechers": leechers,
                                  "Uploaded_by": uploader}
                    data.append(dictionary)

        for d in div:
            v = str(d.find_all("td", class_="tlista")).split('>')
            for elem in v:
                if "/torrent/" in elem:
                    url_pattern = 'href="(.*?)"'
                    u = re.search(url_pattern, elem)
                    url = u.group().replace('href=', '').replace('"', '')
                    url_list.append(url)
        print(f"Indexing movies from page {pages}")
    x = 0
    for dict_list in data:
        dict_list["Url"] = f'https://www.rarbggo.to{url_list[x]}'
        x += 1

    return data
