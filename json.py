import json

mydict = {'name': 'Kanishkar', 'age': '22', 'city': 'Erode'}

# convert dict to json format

x = json.dumps(mydict)
print(x)

# convert json to dict

y = json.loads(x)
print(y)
