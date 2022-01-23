import string
import sys
import os

def printHelp():
    print("Usage:\n")
    print("python3 app.py [args]\n")
    print("Example:\n")
    print("With files as arguments: python3 app.py text-examples/moby-dick.txt text-examples/2-word-catcher.txt")
    print("or")
    print("Using STDIN: cat text-examples/moby-dick.txt | python3 app.py\n")

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
    input_string = input_string.replace("’", "'")
    input_string = input_string.replace("”", "")
    input_string = input_string.replace("“", "")
    input_string = input_string.replace("—", "")
    input_string = input_string.replace("\n", " ")
    input_string = input_string.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    return input_string

def printResults(sortedDic):
    i = 0
    for x in sortedDic:
        if(i<100):
            print(x[0],"-", x[1])
            i+=1

def readInput(argv):
    bookstring = ""
    if (len(argv) < 2):
        if not sys.stdin.isatty():
            bookstring = sys.stdin.read()
        else:
            printHelp()
            
    elif(argv[1] == "-h" or argv[1] == "--help"):
        printHelp()
    else:
        for arg in argv[1:]:
            if(os.path.exists(arg)):
                book = open(arg, 'r', encoding="utf8")
                auxBookString = book.read()
                bookstring = bookstring+" "+auxBookString
                book.close()
            else:
                print("File: "+arg+" doesn't exists, exiting...")
                exit()

    return bookstring

if __name__ == '__main__':
    sortedDictionary = {}
    book = readInput(sys.argv)
    sortedDic = fillStringDictionary(sortedDictionary, clearInput(book))
    printResults(sortedDic)
