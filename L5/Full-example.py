import urllib.request, json

#openning a web request
url = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=5d809c29233da8e068f7")

#decode responce to str
data = json.loads(url.read().decode())          #decoding a web request



#parcing results

results = data['results']
USD_ILS = results['USD_ILS']
val = USD_ILS['val']
print(val)