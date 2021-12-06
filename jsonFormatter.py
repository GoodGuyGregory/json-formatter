import os
import re


def formatJson():
    # get working dir
    allFilesInCWD = os.listdir(os.getcwd())
    print("=================================================")
    # regex variable:
    filetoParse = input('Enter the file name to be formatted: ')

    fileRegex = re.compile(r'%s' % filetoParse)
    valueSpecificRegex = re.compile(r'\D+')
    keyValueRegex = re.compile(r'(\w+:) (.+)')

    jsonFilesFound = []
# file json files
    for potentialFile in allFilesInCWD:
        parseableFile = fileRegex.match(potentialFile)
        if parseableFile:
            print('Found File ' + str(parseableFile[0]) + '... ')
            jsonFilesFound.append(parseableFile[0])

    if len(jsonFilesFound) == 0:
        print('No files found for %s' % filetoParse)

    for jsonfile in jsonFilesFound:
        # open existing json
        openedOriginaljsonFile = open(jsonfile, 'r')
        originalJson = openedOriginaljsonFile.readlines()
        # open new json with formats
        newFormattedFile = open('formated.json', 'w')

#
        for line in originalJson:
            # search the files for keys
            foundKey = keyValueRegex.findall(line)
            if foundKey:
                # add the found key to the formatted file
                keyvalue = foundKey[0][0]
                pairValue = foundKey[0][1][:-1]
                pairValueSearch = valueSpecificRegex.search(pairValue)
                if pairValueSearch:
                    # format the value found to JSON
                    # reassign the value
                    pairValue = foundKey[0][1][1:-2]
                    # slice off the : and append the "<key>" formatting
                    formattedKeyValuepair = ' \"' + \
                        keyvalue[0:-1] + '\"' + ':' + \
                        '\"' + pairValue + '\"' + ','
                    newFormattedFile.write(formattedKeyValuepair)
                else:
                    # the value was a number or not in the regex params
                    formattedKey = ' \"' + \
                        keyvalue[0:-1] + '\"' + ':' + pairValue + ','
                    newFormattedFile.write(formattedKey)
            # append to the new jsonfile because the key might be alright
            else:
                newFormattedFile.write(line)


def main():
    formatJson()


main()
