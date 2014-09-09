import urllib.request
import json

def request_raw(url):
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        the_page = response.read()

        return str(the_page, 'UTF-8')
    except urllib.error.HTTPError as e:
        print('Error', e.code)

    return ''

def request_json(url):
    json_data = request_raw(url)
    data = json.loads(json_data)
    return data

#request_json('https://euw.api.pvp.net/api/lol/euw/v1.4/summoner/by-name/percivalalb?api_key=fa3518a3-2076-40e9-adfd-2f19bf27a502')