# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
dataset={
'Lisa': {
'Lady in the Water': 2.5,
'Snakes on a Plane': 3.5,
'Just My Luck': 3.0,
'Superman Returns': 3.5,
'You, Me and Dupree': 2.5,
'The Night Listener': 3.0},

'Gene': {'Lady in the Water': 3.0,
'Snakes on a Plane': 3.5,
'Just My Luck': 1.5,
'Superman Returns': 5.0,
'The Night Listener': 3.0,
'You, Me and Dupree': 3.5},

'Michael': {'Lady in the Water': 2.5,
'Snakes on a Plane': 3.0,
'Superman Returns': 3.5,
'The Night Listener': 4.0},

'Claudia': {'Snakes on a Plane': 3.5,
'Just My Luck': 3.0,
'The Night Listener': 4.5,
'Superman Returns': 4.0,
'You, Me and Dupree': 2.5},

'Mick': {'Lady in the Water': 3.0,
'Snakes on a Plane': 4.0,
'Just My Luck': 2.0,
'Superman Returns': 3.0,
'The Night Listener': 3.0,
'You, Me and Dupree': 2.0},

'Jack': {'Lady in the Water': 4.0,
'Snakes on a Plane': 4.0,
'The Night Listener': 4.0,
'Superman Returns': 4.0,
'You, Me and Dupree': 4},

'Toby': {'Snakes on a Plane':4,
'You, Me and Dupree':4.0,
'Superman Returns':4.0}}

'''
import json
dataset = json.loads(open('../delete.py').read())
print(dataset)
