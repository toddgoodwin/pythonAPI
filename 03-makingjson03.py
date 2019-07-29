#!/usr/bin/python3
import json

def main():

    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code abive is string data. Python cannot easily work with this data.")
    input("Press Enter to continue\n")

    ## Create json string
    datacenterdecoded = json.loads(datacenterstring)

    ## this is now  a dict
    print(type(datacenterdecoded))

    ## display servers
    print(datacenterdecoded)

    ## display te servers in row3
    print(datacenterdecoded["row3"])

    ## display the 2nd server in row2
    print(datacenterdecoded["row2"][1])

    ##write code to display the last server in row3
    print(datacenterdecoded["row3"][-1])

    print(datacenterdecoded["row2"][0])
main()

