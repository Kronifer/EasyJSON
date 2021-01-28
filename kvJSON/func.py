import json
import os
import subprocess
import random


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
		     if(element == undesirablechars):
		        pass
		     else:
		        keyToRead += element
		value = data.get(keyToRead)
		return value

def removeData(key):
    with open(file, 'r+') as readfile:
        data = json.load(readfile)
        os.remove("datastoring.json")
        keytoread = ""
        for element in key:
            if(element == undesirablechars):
                pass
            else:
                keytoread += element
        del data[key]
        with open(file, 'w') as writefile:
            json.dump(data, writefile)

def encryptData(key):
	with open(file, "r+") as readfile:
		data = json.load(readfile)
		keyToRead = ""
		for element in key:
			if element == undesirablechars:
				pass
			else:
				keyToRead += element
		value = data.get(keyToRead)
		alphadict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
		11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o', 16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't', 21: 'u',
		22: 'v', 23: 'w', 24: 'x', 25: 'y', 26: 'z'}
		encryptKey = []
		newKey = ''
		for element in value:
			shiftvalue = random.randint(1, 26)
			encryptchar = alphadict.get(shiftvalue)
			encryptKey.append(shiftvalue)
			newkey += encryptchar
		newdata = {keyToRead: newKey}
		data.update(newdata)
		readfile.seek(0)
		json.dump(data, readfile)
		with open("hiddenkeys.json", 'w') as writefile:
			json.dump(encryptKey, writefile)
			subprocess.check_call(["attrib","+H","hiddenkeys.json"])



        