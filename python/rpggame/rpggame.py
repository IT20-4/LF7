import random

def showInstructions():
    # print a main menu and the commands
    print('''
============================
Welcome to your own RPG Game
============================

Get to the garden with a key and a potion

or

get to the laboratory with the book of life and the beam-o-mat.

Avoid the monster!


Commands you can use:
    go [direction]
    get [item]
''')

def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)

    # print the current inventory
    print('Inventory : ' + str(inventory))

    # print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")

# inventory --> empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Hall' : { 
        'south'     : 'Kitchen',
        'east'      : 'Dining Room',
        'west'      : 'Office',
        'item'      : 'Key',
        'enemy'     : ''
    },
    
    'Kitchen' : {
        'north'     : 'Hall',
        'item'      : '',
        'enemy'     : ''
    },

    'Dining Room' : {
        'west'      : 'Hall',
        'south'     : 'Garden',
        'item'      : 'Potion',
        'enemy'     : ''
    },

    'Garden' : {
        'north'     : 'Dining Room',
        'enemy'     : ''
    },

    # more rooms

    'Library' : {
        'east'      : 'Office',
        'item'      : 'Book of Life',
        'enemy'     : ''
    },

    'Office' : {
        'east'      : 'Hall',
        'south'     : 'Laboratory',
        'west'      : 'Library',
        'enemy'     : ''

    },

    'Laboratory' : {
        'north'     : 'Office',
        'item'      : 'Beam-O-Mat',
        'enemy'     : ''
    }

}

# start the player in the Hall
currentRoom = 'Hall'

# random monster location
locationMonster = []

# in which rooms could the monster spawn?
locationMonster = ['Kitchen', 'Dining Room', 'Garden', 'Office', 'Laboratory', 'Library']

random.shuffle(locationMonster)
locationMonster = locationMonster[0]
rooms[locationMonster]['enemy'] = 'Monster'


########################################

# main

########################################

# show instructions at start
showInstructions()

while True:
    # show status
    showStatus()

    # show where to monster spawned --> debug
#    print('The Monster is in the:', locationMonster)

    # get move
    move = ''
    while move == '':
        move = input('>')
#    move = move.lower().split() # split --> items cant be nammed with upper case letters
    move = move.split(' ', 1) # only the first command should be split, so itemnames can have spaces

    # exit
    if move[0] == "exit":
        break

    # go
    if move[0] == 'go':

        # user shouldn't only input "go"
        if len(move) <= 1:
            print("Something is not right here...")

        # movement
        elif move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    # get
    if move[0] == 'get' :
        
        # user shouldn't only input "get"
        if len(move) <= 1:
            print("Something is not right here...")

        # action
        elif 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory += [move[1]]
            print(move[1] + ' got!')
            del rooms[currentRoom]['item']
        else:
            print('Can\'t get ' + move[1] + '!')
    
    # loss
    if 'enemy' in rooms[currentRoom] and 'Monster' in rooms[currentRoom]['enemy']:
        print('A monster has got you... GAME OVER!')
        break

    # win 1
    if currentRoom == 'Garden' and 'Key' in inventory and 'Potion' in inventory:
        print('You escaped the house... YOU WIN!')
        break

    # win 2
    if currentRoom == 'Laboratory' and 'BookOfLife' in inventory and 'Beam-O-Mat' in inventory:
        print('You escaped the house... YOU WIN!')
        break