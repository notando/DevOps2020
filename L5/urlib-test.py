import urllib.request
val = urllib.request.urlopen("https://free.currconv.com/api/v7/convert?q=USD_ILS&compact=n&apiKey=5d809c29233da8e068f7").read()
print(val)