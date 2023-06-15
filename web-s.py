#goal: write a program that can take in a .txt file and convert it to csv or otherwise format it properly
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
    with open(f) as reader:
        while reader.readable():
            firstLine = reader.readline()
            if firstLine.isspace():
                print("")
            while(firstLine[0].isalpha()):
                print(firstLine)
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
                print(n, abbreviation, stat, eq, description)
                #above code: takes in the string corresponding to a company with the initial information, then takes required information (name, bio, ticker, weight in index) and sorts that info
                #figure out a way to read n lines corresponding to the company and then store the information appropriately
                firstLine = reader.readline()
                lst = []
                lst1 = []
                dictionary2 = {}
                while(firstLine.__contains__(n) or firstLine[0].isnumeric() or firstLine.isspace()):
                    if(firstLine[0].isnumeric()):
                        if(firstLine.__contains__('SDG')):
                            val = int(firstLine[firstLine.index('SDG') + 4 :firstLine.index(':')])
                            if(firstLine.__contains__('exposure)')):
                                fL = firstLine[firstLine.index("-") + 2:]
                            else:
                                fL = firstLine[firstLine.index('-') + 2:]
                                fl1 = reader.readline()
                                fL += " - " + fl1
                        else:
                            val = int(firstLine[:firstLine.index('.')])
                            fL = firstLine[firstLine.index('-') + 2:]
                        lst.append(val)
                        lst1.append(fL)
                        dictionary2.update({val : fL})
                    elif(firstLine.isspace()):
                        print("")
                    firstLine = reader.readline()
                for x in range(1, 18):
                    if x in dictionary2.keys():
                        dictionary.get(str(x)).append(dictionary2.get(x))
                    else:
                        dictionary.get(str(x)).append("N/A")
                for x in range(1, 18):
                    print(dictionary.get(str(x)))
    return 1

print(txtFormatterTHB('MSCI World All Company ESG Exposure.txt'))
