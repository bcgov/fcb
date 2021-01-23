
import sys
import json
inputStr = sys.argv[1]
inputStr = inputStr.replace(']','').replace('[', '')
inputList = inputStr.split(',')
newList = []
for i in inputList:
    newList.append(i.strip())
jsonstr = json.dumps(newList)
sys.stdout.write(jsonstr)

