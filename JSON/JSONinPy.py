#JSON is a javascript object notation used to store and transfer data

import json

x='{"Name":"Ashwin","Age":"30"}'  #JSON object
y=json.loads(x)   #coverts JSON to Py
print(y["Age"])


z={'Name':"Ashwin",
"Age":20,
"Dept":"IT"
}
s=json.dumps(z)   #coverts  Py to JSON 
print(s)

