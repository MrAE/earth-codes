

import what3words
from os import environ
api_key = environ['W3W_API_KEY']
w3w = what3words.Geocoder(api_key)
res = w3w.reverse(lat=51.484464, lng=-0.195405)

res = w3w.forward('yarn.tigers.verbs')
res = w3w.standardblend("coffee.a.a")
res = w3w.standardblend("coffee.*.*")

print(res)




