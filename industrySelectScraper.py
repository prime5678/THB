#We want to scrape the articles that say "New US Manufacturing Operations Announced in MONTH YEAR" for information such as the Company Name, Particular State, and Number of Jobs that will be opened
#first let us experiment by providing the particular URL to the webpage that we want to scrape, i.e. a concrete example of such an article
#let's try using beautifulSoup
import requests
import pandas as pd
from bs4 import BeautifulSoup
import nltk

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('averaged_perceptron_tagger')

def webPageParser(link):
    listOfStates = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
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
        lst2.append(x[1])
    #above code extracts the text from the webpage and sorts the titles and corresponding paragraphs into a single list over which we can iterate and use methods to filter out specific information we need
    #let's try to find a way for the program to recognize/distinguish between the features of company name, state, and jobs that will be created
    #ideas: try using NLP or LLMs for retrieval
    #idea 1: NLP in Python
    for x in lst2:
        templst = []
        for sent in nltk.sent_tokenize(x):
            for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
                if hasattr(chunk, 'label'):
                    templst.append(chunk.label() + " " + ' '.join(c[0] for c in chunk))
        print(templst)
        lstGPE = [s[4:] for s in templst if "GPE" in s]
        lstPERSON = [s for s in templst if "PERSON" in s or "ORGANIZATION" in s]
        if len(lstGPE) == 1:
            state.append(lstGPE[0])
        else:
            p = [g for g in lstGPE if g in listOfStates]
            state.append(p[0])
        for q in range(len(lstPERSON)):
            if "PERSON" in lstPERSON[q]:
                lstPERSON[q] = lstPERSON[q][len("PERSON") + 1:]
            else:
                lstPERSON[q] = lstPERSON[q][len("ORGANIZATION") + 1:]

webPageParser("https://www.industryselect.com/blog/new-us-manufacturing-plants-announced-may-2023")
