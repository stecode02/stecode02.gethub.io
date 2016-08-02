#My FIrst Day of School
#Interactive Python
#Larry and Toby



def introduction():  #this function is called in the last line of code
	print "First Day of School"
	print "Welcome to our school. Proceed to the office to obtain your class schedule."
	print "Proceed to first period."
	restroom()

def restroom():
	print ""
	print "You have sudden urge to relieve yourself."
	print "Would you like to go to the restroom or go to class?"
	print "Type r for restroom or type c for class."
	answer = raw_input()
	if answer == "r":		#if statement decides to go to restroom or not
		print "You go to the restroom and you're late to class"
		proceed()
	else:
		print "c"		#else statement decides to go to class
		proceed()
	
def proceed():
	print ""
	print "Proceed to third period."
	print "Proceed to fourth period."
	print "It's lunch time. Would you like McDonald's or cafeteria lunch?"
	print "Type on for cafeteria lunch or type off for McDonald's."
	answer = raw_input()
	if answer == "on":		#if statement decides where to eat 
		print "You're going to cafeteria."
		beatdown()
	else:
		print "Enjoy your happy meal."
		proceed2()		

def beatdown():
	print ""
	print "You get your lunch and sit at a table by yourself."
	print "A group thug looking seniors approach you."
	print "One of them stands next you and says,what you got on my lunch homie?"
	print "You shocked by the ambush, so you stare at them silently."
	print "Do you give them the $2 in your pocket or ignore them and walk away."
	print "Type 2 to give money or type w to walk away."
	answer = raw_input()
	if answer == "2":		#if statement decides to give money or walk away 
		print "You give him your money and he says, thanks homie, we be back tomorrow."
		proceed2()
	else:
		print "You get up and walk away but they catch up to you in the hall,take your $2 and throw you in the trashcan."
		proceed2()

def proceed2():			
	print ""
	print "Proceed to fifth period."
	print "Ring, Ring!! Your phone is ringing and won't stop."
	print "Would you like to answer it or ignore it?"
	print "Type 1 to answer or type 2 to ignore."
	answer = raw_input()
	if answer == "1":		#if statement decides to answer phone or not
		print "Cute girl from first period wants to meet you in the hall."
		print "Everyone in class begins to stare at you."
		ditch()
	else:
		print "You're phone keeps ringing."
		print "Ignore your phone and proceed to sixth period."
		ditch()		

def ditch():	
	print ""
	print "You approach your sixth period class and nobody's there."
	print "Do you want to ditch seventh period and go home?"
	print "Or do you want to go to the office to get the correct room number?"
	print "Type 7 to go to class or type h to go home."
	answer = raw_input()
	if answer == "7":		#if statement decides to ditch or not
		print "Proceed to the office to get the correct room number."
		print "Proceed to seventh period."
		print "Go home."
	else:
		print "Go home."
	
introduction()
