#goal: write a program that can take in a .txt file and convert it to csv or otherwise format it properly
import pandas as pd
def txtFormatterTHB(f): #make sure that f is located in the same directory as this file
    assert type(f) == str #ensures that the argument that is passed into this function is a txt file or string
    name = []
    ticker = []
    statistic = []
    equity = []
    bio = []
    sdg1 = []
    sdg2 = []
    sdg3 = []
    sdg4 = []
    sdg5 = []
    sdg6 = []
    sdg7 = []
    sdg8 = []
    sdg9 = []
    sdg10 = []
    sdg11 = []
    sdg12 = []
    sdg13 = []
    sdg14 = []
    sdg15 = []
    sdg16 = []
    sdg17 = []
    #initialized all of the lists that we will be appending information to, these lists will later be formatted
    dictionary = {
        "1": sdg1,
        "2": sdg2,
        "3": sdg3,
        "4": sdg4,
        "5": sdg5,
        "6": sdg6,
        "7": sdg7,
        "8": sdg8,
        "9": sdg9,
        "10": sdg10,
        "11": sdg11,
        "12": sdg12,
        "13": sdg13,
        "14": sdg14,
        "15": sdg15,
        "16": sdg16,
        "17": sdg17
    }
    #dictionary that will hold a reference to all of the lists to make it easier to append values
    columns = ["Name", "Ticker", "Weight in Index", "Equity", "Description", "SDG1", "SDG2", "SDG3", "SDG4", "SDG5", "SDG6", "SDG7", "SDG8", "SDG9", "SDG10", "SDG11", "SDG12", "SDG13", "SDG14", "SDG15", "SDG16", "SDG17"]
    dictionary2 = {}
    with open(f) as reader:
        firstLine = reader.readline()
        while reader.readable():
            if firstLine.isspace():
                print("")
                firstLine = reader.readline()
            elif(firstLine[0].isalpha()):
                p = firstLine[firstLine.index('.') - 1:]
                stat = float(p[:p.index("\t")])
                n = firstLine[:firstLine.index('0') - 1]
                description = firstLine[firstLine.index('"'):]
                capital = n[0]
                finalNum = str(stat)[-1]
                substring = firstLine[firstLine.index(finalNum) + 2:]
                abbreviation = substring[substring.index(capital):substring.index(" ")]
                ab = abbreviation[-1]
                eq = substring[substring.index(ab) + 2:substring.index('"') - 1]
                name.append(n)
                ticker.append(abbreviation)
                statistic.append(stat)
                equity.append(eq)
                bio.append(description)
                #above code: takes in the string corresponding to a company with the initial information, then takes required information (name, bio, ticker, weight in index) and sorts that info
                #figure out a way to read n lines corresponding to the company and then store the information appropriately
                firstLine = reader.readline()
                while(reader.readable()):
                    if(firstLine.isspace()):
                        print("")
                    elif(firstLine[0].isnumeric()):
                        val = firstLine[firstLine.index("G") + 2:firstLine.index(":")]
                        temp = firstLine[firstLine.index("-") + 2: -1]
                        temp2 = reader.readline()
                        fL = temp + " - " + temp2
                        dictionary2.update({val:fL})
                    else:
                        firstLine = reader.readline()
                        break
                    firstLine = reader.readline()
                    if(len(firstLine) == 0):
                        break
                for x in range(1, 18):
                    if str(x) in dictionary2.keys():
                        dictionary.get(str(x)).append(dictionary2.get(str(x)))
                    else:
                        dictionary.get(str(x)).append("N/A")
                if(len(firstLine) == 0):
                    break
    df = pd.DataFrame(list(zip(name,  ticker, statistic, equity, bio, sdg1, sdg2, sdg3, sdg4, sdg5, sdg6, sdg7, sdg8, sdg9, sdg10, sdg11, sdg12, sdg13, sdg14, sdg15, sdg16, sdg17)), columns = columns)
    df.to_excel('export.xlsx')
    return None

#remember to close export.xlsx otherwise it will an error (as the program is attempting to write to an open file)
txtFormatterTHB('msciSample.txt')
