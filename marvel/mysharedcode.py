import hashlib
import requests

def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

def marvelcharcall(url, stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(url+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    print(url+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    getmystuff =  r.json()
    #print(getmystuff)
    #
    print(getmystuff['data']['results'][0]['id'])
    print(getmystuff['data']['results'][0]['name'])
    print(getmystuff['data']['results'][0]['description'])

