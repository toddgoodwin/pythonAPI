#!/usr/bin/python3

import argparse
import time
import requests
import hashlib

import mysharedcode

# define API
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

# calculate has
# md5 calc md5(ts+privateKey+publicKey)


def main():
    whichHero = input('Name your hero?')

    ##harvest private key
    with open(args.dev) as wadepriv:
        wilsonpriv = wadepriv.read().rstrip('\n')
    ##harvest pub key
    with open(args.pub) as wadepub:
        wilsonpub= wadepub.read().rstrip('\n')

    print(wilsonpriv + ' ' + wilsonpub)

    timestone = str(time.time()).rstrip('.')
    
    cerebro = mysharedcode.hashbuilder(timestone, wilsonpriv, wilsonpub)

    print(cerebro)

    uncanny = mysharedcode.marvelcharcall(XAVIER, timestone,cerebro, wilsonpub, whichHero)
    print(uncanny)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv')
    parser.add_argument('--pub', help='Provde the .pub')
    args = parser.parse_args()
    main()

