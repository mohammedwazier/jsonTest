# Working with Json File
# this case is testing real world working with JSON
# Add(Create), Add(Append), Edit, Delete, Load, Write to File

import json
import time

start = time.time()

def appendFunc(data):
    #Appending Data from data(array) from JSON
    #Basic Append Data
    data['data'].append({
        "Cpu" : 0,
        "realMem" : 0,
        "wireMem" : 0,
        "activeMem" : 0,
        "inactiveMem" : 0,
        "freeMem" : 0
    })


#Creating a protocol
defaultData = {}
defaultData['data'] = []
defaultData['run'] = 0
defaultData['timeExec'] = 0
#end Creating a protocol

#Append JSON Data
appendFunc(defaultData)
newData = json.dumps(defaultData, indent=2)
newData = json.loads(newData)
appendFunc(newData)
# appendFunc(newData)
for test in newData['data']:
    print(json.dumps(test, indent=2))
# print(json.dumps(newData, indent=2))
print(time.time()-start) #Print Time Load Execution
