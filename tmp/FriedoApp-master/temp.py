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
tvshows = [None, '1', '2', '3', '4', '5', '6', '7', '8']

'''
'''
'''
op
#print (j.items())
dict_items([('tvshows', '3,8,0,0'), ('books', '3,6,9,12'), ('dreamcity', '3,7,9,13'), ('food', '1,4,6,9'), ('dreams', '3,4,7,9'), ('user_id', 3), ('hate', '3,4,6,0'), ('movies', '3,4,7,11'), ('hobbies', '1,7,8,13')])
#print (j['tvshows'])
3,8,0,0
print(type(j['tvshows']))
str
print (type(temp_list2))
list and elements in temp_list2 are now 'int'
'''
dataset={
'Lisa': {
'Lady in the Water': 2.5,
'Snakes on a Plane': 3.5,
'Just My Luck': 3.0,
'Superman Returns': 3.5,
'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},
}


for i in a.items():
    for j in i:
        if( type(j) == str):
            continue
        #print (j.items())
        temp_list = []
        user_id = j['user_id']
        dataset[user_id] = {}
        abc = j['tvshows']
        temp_list = abc.split(',')
        temp_list2 = [int(x) for x in temp_list]
        print (temp_list2)
        for item_index in temp_list2:
            if(item_index > 0):
                item_name = tvshows[item_index]
                dataset[user_id][item_name] = 5
        #print (j['tvshows'])
print (dataset)



key_index = {

    'books': 0,
    'dreamcity': 7,
    'dreams': 6,
    'food': 3,
    'hate': 5,
    'hobbies': 4,
    'movies': 1,
    'tvshows': 2n

}
