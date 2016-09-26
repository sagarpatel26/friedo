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
    "interests": {
        "books": "3,6,9,12",
        "dreamcity": "3,7,9,13",
        "dreams": "3,4,7,9",
        "food": "1,4,6,9",
        "hate": "3,4,6,0",
        "hobbies": "1,7,8,13",
        "movies": "3,4,7,11",
        "tvshows": "3,8,0,0",
        "user_id": 3
    }
}

a = a['interests']

d = {}
d[a['user_id']] = {}

import json
jsn = json.loads(open('questions.json').read())

for key in a.keys():
    if key!='user_id':
        inx = key_index[key]
        for i in a[key].split(','):
            i = int(i)
            if (i==0):
                break
            d[a['user_id']][jsn['questions'][inx]['options'][i-1]] = 5.0

print(d)
