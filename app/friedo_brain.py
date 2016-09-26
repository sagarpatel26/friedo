import json
from app import SCORE_THRESHOLD

def get_top(user_id, n, a):
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

    a = a['all_interests']
    jsn = json.loads(open('./app/questions.json').read())
    d = {}
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

#    print d
#    print a
    sfl = most_similar_users(user_id, n, d)
    sfl_r = [person_id for (score, person_id) in sfl if score>SCORE_THRESHOLD]
#    sfl_r = filter(lambda x: score > 0.1, )
#    print sfl
    return sfl_r

from math import sqrt
def similarity_score(person1,person2):

	# Returns ratio Euclidean distance score of person1 and person2

	both_viewed = {}		# To get both rated items by person1 and person2

	for item in dataset[person1]:
		if item in dataset[person2]:
			both_viewed[item] = 1

		# Conditions to check they both have an common rating items
		if len(both_viewed) == 0:
			return 0

		# Finding Euclidean distance
		sum_of_eclidean_distance = []

		for item in dataset[person1]:
			if item in dataset[person2]:
				sum_of_eclidean_distance.append(pow(dataset[person1][item] - dataset[person2][item],2))
		sum_of_eclidean_distance = sum(sum_of_eclidean_distance)

		return 1/(1+sqrt(sum_of_eclidean_distance))



def pearson_correlation(person1,person2, dataset):

	# To get both rated items
	both_rated = {}
	for item in dataset[person1]:
		if item in dataset[person2]:
			both_rated[item] = 1

	number_of_ratings = len(both_rated)

	# Checking for number of ratings in common
	if number_of_ratings == 0:
		return 0

	return number_of_ratings/32.0


def most_similar_users(person,number_of_users, dataset):
	# returns the number_of_users (similar persons) for a given specific person.
	scores = [(pearson_correlation(person,other_person, dataset), other_person) for other_person in dataset if  other_person != person ]

	# Sort the similar persons so that highest scores person will appear at the first
	scores.sort()
	scores.reverse()
	return scores[0:number_of_users]



