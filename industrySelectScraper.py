#We want to scrape the articles that say "New US Manufacturing Operations Announced in MONTH YEAR" for information such as the Company Name, Particular State, and Number of Jobs that will be opened
#first let us experiment by providing the particular URL to the webpage that we want to scrape, i.e. a concrete example of such an article
#let's try using beautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulSoup
def webPageParser(link):
    companyName = []
    state = []
    jobCount = []
    r = requests.get(link)
    soup =  BeautifulSoup(r.content, 'html.parser')
    titles = []
    header = soup.find("h2").text
    splitter = " xskxskxsk "
    fullText = ""
    for x in soup.find_all("h3"):
        titles.append(x.text)
    target = soup.find('p')
    for t in target.find_next_siblings():
        if t.text in titles:
            fullText += splitter
        else:
            fullText += t.text + " "
    lst = fullText.split(splitter)
    lst = lst[1:-1]
    titles = titles[:-1]
    lst2 = []
    for x in zip(titles, lst):
        lst2.append(x[0] + "\n" + x[1])
    


webPageParser("https://www.industryselect.com/blog/new-us-manufacturing-plants-announced-may-2023")