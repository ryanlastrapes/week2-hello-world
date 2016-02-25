# Ryan Lastrapes

# write a program that:
# 1. greets the user in English
# 2. asks the user to choose from 1 of 3 spoken languages (pick your favorite languages!) 
# 3. displays the greeting in the chosen language
# 4. exits

# make sure that your code contains comments explaining your logic!

while True:
	print('Hello world! Please enter Spanish, French, or Italian')
	language = input()
	if language == 'Spanish':
		print('Hola!')
		break
	if language == 'French':
		print('Bonjour!')
		break
	if language == 'Italian':
		print('Ciao!')
		break