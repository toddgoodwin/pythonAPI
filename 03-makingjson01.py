#!/usr/bin/python3
import json

def main():
    hitchhikers = [{"name":"Zaphod Beeblebox", "species": "Betelgeusian"}, {"name": "Arthur Dent", "species": "Human"}]

    with open("galaxyguide.json", "w") as zfile:
        json.dump(hitchhikers, zfile)

main()

