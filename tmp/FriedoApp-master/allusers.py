import json
import random

key_index = {

    'books': 0,
    'dreamcity': 7,
    'dreams': 6,
    'food': 3,
    'hate': 5,
    'hobbies': 4,
    'movies': 1,
    'tvshows': 2

}

a = {
    "all_interests": [
    {
        "books": "3,6,9,12",
        "dreamcity": "3,7,9,13",
        "dreams": "3,4,7,9",
        "food": "1,4,6,9",
        "hate": "3,4,6,0",
        "hobbies": "1,7,8,13",
        "movies": "3,4,7,11",
        "tvshows": "3,8,0,0",
        "user_id": 3
    },
    {
        "books": "3,6,9,12",
        "dreamcity": "3,7,9,13",
        "dreams": "3,4,7,9",
        "food": "1,3,6,9",
        "hate": "3,1,6,0",
        "hobbies": "1,7,9,13",
        "movies": "3,4,7,11",
        "tvshows": "3,8,0,0",
        "user_id": 2
    }
    ]
}

a = a['all_interests']
d = {}


jsn = json.loads(open('questions.json').read())

'''
d[a['user_id']] = {}


jsn = json.loads(open('questions.json').read())

for key in a.keys():
    if key!='user_id':
        inx = key_index[key]
        for i in a[key].split(','):
            i = int(i)
            if (i==0):
                break
            d[a['user_id']][jsn['questions'][inx]['options'][i-1]] = 5.0
'''
for i in a:
    temp_storage = i
    d[temp_storage['user_id']] = {}
    for key in temp_storage.keys():
        if key!='user_id':
            inx = key_index[key]
            for i in temp_storage[key].split(','):
                i = int(i)
                if (i==0):
                    break
                d[temp_storage['user_id']][jsn['questions'][inx]['options'][i-1]] = 5

#random.uniform(1,5)
#print(d)

dataset = d
output = dataset
#print(dataset)

with open('delete.py', 'w') as f:
    json.dump(dataset, f)
