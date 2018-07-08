#Imports-----------------------------
import warnings
from time import sleep
#------------------------------------

#-------------------------------------
# Escape Room Program
#-------------------------------------
'''
This program is a simple escape room
It takes a few inputs 'look', 'use'
The goal is to find the key to escape the room
'''

#function to try and escape to room
def escape_room():

  ##These are some things that will never change throughout the game
  hard_ending = '''
  CONGRATULATIONS!!!!!!!

  You have unlocked the door!
  '''
  possible_inventory_items = ['key','axe','complicated puzzle','solved puzzle']
  acceptable_choices = ['search','examine','use','stop']

  ##This is a variety of variables that will be changed throughout the game
  #objects that are removed throughout the game be put here
  removed_objects_list = []
  #starting inventory
  inventory = []
  #what a user can see in the room to begin with
  room_look = ['door','table','bookcase','emergency axe cabinet']
  #all possible searches player can perform
  #The current code needs everything to be 1:1
  search_dict = {
    'door':'lock'
    ,'table':'complicated puzzle'
    ,'suspicious dictionary':'key'
    ,'emergency axe cabinet':'axe'
    ,'bookcase':'suspicious dictionary'
  }
  #The keys in this dictionary should include all possible starting inventory and room_look items
  examine_dict= {
    'table':'A wooden table.  Great for solving puzzles.  It would likely shatter with a little force...I mean...why would that ever happen....'
    ,'door': 'A strudy wooden door.  It has many fine engravings on it\'s surface. Whoever created this must care about it a lot'
    ,'lock':'A shiny iron lock in the door.  It looks very strong.  You will need to find the key to open it!'
    ,'key':'A shiny steel key gilded with stands of gold on its edges.  You found it!  Now open the door!'
    ,'axe':'A fire axe...this isn\'t part of the game.  It\'s only for emergencies...what are you thinking of doing....'
    ,'bookcase':'A sturdy wooden bookcase, contains a bunch of dictionaries...one particular volume looks a little...suspicious...'
    ,'suspicious dictionary':'This dictionary is slightly open and ruffled, like it\'s been used a lot.  Titled \'Volume E\''
    ,'complicated puzzle':'This looks really difficult...you could probably try working on it at the table'
    ,'emergency axe cabinet':'A note says \'ONLY OPEN IN CASE OF EMERGENCY\'....I guess I should leave it alone...'
  }
  first_miss = 0

  door_unlocked = False

  print '''

  ##############################################################
  Welcome to the Escape Room!


  Thank you for testing out my new escape room game!
  Your Mission: Unlock the door!

  If you ever want to stop early just type stop when prompted
  ##############################################################

  '''
  sleep(5)
  print'''
  #####################################################
  Oh! One more thing...

  ...there's an axe in the room...

  It's not part of the game...I haven't gotten around
  to taking it out yet. So just avoid it for now!

  Good luck!
  ######################################################

  '''
  sleep(4)
  #used by sleep function to slow down the game
  t1 = 1
  t2 = 2
  t3 = 3
  print 'Before we start, do you want to speed the game up?'
  print 'Be Careful: Speeding things up will make things really fast!'
  print
  sleep(t2)
  speed_choice = raw_input('Hit enter to keep things normal. To speed up type: yes ')
  print
  if speed_choice == 'yes':
    t1=0
    t2=0
    t3=0
    print 'Ok...things are going to be fast!'
  else:
    print 'OK, we will keep things at normal speed.'
  print
  sleep(t1)
  while door_unlocked == False:
    #this happens every time.
    #It allows the user to see what's in the room and decide what to do
    raw_input('Press enter to look around the room')
    room_look = sorted(room_look)
    sleep(t1)
    print
    print
    print '######################################################'
    print 'You can the see: '
    print
    for i in room_look:
      print ' '+ i
    print
    if len(inventory)>1:
      print 'You are holding: '
      print
      for i in inventory:
        print' '+i
      print
    elif len(inventory)==1:
      if inventory[0][0] in 'aeiou':
        print
        print 'You are holding an ' + ''.join(inventory)
      else:
        print 'You are holding a ' + ''.join(inventory)
      print
    else:
      print 'You aren\'t holding anything'
      print
    if first_miss == 1:
      print
      print 'Your options are: '+'/'.join(acceptable_choices)
    choice = raw_input('What do you want to do? ')
    sleep(t1)
    print '######################################################'

    #wrong choice creates an error and restarts the loop
    if choice not in acceptable_choices:
      print
      sleep(t1)
      if first_miss == 0:
        first_miss +=1
        print'''
###############################################
Oh! I forgot to mention...
You can only: %s
My bad! Try again!

*hint* try search
##############################################
        '''%('/'.join(acceptable_choices))
        sleep(t1)
      elif first_miss==1:
        print'''
###############################################
Remember!
You can only: %s
Try again!
##############################################
        ''' %('/'.join(acceptable_choices))
        sleep(t1)
    #user decides to end the loop
    #this stops the game
    elif choice == 'stop':
      print
      sleep(t1)
      print 'Ok ok...I\'ll unlock the door for you'
      sleep(t3)
      print
      door_unlocked = True
      print 'The lock turns...'
      sleep(t2)
      print '''
      The door is unlocked
      You made it out the easy way
      '''

    #user searches
    elif choice == 'search':
      print
      print 'You can see the following: '
      print  ' '
      for i in room_look:
        print' '+i
      print
      search_choice = raw_input('What do you want to search? ')
      print
      sleep(t1)
      print 'You search the '+search_choice
      print
      sleep(t2)
      if search_choice not in room_look:
        print 'You don\'t see that'
        print
      else:
        if search_choice not in search_dict.keys() or search_dict[search_choice] in removed_objects_list or search_dict[search_choice] in room_look:
          print 'You don\'t find anything new'
          print
        else:
          discovery = search_dict[search_choice]
          if discovery[0] in 'aeiou':
            print 'You find an ' + discovery
            print
          else:
            print 'You find a ' + discovery
          print
          sleep(t1)
          room_look.append(discovery)
          if discovery in possible_inventory_items:
            inventory.append(discovery)
            print 'You pick up the ' + discovery
            print
            sleep(t2)

    #user examines
    elif choice == 'examine':
      print
      print 'You can see the following: '
      print
      for i in room_look:
        print' '+i
      print
      examine_choice = raw_input('What would you like to examine? ')
      print
      print 'You take a moment to examine the '+examine_choice
      print
      sleep(t2)
      if examine_choice not in room_look:
        print 'You couldn\'t find that'
        print
      else:
        ' '
        print
        sleep(t1)
        print examine_dict[examine_choice]
        sleep(t2)
        print

    #user chooses to use something
    elif choice == 'use':
      print
      if len(inventory) == 0:
        print 'You aren\'t holding anything'
        print
        sleep(t1)
      else:
        if len(inventory)==1:
          print 'You are holding: ' + ''.join(inventory)
          print
          sleep(t1)
        else:
          print 'You are holding: '
          print
          for i in inventory:
            print' '+i
          print
          sleep(t1)
        inv_choice = raw_input('What would you like to use? ')
        print
        if inv_choice not in inventory:
          print 'Sorry, you don\'t have that available to use'
          print
          sleep(t1)
        else:
          print
          print 'You can see the following: '
          print
          for i in room_look:
            print' '+i
          print
          sleep(t1)
          use_choice = raw_input('What would you like to use the ' + inv_choice + ' on? ')
          if use_choice not in room_look:
            print 'Sorry, you don\'t see that'
            print
          else:

            ##these are ALL the different ways objects can be used along with their consequences

            #wins the game
            if inv_choice == 'key' and use_choice == 'lock':
              door_unlocked = True
              sleep(t2)
              print
              print 'You insert the key into the lock...'
              print
              sleep(t3)
              print 'The lock turns...'
              sleep(t2)
              print
              print hard_ending


            #'normal' escape room things
            elif inv_choice == 'complicated puzzle' and use_choice == 'table':
              print
              room_look.remove('complicated puzzle')
              inventory.remove('complicated puzzle')
              removed_objects_list.append('complicated puzzle')
              room_look.append('solved puzzle')
              inventory.append('solved puzzle')
              examine_dict['solved puzzle'] = 'After working on the puzzle for almost an hour...you finally solve it! It says you need to \'define Escape\'...'
              print examine_dict['solved puzzle']
              print
              sleep(t1)
              print 'You now have a solved puzzle'
              print
            elif inv_choice == 'axe' and use_choice == 'emergency axe cabinet':
              print
              print 'You gently place the axe back in the cabinet'
              print
              sleep(t1)
              print 'That\'s probably for the best..what were you going to use it on anyway..the door?'
              print
              sleep(t1)
              search_dict['emergency axe cabinet']='axe'
              inventory.remove('axe')
              room_look.remove('axe')

            #unusal situations I'm providing some text for
            elif inv_choice == use_choice:
              print
              print 'Using the %s on itself....creative...but not effective' %(inv_choice)
              print
              sleep(t1)
            elif inv_choice == 'key' and use_choice in ['door','damaged door','severely damaged door']:
              print
              print 'Hm...maybe if you searched the door you might find a lock?'
              print
              sleep(t1)
            elif inv_choice == 'complicated puzzle' and use_choice != 'table':
              print
              print 'Trying using the puzzles at the table'
              print
              sleep(t1)
            elif inv_choice == 'complicated puzzle' and use_choice == 'table remains':
              print
              print 'The table has been destroyed...you won\'t be able to work on the puzzle now'
              print
              sleep(t1)
            elif inv_choice == 'solved puzzle' and use_choice == 'table':
              print
              print 'There is no more work to do on the puzzle...it says you need to find a dictionary for the word \'Escape\''
              print
              sleep(t2)

            #axe 'trying' to destroy things
            #needs to be ontop of the axe destroying things section
            elif inv_choice == 'axe' and use_choice in ['lock','key']:
              print
              print 'The axe doesn\'t make a dent in the strong '+ use_choice
              print
              sleep(t1)
              print '...I guess you could always try using the axe on something else...wait...hold on...'
              print
              sleep(t1)

            #axe destroying things
            elif inv_choice == 'axe' and use_choice == 'table':
              print
              print 'You have successfully...destroyed the table...and anything that was on it'
              print
              sleep(t1)
              room_look.remove('table')
              removed_objects_list.append('table')
              room_look.append('table remains')
              examine_dict['table remains'] = 'The table is just a pile of wood now...'
              print
              print 'You can now see the remains of the table...'
              print
            elif inv_choice == 'axe' and use_choice == 'bookcase':
              print
              print 'You have successfully...destroyed the bookcase'
              sleep(t1)
              room_look.remove('bookcase')
              removed_objects_list.append('bookcase')
              room_look.append('bookcase remains')
              examine_dict['bookcase remains'] = 'The bookcase is in now in pieces...with most of the books destroyed...'
              search_dict['bookcase remains'] = 'suspicious dictionary'
              print
              print 'You can now see the remains of the bookcase...'
              print
              sleep(t1)
            elif inv_choice == 'axe' and use_choice == 'suspicious dictionary':
              print
              print 'You have successfully...destroyed the suspicious looking dictionary'
              print
              sleep(t1)
              room_look.remove('suspicious dictionary')
              removed_objects_list.append('suspicious dictionary')
              if search_dict[use_choice] not in inventory:
                room_look.append(search_dict[use_choice])
                print
                print 'You have found the '+ search_dict[use_choice]
                print
                sleep(t1)
                inventory.append(search_dict[use_choice])
                print 'You have picked up the ' + search_dict[use_choice]
                print
                sleep(t1)
              print 'The suspicious dictionary has been completely destroyed...'
              print


            #the axe destroying the door - alternate ending
            elif inv_choice == 'axe' and use_choice == 'door':
              print
              print 'The door is damaged'
              sleep(t1)
              print
              print'''

###################################################################
Woah...are you using the axe on the door? Escape rooms have
rules you know...they have structure...you can't just go
around hacking through an escape room with an axe...
Now...why don't we put down the axe and go back to solving puzzles?
###################################################################

              '''
              room_look.remove('door')
              removed_objects_list.append('door')
              room_look.append('damaged door')
              examine_dict['damaged door'] = 'This door has a massive hole where the axe had landed...'
              search_dict['damaged door'] = 'lock'
            elif inv_choice == 'axe' and use_choice == 'damaged door':
              print 'The door is REALLY damaged'
              sleep(t1)
              print
              print'''

##############################################################
Ok look, I'm not supposed to do this but....
the key is in the dictionary on the bookshelf, ok...just...
just put away the axe, get the key, and we can forget ALL
about this whole 'destroying the door with an axe' business
##############################################################

                '''
              room_look.remove('damaged door')
              removed_objects_list.append('damaged door')
              room_look.append('severely damaged door')
              examine_dict['severely damaged door'] = 'What is left of this door...if one could still consider it a door...is damaged beyond repair'
              search_dict['severely damaged door'] = 'lock'
            elif inv_choice == 'axe' and use_choice == 'severely damaged door':
              door_unlocked = True
              sleep(t1)
              print '''
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Despite the futile pleas from the game developer, you continue to swing the axe at the door
Hacking at the last remaining planks of wood, only but a few still impetuously stand before you...
Every stroke is a celebration of your intentional subversion...circumventing the structure of the game
With one final strike, what little is left of the door finally crumbles before your will

...you have won!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                '''
              sleep(t1)
              print
              finalmessage = ''
              finalmessage = raw_input('What do you say once the door finally falls? ')
              sleep(t1)
              print
              if finalmessage == '':
                print 'Nothing more needs to be said...you have won'
              else:
                print 'With a triumphant grin you declare: \'' + finalmessage +'\''
              print
              sleep(t2)
              print '...well...you were technically supposed to UNLOCK the door...'
              print
              sleep(t1)
              print 'but...ya...sure...ya that works...'
              print
              sleep(t1)
              print hard_ending

            #axe destroying anything else
            #needs to be on bottom
            elif inv_choice == 'axe' and use_choice in room_look:
              print
              room_look.remove(use_choice)
              if use_choice in inventory:
                inventory.remove(use_choice)
              removed_objects_list.append(use_choice)
              print 'You have successfully...destroyed the ' + use_choice
              print
              sleep(t1)
              print 'The '+ use_choice + 'is completely destroyed'
              sleep(t1)
              print 'I hope you didn\'t need that'
              print
              sleep(t2)

            #anything else done gets the generic text
            else:
              print
              print 'That doesn\'t seem to do anything'
              print
              sleep(t1)

escape_room()
