import apicaller

champion_id = {}
id_champion = {}
champion_count = 0


def load_champions(region, apikey):
    global champion_count
    champions = apicaller.get_champions(region, apikey)

    for champion_name in champions['data']:
        champion = champions['data'][champion_name]
        
        champion_id[champion['name']] = champion['id']
        id_champion[champion['id']] = champion['name']

        champion_count += 1

    #for stuff in sorted(id_champion.keys()):
    #    print(id_champion[stuff], stuff)

def get_champion_from_id(championid):
    return id_champion[championid]

def get_id_from_champion(champion):
    return champion_id[champion]

def get_champion_count():
    return champion_count
