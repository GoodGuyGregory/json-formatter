import os
import re


def formatJson():
    # get working dir
    allFilesInCWD = os.listdir(os.getcwd())
    print("=================================================")
    # regex variable:
    filetoParse = input('Enter the file name to be formatted: ')

    fileRegex = re.compile(r'%s' % filetoParse)
    keyRegex = re.compile(r'(\w+:)')
    valueRegex = re.compile(r'\(\'.+\'\)')

    jsonFilesFound = []
# file json files
    for potentialFile in allFilesInCWD:
        parseableFile = fileRegex.match(potentialFile)
        if parseableFile:
            print('Found File ' + str(parseableFile[0]) + '... ')
            jsonFilesFound.append(parseableFile[0])

    for jsonfile in jsonFilesFound:
        # open existing json
        openedOriginaljsonFile = open(jsonfile, 'r')
        originalJson = openedOriginaljsonFile.readlines()
        # open new json with formats
        newFormattedFile = open('formated.json', 'w')

        for line in originalJson:
            foundKey = keyRegex.match(line)
            if foundKey:
                print('found ' + foundKey[0])


def main():
    formatJson()


main()
