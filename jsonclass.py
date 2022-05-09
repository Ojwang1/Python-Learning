import json


x = '{"name":"John","age":30,"city":"New York"}'
# parse x:

y = json.loads(x)

#the result is a Python dictionary:
print(y["age"])

import json

x={
    "name":"John",
    "age":30,
    "married":True,
    "divorced":False,
    "children":("Ann","Billy"),
    "pets":None,
    "cars":[
        {"model":"BMW 230","mpg":27.5},
        {"model":"Ford Edge","mpg":24.1}
    ]
}
print(json.dumps(x,indent=4))

#RegEx in Pythone

import re
txt="The rain in Kenya is made by Nicholas"
x=re.search("^The.*Nicholas$",txt)
print(x)

import re
txt="The rain in Kenya is made by Nicholas"
x=re.findall("^The.*Nicholas$",txt)
print(x)

import re
txt="The rain in Kenya is made by Nicholas"
x=re.split("^The.*Nicholas$",txt)
print(x)

import re
txt="The rain in Kenya is made by Nicholas"
x=re.sub("^The.*Nicholas$",txt)
print(x)

#Example2
import re
txt="wayanicholas@gmail.com"
x=re.sub("^The.*Nicholas$",txt)
print(x)




#Metacharacters






