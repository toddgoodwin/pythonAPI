#!/usr/bin/python3
import json

def main():
    hitchhikers = [{"name":"Zaphod Beeblebox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    print(hitchhikers)
    print(type(hitchhikers))

    jsonstring = json.dumps(hitchhikers)

    print(jsonstring)
    print(type(jsonstring))

    print(hitchhikers[0])

    print(jsonstring[0])


main()

