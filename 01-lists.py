#!/usr/bin/python3

def main():
    zlist = ['cisco', 'juniper', 'bigip', 'tellabs', 'meraki']

    print(zlist[2])

    zlist.append('nortel')

    print(zlist[-1])

    zcloud = ['aws', 'openstack', 'google', 'azure']

    zlist.extend(zcloud)
    
    print(zlist)

main()

