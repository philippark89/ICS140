degree = input("Enter degree: ")
programming_experience = int(input('Enter years of programming experience: '))
other_it_experience = int(input("Enter years of other IT experience: "))
game_programming = input("Does the applicant have at least one year of experience in game programming? Answer y or Y ")

if ((game_programming == 'y' or game_programming == 'Y') and \
    degree == 'AS' and programming_experience + other_it_experience >= 10) and programming_experience >= 5 or \
    (game_programming == 'y' or game_programming == 'Y') and \
    degree == 'BS' and programming_experience + other_it_experience >= 5 and programming_experience >= 3 or \
    (game_programming == 'y' or game_programming == 'Y') and \
    degree == 'MS' and programming_experience + other_it_experience >= 3 and programming_experience >= 2:
	print('The applicant is qualified')
else:
	print('The applicant is not qualified')
