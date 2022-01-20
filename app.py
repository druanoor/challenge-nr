import string
import sys

def fillStringDictionary(sortedDictionary, input_string):
    stringDictio = {}
    words = input_string.split()
    if len(words) < 3:
        return stringDictio

    for index, word in enumerate(words):
        if index+2 < len(words):
            wordTriplet = (word+" "+words[index+1]+" "+words[index+2])
            if wordTriplet in stringDictio:
                stringDictio[wordTriplet] += 1
            else:
                stringDictio[wordTriplet] = 1

    sortedDictionary = sorted(stringDictio.items(), key=lambda x: x[1], reverse=True)

    return sortedDictionary

def clearInput(input_string):
    input_string = input_string.lower()
    input_string = input_string.replace("’", "'").replace("”", "").replace("“", "").replace("—", "")
    input_string = input_string.replace("\n", " ")
    input_string = input_string.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    return input_string

def printResults(sortedDic):
    i = 0
    for x in sortedDic:
        if(i<100):
            print(x[0],"-", x[1])
            i+=1

def readInput():
    bookstring = ""
    if (len(sys.argv) < 2):
        bookstring = sys.stdin.read()
    else:
        for argv in sys.argv[1:]:
            book = open(argv, 'r', encoding="utf8")
            auxBookString = book.read()
            bookstring = bookstring+" "+auxBookString

    return bookstring

sortedDictionary = {}
book = readInput()
sortedDic = fillStringDictionary(sortedDictionary, clearInput(book))
printResults(sortedDic)
