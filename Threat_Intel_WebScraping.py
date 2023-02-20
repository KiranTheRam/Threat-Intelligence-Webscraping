import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def thn_scrape():
    URL = "https://thehackernews.com/"

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    article = soup.find("h2", class_="home-title").text
    date = soup.find("span", class_="h-datetime").text[1:]
    blurb = soup.find("div", class_="home-desc").text
    link = soup.find("a", class_="story-link")["href"]
    return {"article": article, "date": date, "blurb": blurb, "link": link}


def dr_scrape(URL):
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    article = soup.find("span", class_="article-title").text
    date = soup.find("div", class_="d-md-none arcile-date").text
    blurb = soup.find("div", class_="article-body d-md-none").text
    link = soup.find("a", class_="article-edge-wrap--link")["href"]
    return {"article": article, "date": date, "blurb": blurb, "link": link}


def kos_scrape():
    URL = "https://krebsonsecurity.com/"

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    article = soup.find("h2", class_="entry-title")
    link = article.find("a")["href"]
    article = article.find("a").text
    date = soup.find("span", class_="date updated")
    date = date.text
    blurb = soup.find("div", class_="entry-content")
    blurb = blurb.find("p").text
    return {"article": article, "date": date, "blurb": blurb, "link": link}


while True:
    site_code = input("\nEnter one of the following:\nThe Hacker Network -> thn \nDark Reading - Security Monitoring -> dr_sm\nDark Reading - Cloud -> dr_cloud\nDark Reading - Attack Breaches -> dr_ab\nDark Reading - Application Security -> dr_as\nKrebbs On Security -> kos\n->")

    site_code = site_code.lower()
    if site_code == 'exit':
        exit(-34)
    elif site_code == "thn":
        article_info = thn_scrape()
    elif site_code == "dr_sm":
        URL = "https://www.darkreading.com/security-monitoring"
        article_info = dr_scrape(URL)
    elif site_code == "dr_cloud":
        URL = "https://www.darkreading.com/cloud"
        article_info = dr_scrape(URL)
    elif site_code == "dr_ab":
        URL = "https://www.darkreading.com/attacks-breaches"
        article_info = dr_scrape(URL)
    elif site_code == "dr_as":
        URL = "https://www.darkreading.com/application-security"
        article_info = dr_scrape(URL)
    elif site_code == "kos":
        article_info = kos_scrape()
    else:
        print("Value entered not defined, refer to prompt and try again")
        continue

    print("____________________\nFound Link: " + article_info["link"])
    print(article_info["article"] + "\n" + article_info["date"] + "\n" + article_info["blurb"] + "\n____________________\n")
