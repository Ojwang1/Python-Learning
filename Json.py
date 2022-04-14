#JSON is a syntax for storing and exchanging data.

import json
#some JsON:

x='{"name":"John","age":30,"city":"New York"}'
#parse x:
y=json.loads(x)
# the result is a Python dictionary:
print(y["age"])

#Convert  from Python to JSON Using json.dumps(x)



