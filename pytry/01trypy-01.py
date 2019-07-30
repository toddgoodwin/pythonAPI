#!/usr/bin/python3

while True:
    try:
        name = input('Enter a file name: ')
        with open(name, 'w') as myfile:
            myfile.write('Well done.\n')
    except:
        print('Error in creating that file...try again')
    else:
        print('File created successfull')
        break
