import sys
import re

def strong_pass(password):
	#check if there is an upper case
	assert re.match('\w*\s\w*',password) is None #Ensure no spaces!

	#\w -> [a-z][A-Z][0-9] 
	strength = 0
	if re.match(r'\w*[A-Z]\w*', password) is not None: #Capital Letters
		strength += 1
		
	if re.match(r'\w*\d\w*', password) is not None: #digits
		strength += 1

	if re.match(r'\w*[^A-Za-z0-9]\w*', password) is not None: #Special Characters
		strength += 1

	if len(password) > 8:
		strength += 1

	if len(password) > 14: #Very long passwords are good
		strength += 2
	return strength


def main():
	if len(sys.argv) != 2:
		print("Usage: python -m strong_password password")
		sys.exit(0) 
	strength = strong_pass(sys.argv[1])
	if strength == 0:
		print "I'm sorry, that's a very weak password. You should never use it."
	elif strength == 1:
		print "That password is okay, but nothing special. You can improve it."
	elif strength == 2:
		print "That password is MEh but better than okay, you can do better! JUST DO IT"
	elif strength == 3:
		print ":DDDDDDDDDD YAYAYYASJLKFAJSLFKJSLHSKJDLAJD. Sorry was gonna congratulate you but Akshay said it was not good enough (;"
	else:
		print "That password is pretty strong! Well done."



if __name__ == '__main__':
	main()