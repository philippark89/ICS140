# Auuhor: Taeju Park
# menu constants
EXIT = 0
ADD_EMPLOYEE = 1
ADD_PROJECT = 2
ASIGN_PROJECT = 3
UNASIGN_PROJECT = 4
REMOVE_EMPLOYEE = 5
REMOVE_PROJECT = 6
LIST_EMPLOYEE = 7
LIST_PROJECT = 8
LIST_PROJECT_TEAMS = 9
PRINT_MENU = 10

# functions
def add_employee(name):				# 1
	# to add an employee.
	employee = input('Enter employee name: ')
	name.append(employee)
	print(employee, 'added as an employee')

def add_project(name):				# 2
	# to add a project.
	project = input('Enter project name: ')
	name.append(project)
	print(project, 'added as a project')

def asign_project(name, project, group):	# 3
	# to assign an employee to a project.
	# Assign only if the employee and the project exist.
	employee = input('Enter employee name: ')
	if employee in name:
		project_name = input('Enter project name: ')
		if project_name in project:
			if project_name not in group:
				group[project_name] = [employee]
			elif employee in group[project_name]:
				print(employee, 'is already assigned in project', \
					project_name)
			else:
				group[project_name].append(employee)
				print(employee, 'assigned to project', project_name)
		else:
			print('Project', project_name, 'not found')
	else:
		print('Employee', employee, 'not found')

def unasign_project(name, project, group):	# 4
	# to unassign an employee from his/her project.
	# Unassign only if the employee exists and is assigned to a project.
	employee = input('Enter employee name: ')
	if employee in name:
		existChecking = True
		for key, value in group.items():
			if employee in group[key]:
				group[key].remove(employee)
				print('Employee', employee, 'unassign from project', key)
				existChecking = False
		if existChecking:
			print('Employee', employee, 'is not in any projects yet')
	else:
		print('Employee', employee, 'not found')
	

def remove_employee(name, project, group):	# 5
	# to remove an employee.
	# Remove only if the employee exist and is not assigned to a project.
	employee = input('Enter employee name: ')
	if employee in name:
		existChecking = True
		for key, value in group.items():
			if employee in group[key]:
				print("Can't remove. Employee assigned to project", key)
				existChecking = False
		if existChecking:
			name.remove(employee)
			print('Employee', employee, 'removed')
	else:
		print('Employee', employee, 'not found')


def remove_project(project, group):			# 6
	# to remove a project.
	# Remove only if the project exists. 
	project_name = input('Enter project name: ')
	if project_name in project:
		project.remove(project_name)
		if project_name in group:
			del group[project_name]
		print('Project', project_name, 'removed')
	else:
		print('Project', project_name,' not found')


def list_employee(list):			# 7
	# to list employee
	if list == []:
		print('No employees added')
	else:
		print('Employee list')
		for i in list:
			print(i)

def list_project(list):				# 8
	# to list project
	if list == []:
		print('No projects added')
	else:
		print('Project list')
		for i in list:
			print(i)	

def list_project_teams(dict):		# 9
	# to list all project teams
	if dict == {}:
		print('No projects assigned yet')
	else:
		print('Project assigned list')
		for i in dict:
			print(i, 'members: ', end = '')
			for i in dict[i]:
				print(i, end = ' ')
			print()

def print_menu():					# 10
	# to print the menu
	print(ADD_EMPLOYEE, 'to add an employee')
	print(ADD_PROJECT, 'to add a project')
	print(ASIGN_PROJECT, 'to assign an employee to a project')
	print(UNASIGN_PROJECT, 'to unassign an employee from a project')
	print(REMOVE_EMPLOYEE, 'to remove an employee')
	print(REMOVE_PROJECT, 'to remove a project')
	print(LIST_EMPLOYEE, 'to list employees')
	print(LIST_PROJECT, 'to list projects')
	print(LIST_PROJECT_TEAMS, 'to list all project teams')
	print(PRINT_MENU, 'to print the mneu')
	print(EXIT, 'to exit')

def main():
	employee_names = []
	project_names = []
	asigned_projects = {}

	command = int(input('Enter command; 10 for help '))
	while command != EXIT:
		if command == ADD_EMPLOYEE:			# 1
			add_employee(employee_names)
		elif command == ADD_PROJECT:		# 2
			add_project(project_names)
		elif command == ASIGN_PROJECT:		# 3
			asign_project(employee_names, project_names, asigned_projects)
		elif command == UNASIGN_PROJECT:	# 4
			unasign_project(employee_names, project_names, asigned_projects)
		elif command == REMOVE_EMPLOYEE:	# 5
			remove_employee(employee_names, project_names ,asigned_projects)
		elif command == REMOVE_PROJECT:		# 6
			remove_project(project_names, asigned_projects)
		elif command == LIST_EMPLOYEE:		# 7
			list_employee(employee_names)
		elif command == LIST_PROJECT:		# 8
			list_project(project_names)
		elif command == LIST_PROJECT_TEAMS:	# 9
			list_project_teams(asigned_projects)
		elif command == PRINT_MENU:			# 10
			print_menu()

		command = int(input('Enter command; 10 for help: '))

main()
