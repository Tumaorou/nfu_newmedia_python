# -*- coding: utf-8 -*-
from pprint import pprint
import requests
import json


'''with open('data/{ename}.json'.format(ename=dict_hero[id1]),'w', encoding='utf8') as d:
    dict_d = json.load(d)
    dict_hero = {x['id']:{x['passive']['name']:x['passive']['description']}.format(x=dict_d['data'][0])}
    pprint(dict_hero)
#    dict_hero = [x['id'] for x in dict_d['data'][0]]
#   pprint(dict_hero)'''
with open('data/Annie.json')as file1:
     dict_ab = json.load(file1)
     pprint(dict_ab)

