import json

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

a = a['interests']
d = {}


jsn = json.loads(open('questions.json').read())

d[a['user_id']] = {}



for key in a.keys():

    if key!='user_id':
        inx = key_index[key]
        temp_storage = []
        for i in a[key].split(','):
            i = int(i)
            if (i==0):
                break
            b = jsn['questions'][inx]['options'][i-1]
            temp_storage.append(b)
            d[a['user_id']][key] = temp_storage

print (d)
