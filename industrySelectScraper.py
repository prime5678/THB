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
    for x in list(zip(titles, lst)):
        lst2.append(x[0] + "\n" + x[1])
    #above code extracts the text from the webpage and sorts the titles and corresponding paragraphs into a single list over which we can iterate and use methods to filter out specific information we need
    #let's try to find a way for the program to recognize/distinguish between the features of COMPANY NAME, STATE, and JOBS CREATED
    #ideas: try using NLP or LLMs for retrieval
    #idea 1: NLP in Python
    statesWithAbbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    keys = listOfStates + statesWithAbbreviations
    vals = listOfStates + listOfStates
    labeledStates = dict(zip(keys, vals))
    #created the list of potential inputs then put them into a dictionary that will centralize all potential inputs into a more finite set
    def whichState(text):
        p = {}
        for x in labeledStates.keys():
            if x in text and x not in p.keys():
                p.update({x: text.count(x)})
        g = {}
        for x in p.keys():
            if labeledStates.get(x) in g.keys():
                g.update({labeledStates.get(x): g.get(labeledStates.get(x)) + p.get(x)})
            else:
                g.update({labeledStates.get(x): p.get(x)})
        df = pd.DataFrame({
            'states': g.keys(),
            'count': g.values()
        })
        df_sorted = df.sort_values(by='count', ascending=False)
        df_sorted_and_filtered = df.loc[df_sorted['count'] == df_sorted['count'].max()]
        return list(df_sorted_and_filtered['states'])
    #helper function which returns a list of state(s) that are most common in the original text, which in most cases implies the correct state that we are looking for
    for x in lst2:
        state.append(whichState(x))
    print(state)
webPageParser("https://www.industryselect.com/blog/new-us-manufacturing-companies-unveiled-may-2022")
