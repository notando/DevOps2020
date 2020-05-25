import json
x = '{"name":"Rom", "age":30, "city":"BeerSheva"}'
y = json.loads(x)
print(y["age"])