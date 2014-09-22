import datetime
import json

class summoner():

    def __init__(self, name, region, data):
        self.name = name
        self.region = region
        self.data = data

    def __str__(self):
        return json.dumps(self.data, indent=4)

    def get_data(self):
        return self.data

    def get_name(self):
        return self.name

    def get_region(self):
        return self.region

    def get_name_in_game(self):
        return self.data[self.name]['name']

    def get_profile_icon_id(self):
        return self.data[self.name]['profileIconId']

    def get_id(self):
        return self.data[self.name]['id']

    def get_revision_date(self, formated=False):  
        revisiondate = self.data[self.name]['revisionDate']
        if formated:
            return datetime.datetime.fromtimestamp(revisiondate / 1000).strftime('%d-%m-%Y %H:%M:%S')
        return revisiondate

    def get_summoner_level(self):
        return self.data[self.name]['summonerLevel']

class league():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

    def get_data(self):
        return self.data

    def get_tier(self):
        self.data[str(self.summoner.get_id())]['tier']

    def get_league_points(self):
        pass
    
    def __str__(self):
        return json.dumps(self.data, indent=4)

class game():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

    def get_data(self):
        return self.data

    def get_match_count(self):
        return len(self.data['games'])
    
    def __str__(self):
        return json.dumps(self.data, indent=4)

class matchhistory():

    def __init__(self, summoner, data):
        self.summoner = summoner
        self.data = data

class match():

    def __init__(self):
        pass
        
