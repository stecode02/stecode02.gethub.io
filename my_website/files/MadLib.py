from __future__ import print_function

import time
import winsound

def playmusic():
    winsound.PlaySound("C:\\bgm.wav", winsound.SND_ASYNC)

def stopmusic():
    winsound.PlaySound(None, winsound.SND_ASYNC)

def clear():
	for x in range(0,50):
		print (" ")
	time.sleep(1)

def type(storystring):
	for letter in storystring:
		print (letter, end="")
		time.sleep(.05)
	print(" ")
	print(" ")
	time.sleep (1)

def madlibs():
    #Program will return a story based on user's input
    print ("Type in an adjective: ")
    adj1 = raw_input()
    print ("Type in a noun: ")
    noun1 = raw_input()
    print ("Type in a plural noun: ")
    noun2 = raw_input()
    print ("Type in an adjective: ")
    adj2 = raw_input()
    print ("Type in yet another adjective!: ")
    adj3 = raw_input()
    print ("Type in a verb ending in -ing: ")
    verb1 = raw_input()
    print ("Type in another verb ending in -ing: ")
    verb2 = raw_input()
    print ("Type in an adjective: ")
    adj4 = raw_input()
    print ("Type in another adjective: ")
    adj5 = raw_input()
    print ("Type in a noun: ")
    noun4 = raw_input()
    print ("Type in a food, plural: ")
    food1 = raw_input()
    print ("Type in a body type, plural: ")
    body = raw_input()
    print ("Type in an adjective: ")
    adj6 = raw_input()
    print ("Type in the name of a vehicle: ")
    vehicle = raw_input()
    print ("Type in a food, plural: ")
    food2 = raw_input()
    print ("Type in another food, plural: ")
    food3 = raw_input()
    print ("Type in an animal, plural: ")
    animal1 = raw_input()
    print ("Type in another animal, plural: ")
    animal2 = raw_input()
    print ("Type in an adverb: ")
    adv = raw_input()
    print ("Type in a singular noun: ")
    noun3 = raw_input()
    playmusic()
    type(''.join(["If you go to some ", adj1, " place like Yellowstone National ", noun1, ", you must deal with wild animals, such as bears, wolves, and ", noun2, "."]))   
    type(''.join(["The most important of these is the bear. There are three kinds of bears; the grizzly bear, the ", adj2, " bear, and the ", adj3, " bear."]))
    type(''.join(["Bears spend most of their time ", verb1, " or ", verb2, "."]))
    type(''.join(["They look very ", adj4, ", but if you make them ", adj5, ", they might bite your ", noun4, "."]))
    type(''.join(["Bears will come up to your car and beg for ", food1,"."]))
    type(''.join(["They will stand on their hind legs and clap their ", body, " together and pretend to be ", adj6, "."]))
    type(''.join(["But do not get out of your ", vehicle, " or off of the bear's ", food2, " or ", food3, "."]))
    type(''.join(["This same advice applies to other wild creatures such as ", animal1, " and ", animal2, "."]))
    type(''.join(["Remember all these rules and you will spend your vacation ", adv, " and not get eaten by a/an ", noun3, "."]))
    stopmusic()
    
madlibs()