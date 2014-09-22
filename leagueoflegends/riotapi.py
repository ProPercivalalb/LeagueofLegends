import apicaller
import staticdata
import tkinter
import datetime

apikey = 'fa3518a3-2076-40e9-adfd-2f19bf27a502'
region = 'euw'

print('Loading champions')
staticdata.load_champions(region, apikey)
print('Loaded {total} champions'.format(total=staticdata.get_champion_count()))

while True:
    name = input('Enter name: ')
    summoner = apicaller.get_summoner_by_name(name, region, apikey)
    print(summoner)
    print(summoner.get_revision_date(formated=True))
    data = apicaller.get_league(summoner, apikey)
    print(data)
    print(data.get_tier())
    data = apicaller.get_game_data(summoner, apikey)
    for i in range(data.get_match_count()):
        print(staticdata.get_champion_from_id(data.get_data()['games'][i]['championId']))

