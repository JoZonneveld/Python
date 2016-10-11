#password_check

user_pass = (input('please enter a password: '))
length = len(user_pass)
weak = '[!]your password is too damn weak'
medium = '[!]your password is meduim'
strong = '[!]your password is strong'
lower_case = True
upper_case = True
sym        = True
nummer     = True

#heb de functie weg gehaald, de functie zorgde ervoor dat hij niet werkte, dit is volgens mij ook een betere manier inplaats van de functie
for i in user_pass:
	o = ord(i)
	if o >=97 and o <=122:
		lower_case = False
	elif o >=65 and o <=90:
		upper_case = False
	elif o >=33 and o <=47:
		sym = False
	elif o >=48 and o <=57:
		nummer = False

def password_length_check(user_pass):
	length = len(user_pass)
	if length > 20 or length < 8 :
		print('password is too long or too short')
		print('your password has {0} characters.'.format(length))
	else:
		print('password length passed.')

password_length_check(user_pass)
''' Je kan deze punten telling gebruiken bijvoorbeeld
punten = 0
if lower_case == False:
	punten += 1
if upper_case == False:
	punten += 1
if sym == False:
	punten += 1
if nummer == False:
	punten += 1
'''
def error_message(user_pass):
	if  lower_case == True and upper_case == True and sym == True and nummer == True:
		print(weak + ',try adding  more num, sym, cptals and lower characters for a strong password')
	elif lower_case and upper_case and sym == True:
		print(medium + ',you miss a number for an strong password')
	elif lower_case and upper_case and sym and nummer == False:
		print(strong)
error_message(user_pass)
