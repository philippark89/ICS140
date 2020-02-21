class_id = ['cs 101', 'cs 201', 'cs 301', 'cs 401']
class_dict = {'cs 101': 4, 'cs 201': 3, 'cs 301': 5, 'cs 401': 4}
TUITION_RATE = 200.0
userInput = input(class_id)

print('You are taking', userInput, 'which is',
      class_dict[userInput], 'credits costing you $',
      class_dict[userInput] * TUITION_RATE)
