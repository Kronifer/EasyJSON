import json
import os


def init(*filename):
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
        os.remove(file)
        keytoread = ""
        for element in key:
            if(element == undesirablechars):
                pass
            else:
                keytoread += element
        del data[key]
        with open(file, 'w') as writefile:
            json.dump(data, writefile)

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
