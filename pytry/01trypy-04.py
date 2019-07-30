#!/usr/bin/python3

import uuid

#simulate job number with uuid package

ticket = uuid.uuid1()

try:
    print('Please type the config file to load')
    configfile = input("Filename : ")
    configfileobj = open(configfile, 'r')
    switchconfig = configfileobj.read()
    configfileobj.close()
except:
    x = 'Error with obtaining config file info'
else:
    x = 'Switch file found'
finally:
    with open('try04.log','a') as zlog:
        print('\n\n\Writing results of service to log file...')
        print(ticket, ' - ', x, file=zlog)
    
