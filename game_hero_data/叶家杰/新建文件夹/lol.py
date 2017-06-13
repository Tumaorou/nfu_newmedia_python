from pprint import pprint
import requests
import json

def lol_data():#生成一个json档
    token = '89641-47687-87110-9E249'
    headers = {"DAIWAN-API-TOKEN":token}
    page=requests.get('http://lolapi.games-cube.com/champion',headers=headers)
    with open ('data/hero_data.json', mode='w', encoding='utf8')as file:
        json.dump(page.json(), file, indent=4 )

def get_dict_champion():#读取
    with open('data/hero_data.json','r') as champion:
        dict_champion = json.load(champion)
    return(dict_champion)

dict_champion = get_dict_champion()
dict_id = [x['id'] for x in dict_champion['data']]
dict_ename = [x['ename'] for x in dict_champion['data']]
dict_hero = {x['id']:x['ename'] for x in dict_champion['data']}

'''token = '89641-47687-87110-9E249'
headers = {"DAIWAN-API-TOKEN":token}
page = requests.get('http://lolapi.games-cube.com/GetChampionDetail?champion_id=1', headers=headers) 
pprint(page.json()) 
with open ('data/Annie.json','w') as champion:
    json.dump(page.json(), champion, indent=4 )'''


for id1 in dict_id[100:135]:
    token = '89641-47687-87110-9E249'
    headers = {"DAIWAN-API-TOKEN":token}
    page = requests.get('http://lolapi.games-cube.com/GetChampionDetail?champion_id={id0}'.format(id0=id1), headers=headers) 
    with open('data/{ename}.json'.format(ename=dict_hero[id1]),'w')as champion:
        json.dump(page.json(), champion, indent=4)
