#Text Based Zombie Game
#Created by Matthew Dievendorf 4/18/19

#4 rooms - Object is to make it to "The End Room"
#version 1.0.2

import pygame
import time
import random
from sys import exit

       

#win= pygame.display.set_mode((win_length, win_height))

def dead(why):
    print(why, 'Good Job!!!!')
    time.sleep(6)
    exit(0)        

def Room_1():
    print('You find a room full of weapons.')
    print('which weapon will you choose. 1-Machete, 2-Gun')
    room_exit = False

    while True:
        choice = input('>')

        if choice == '1':
            print('fine choice you can now do more damage')
            room_exit = True
            Hallway()
            time.sleep(3)
        elif choice == '2':
            print('Good choice!')
            room_exit = True
            time.sleep(3)
            Hallway()
            
def Room_2():
    print('You enter the room and see a lifeless body on the ground being eaten by a flesh crazed maniac. The fear finally set''s in and you realize...')
    time.sleep(2)
    print('Their all ZOMBIES!!!!')
    time.sleep(2)
    print('The Zombies smell you and run vigurously at you!')
    print('What do you do.. A- attack and try to survice the hoard? or B- Flee for your life and hope you survive!?')
    room_exit = False

    while True:
        choice = input('>')

        if choice =='A':
            print('You grab your weapon and head forth into the hoard, destined to become the true survivor!')
            room_exit = True
            time.sleep(3)
            Hallway()
        elif choice == 'a':
            dead('Wrong input.. The Zombies attack you with full force ripping you limb from limb')
        elif choice == 'b':
            dead('Wrong input.. The Zombies attack you with full force ripping you limb from limb')
        elif choice == 'B':
            print('You run out the room and close the door as hard as you can. Narowly escaping with your life! ')  
            room_exit = True
            time.sleep(2)
            Hallway()

def Room_3():
    print(' You enter a room filled with what once were humans. Now eyes are glaring at you with a conscious set to kill.')
    print('Nostrills flared and eyebrows parallel.')
    print('They sniff the air and can tell your fresh meat to them. They start their position and start twords you!')
    print('What do you do.. A- attack and try to survice the hoard? or B- Flee for your life and hope you survive!?')
    room_exit = False

    while True:
        choice = input('>')

        if choice =='A':
            print('You grab your weapon and head forth into the hoard, destined to become the true survivor!')
            room_exit = True
            time.sleep(3)
            Hallway()
        elif choice == 'a':
            dead('Wrong input.. The Zombies attack you with full force ripping you limb from limb')
        elif choice == 'b':
            dead('Wrong input.. The Zombies attack you with full force ripping you limb from limb')
        elif choice == 'B':
            print('You run out the room and close the door as hard as you can. Narowly escaping with your life! ')  
            room_exit = True
            time.sleep(2)
            Hallway()
                  

def Room_4():
    print('You open the door and realize it goes outside. You made it to the end!')
    time.sleep(1)
    print('As you head outside you can see through the hotel windows, the walking unmentionable horror run from room to room looking for their next feast.')
    time.sleep(5)
    print('Outside, its no different you can make out bodies by the pool and blood strewen everywhere')
    print('The horror is not contained to just the inside of the hotel.')
    time.sleep(4)
    print('You made it out alive, Congratulations there. However, now you must set your game plan for real survival in this new world!')
    exit(0)


def Hallway():
    time.sleep(2)
    print('In the Dark and forboding hallway you hear screams and 4 doors!')
    time.sleep(2)
    print('which door do you choose?')
    print('1, 2, 3, or 4')
    time.sleep(2)

    choice2 = input('>')

    if choice2 == '1':
        Room_1()
    elif choice2 =='2':    
        Room_2()
    elif choice2 == '3':    
        Room_3()
    elif choice2 == '4': 
        Room_4()
    else:
        dead('Stay in your room and Zombies crash through your door... eat you alive because your dumb...')
    
    time.sleep(3)    




class start():
#    pygame.init()
#screen = pygame.display.set_mode((800,900))
#done = False

#while not done:
 #   for event in pygame.event.get():
  #      if event.type == pygame.QUIT:
   #         done = True
            
   # pygame.display.flip() 
    
    print('***************************************')
    print('Welcome to the Zombie Hotel')
    print('***************************************')
    time.sleep(4)
    print('After a night out you crash at a hotel near by. Drunk from the night before. The screams from outside your door awaken you abruptly!')
    time.sleep(6)
    print('You wake up in a dim lit room wondering what happened, where are you?, who is that with the blood curdaling screems!')
    time.sleep(5)
    print('you see your door cracked slightly and open it slowly.')
    time.sleep(5)
    print('You open your door and see a dark hallway, you hear screams coming from one of the 4 doors you see.')
    print('Only one door will let you out and let you live.')
    Hallway()
    
start()

 