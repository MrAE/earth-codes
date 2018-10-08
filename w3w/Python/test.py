

import what3words
import string
import time
import pickle
import json
from random import shuffle
from os import environ

with open('../w3w_jlp.conf.ig') as f:
    x = f.readlines()
    api_key = x[0].strip()
 

with open('/usr/share/dict/words') as w:
    tmp = w.readlines()
    wl = [i.strip() for i in tmp]

abc = list(string.ascii_lowercase)
wordList = wl
shuffle(wordList)

wordList.index("coffee")

w3w = what3words.Geocoder(api_key)
res = w3w.reverse(lat=51.484464, lng=-0.195405)

res = w3w.forward('yarn.tigers.verbs')
res = w3w.standardblend("coffee.a.a")
res = w3w.standardblend("coffee.*.*")


aa = wordList.index("coffee")
ab = wordList.index("hop")
ac = wordList.index("blue")
ad = wordList.index("brain")


t1 = [wordList[aa] + '.' + wordList[aa] + '.' + i for i in abc]
t2 = [wordList[aa] + '.' + wordList[ab] + '.' + i for i in abc]
t3 = [wordList[aa] + '.' + wordList[ac] + '.' + i for i in abc]
t4 = [wordList[aa] + '.' + wordList[ad] + '.' + i for i in abc]

res = w3w.standardblend(tmp)

store = []

for i in t1:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(5)

with open("store_data.pkl", 'wb') as output:
    pickle.dump(store, output, pickle.HIGHEST_PROTOCOL)

for i in t2:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(5)



ustore = list(set([ri['blends'][0]['words'] for ri in store]))
tmp = {i: ustore[i] for i in range(len(ustore))} 


with open('store_data.json', 'w') as output:
    json.dump(ustore, output)









