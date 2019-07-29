#!/usr/bin/python3

def showInstructions():
    #print a maain menu and the commands

    print('''
    RPG Game
    ========
    Commands:
      go [directional]
      get [item]
    ''')

def showStatus():
    #print the players current status
    print('----------------------')
    print('You are in the ' + currentRoom)
    #print current inventory
    print('Inventory : '+  str(inventory))
    #print item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print('-----------------------')

#an inventory initially empty
inventory = []

#a dictionary link a room to other rooms
rooms = {'Hall':{'south':'Kitchen', 'east':'Dining Room', 'item':'key'}, 'Kitchen':{'north':'Hall', 'item':'monster'}, 'Dining Room':{'west':'Hall','south':'Garden', 'item':'potion'}, 'Garden': {'north':'Dining Room'}}

#staert the player in the hall
currentRoom = 'Hall'

showInstructions();
#loop forver while true

while True:
    showStatus()
#get the players next move
#.split() breaks it up into a list array
#eg typing 'go east' would give the list:
#['go', 'east']
    move = ''
    while move == '':
        move = input('>')

    move = move.lower().split()

#if they type go first
    if move[0] == 'go':
    #check that they are allowed where the want to go
        if move[1] in rooms[currentRoom]:
        #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
    #there is no door to the new room
        else:
            print('You can\'t go that way!')

#if the type 'get' first
    if move[0] == 'get':
    #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #add the item to their inventory
            inventory += [move[1]]
        #display a helpful message
            print(move[1] + ' got!')
        #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
        else:
        #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
    #if a player enter a room with a monster
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you...  GAME OVER!')
        break
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion...  YOU WIN!!!!')
        break

