#!/usr/bin/python3

import sys

while True:
    try:

        print('Lets divide x by y')
        x=int(input('What is the int value of x?'))
        y=int(input('What is the int value of y?'))
        print('The value of x/y is :', x/y)
        z = 'successful'
    except ZeroDivisionError as zerr:
        print('Handling of a run time error: ', zerr)
        z = 'error div 0'
    except:
        print('Oh wow.  We did not produce code to handle this type of error yet.')
        print(sys.exc_info()[0])
        z = sys.exc_info()[0]
        #raise
    finally:
        with open('try.log', 'a') as log:
            log.write(str(z)+'\n')
