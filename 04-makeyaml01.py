#!/usr/bin/python3

import yaml

def main():
    ##creates a blob of data to work with
    hitchhikers = [{"name":"Zaphod Beeblebrox", "species":"Betelgeusian"}, {"name":"Arthur Denter", "species":"human"}]

    ## display our ython data
    print(hitchhikers)

    ## open file write mode
    with open("galaxyguide.yaml", "w") as zfile:
        yaml.dump(hitchhikers, zfile)

main()

