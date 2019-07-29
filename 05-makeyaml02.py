#!/usr/bin/python3

import yaml
import json

def main():
    with open("galaxyguide.yaml", "r") as yamlfile:
        pyyammy = yaml.load(yamlfile)
    pyyammy.append({'name':'Captain America', 'species':'Super Hero'})
    print(pyyammy)

    with open("yamltojson.json", "w") as yamlJ:
        json.dump(pyyammy, yamlJ)

main()

