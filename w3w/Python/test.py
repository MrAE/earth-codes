

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

#w3w = what3words.Geocoder(api_key)
#res = w3w.reverse(lat=51.484464, lng=-0.195405)
#
#res = w3w.forward('yarn.tigers.verbs')
#res = w3w.standardblend("coffee.a.a")
#res = w3w.standardblend("coffee.*.*")


aa = wordList.index("coffee")
ab = wordList.index("hop")
ac = wordList.index("blue")
ad = wordList.index("brain")

ae = wordList.index("farmer")
af = wordList.index("shark")
ag = wordList.index("bliss")
ah = wordList.index("radar")


t1 = [wordList[aa] + '.' + wordList[aa] + '.' + i for i in abc]
t2 = [wordList[aa] + '.' + wordList[ab] + '.' + i for i in abc]
t3 = [wordList[aa] + '.' + wordList[ac] + '.' + i for i in abc]
t4 = [wordList[aa] + '.' + wordList[ad] + '.' + i for i in abc]

t5 = [wordList[ad] + '.' + wordList[ad] + '.' + i for i in abc]
t6 = [wordList[ad] + '.' + wordList[ac] + '.' + i for i in abc]

t7 = ['farmer' + '.' + 'coffee' + '.' + i for i in abc]
t8 = ['farmer' + '.' + 'brain' + '.' + i for i in abc]
t9 = ['shark' + '.' + 'radar' + '.' + i for i in abc]
t10 = ['shark' + '.' + 'coffee' + '.' + i for i in abc]

t11 = ['whale' + '.' + 'shark' + '.' + i for i in abc]
t12 = ['fish' + '.' + 'shar' + '.' + i for i in abc]
t13 = ['fish' + '.' + 'rad' + '.' + i for i in abc]

t14 = ['neon' + '.' + 'shark' + '.' + i for i in abc]
t15 = ['shark' + '.' + 'bait' + '.' + i for i in abc]
t16 = ['moon' + '.' + 'space' + '.' + i for i in abc]

t17 = ['gold' + '.' + 'shark' + '.' + i for i in abc]
t18 = ['amp' + '.' + 'gold' + '.' + i for i in abc]
t19 = ['moon' + '.' + 'pi' + '.' + i for i in abc]

t20 = ['truck' + '.' + 'shark' + '.' + i for i in abc]
t21 = [i + '.' + 'truck' + '.' + 'shark' for i in abc]

store = []

for i in t1:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t2:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t3:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t4:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t5:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t6:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t7:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t8:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t9:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t10:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t11:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t12:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)
    
for i in t13:
    res = w3w.standardblend(i)
    store.append(res)
    time.sleep(3)

for i in t14:
    res14 = w3w.standardblend(i)
    store.append(res14)
    time.sleep(3)

for i in t15:
    res15 = w3w.standardblend(i)
    store.append(res15)
    time.sleep(3)
    
for i in t16:
    res16 = w3w.standardblend(i)
    store.append(res16)
    time.sleep(2)

for i in t17:
    res17 = w3w.standardblend(i)
    store.append(res17)
    time.sleep(2)

for i in t18:
    res18 = w3w.standardblend(i)
    store.append(res18)
    time.sleep(2)
    
for i in t19:
    res19 = w3w.standardblend(i)
    store.append(res19)
    time.sleep(2)

for i in t20:
    res20 = w3w.standardblend(i)
    store.append(res20)
    time.sleep(2)

for i in t21:
    res21 = w3w.standardblend(i)
    store.append(res21)
    time.sleep(2)


with open("store_data.pkl", 'wb') as output:
    pickle.dump(store, output, pickle.HIGHEST_PROTOCOL)


tmp = {i: store[i] for i in range(len(store))} 
with open('store_data.json', 'w') as output:
    json.dump(tmp, output)







