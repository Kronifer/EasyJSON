import json
import os
import random
import time


def init(filename):
    global file
    file = ""
    global undesirablechars
    undesirablechars = ["(", ")", "'", ","]
    for element in filename:
        if element == undesirablechars:
            pass
        else:
            file += element
    with open(file, "w") as write:
        data = {"Initiated": "True"}
        json.dump(data, write)


def getFilename():
    return file


def addData(key, value):
    keyInFile = ""
    valueInFile = ""
    for element in key:
        if element == undesirablechars:
            pass
        else:
            keyInFile += element
    for element in value:
        if element == undesirablechars:
            pass
        else:
            valueInFile += element
    with open(file, 'r+') as writefile:
        data = {keyInFile: valueInFile}
        adddatatofile = json.load(writefile)
        adddatatofile.update(data)
        writefile.seek(0)
        json.dump(adddatatofile, writefile)


def getData(key):
    with open(file, "r") as readfile:
        data = json.load(readfile)
        keyToRead = ""
        for element in key:
            if (element == undesirablechars):
                pass
            else:
                keyToRead += element
        value = data.get(keyToRead)
        return value


def removeData(key):
    with open(file, 'r+') as readfile:
        data = json.load(readfile)
        copydata = data
        json.dump(data, readfile)
    os.remove(file)
    keytoread = ""
    for element in key:
        if (element == undesirablechars):
            pass
        else:
            keytoread += element
    del copydata[key]
    with open(file, 'w') as writefile:
        json.dump(copydata, writefile)


def updateData(key, value):
    with open(file, 'r+') as readfile:
        data = json.load(readfile)
        os.remove(file)
        keytoread = ""
        for element in key:
            if element == undesirablechars:
                pass
            else:
                keytoread += element
            del data[key]
            newdata = {key: value}
            with open(file, 'w') as writefile:
                data.update(newdata)
                writefile.seek(0)
                json.dump(data, writefile)


def encryptData(key):
    with open('hiddenkeys.json', 'w') as hiddeninit:
        try:
            json.load(hiddeninit)
        except:
            firsttime = {"keys": 0}
            json.dump(firsttime, hiddeninit)
    with open(file, 'r+') as readfile:
        data = json.load(readfile)
        json.dump(data, readfile)
    os.remove(file)
    dataToEncrypt = data.get(key)
    encryptKey = []
    encryptedString = ''
    alphabetDict = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z',
        27: "1",
        28: "2",
        29: "3",
        30: "4",
        31: "5",
        32: "6",
        33: "7",
        34: "8",
        35: "9",
        36: "0"
    }
    alphaDictRev = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5,
        'f': 6,
        'g': 7,
        'h': 8,
        'i': 9,
        'j': 10,
        'k': 11,
        'l': 12,
        'm': 13,
        'n': 14,
        'o': 15,
        'p': 16,
        'q': 17,
        'r': 18,
        's': 19,
        't': 20,
        'u': 21,
        'v': 22,
        'w': 23,
        'x': 24,
        'y': 25,
        'z': 26,
        "1": 27,
        "2": 28,
        "3": 29,
        "4": 30,
        "5": 31,
        "6": 32,
        "7": 33,
        "8": 34,
        "9": 35,
        "0": 36
    }
    for element in dataToEncrypt:
        encryptInt = random.randint(1, 26)
        encryptChar = alphabetDict.get(encryptInt)
        encryptedString += encryptChar
        keyInt = alphaDictRev.get(element)
        encryptKey.append(keyInt)
    with open(file, 'w') as writefile:
        newData = {key: encryptedString}
        data.update(newData)
        writefile.seek(0)
        json.dump(data, writefile)
    with open('hiddenkeys.json', 'r+') as keyfile:
        keyRaw = json.load(keyfile)
        json.dump(keyRaw, keyfile)
    os.remove('hiddenkeys.json')
    keyAmount = keyRaw.get('keys')
    newKeyAmount = keyAmount + 1
    keyData = {newKeyAmount: encryptKey}
    del keyRaw['keys']
    newKeyValue = {'keys': newKeyAmount}
    keyRaw.update(keyData)
    keyRaw.update(newKeyValue)
    with open('hiddenkeys.json', 'w') as newkeyfile:
        newkeyfile.seek(0)
        json.dump(keyRaw, newkeyfile)

def getEncryptKey(number):
	with open('hiddenkeys.json', 'r') as readfile:
		data = json.load(readfile)
		key = data.get(number)
		return key

def decryptData(key, encryptKey):
	with open(file, 'r+') as writefile:
		encryptedData = json.load(writefile)
		json.dump(encryptedData, writefile)
	os.remove(file)
	newValue = ""
	alphabetDict = {
        1: 'a',
        2: 'b',
        3: 'c',
        4: 'd',
        5: 'e',
        6: 'f',
        7: 'g',
        8: 'h',
        9: 'i',
        10: 'j',
        11: 'k',
        12: 'l',
        13: 'm',
        14: 'n',
        15: 'o',
        16: 'p',
        17: 'q',
        18: 'r',
        19: 's',
        20: 't',
        21: 'u',
        22: 'v',
        23: 'w',
        24: 'x',
        25: 'y',
        26: 'z',
        27: "1",
        28: "2",
        29: "3",
        30: "4",
        31: "5",
        32: "6",
        33: "7",
        34: "8",
        35: "9",
        36: "0"
    }
	for element in encryptKey:
		newChar = alphabetDict.get(element)
		newValue += newChar
	with open(file, 'w') as writefile2:
		newData = {key: newValue}
		encryptedData.update(newData)
		json.dump(encryptedData, writefile2)
		return newValue


