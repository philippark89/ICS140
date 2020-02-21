EXIT = 0
ADD_MEMBER = 1
DEL_MEMBER = 2
ADD_BOOK = 3
DEL_BOOK = 4
FIND_BOOK = 5
ISSUE_BOOK = 6
RETURN_BOOK = 7
LIST_MEMBER = 8
LIST_BOOK = 9
HELP = 10

def add_member(member): # member = list
	name = input('Enter the member name to add: ')
	member.append(name)

def del_member(member):
	name = input('Enter the member name to delete: ')
	if name in member:
		member.remove(name)
	else:
		print('member is not found.')

def add_book(book):
	name = input('Enter the book name to add: ')
	book.append(name)

def del_book(book):
	name = input('Enter the book name to delete: ')
	if name in book:
		book.remove(name)
	else:
		print('book is not found.')

def find_book(book, borrowed):
	name = input('Enter the book name to search: ')
	if name in book:
		pass
	else:
		print('Book is not found.')

def issue_book(book, borrowed):
	name = input('Enter the book name to borrow')
	if name in book:
		pass	
	else:
		print('Book is not found.')

def return_book(book, borrowed):
	pass

def list_member(member):
	print('\nCurrent member list:')
	for i in member:
		print(i)
	print()

def list_book(book):
	print('\nCurrent available book list:')
	for i in book:
		print(i)
	print()

def command_help():
	print()
	print(ADD_MEMBER, 'to add a member')
	print(DEL_MEMBER, 'to delete a member')
	print(ADD_BOOK, 'to add a book')
	print(DEL_BOOK, 'to delete a book')
	print(FIND_BOOK, 'to search the book')
	print(ISSUE_BOOK, 'to borrow the book')
	print(RETURN_BOOK, 'to return the book')
	print(LIST_MEMBER, 'print the current members')
	print(LIST_BOOK, 'print the current available books')
	print(EXIT, 'to exit\n')

def main():
	members = []
	books = []
	borrowed = {}

	select = int(input('Select the menu 0 ~ 10 (help: 0): '))

	while select != EXIT:
		if select == ADD_MEMBER:
			add_member(members)
		elif select == DEL_MEMBER:
			del_member(members)
		elif select == ADD_BOOK:
			add_book(books)
		elif select == DEL_BOOK:
			del_book(books)
		elif select == FIND_BOOK:
			find_book(books)
		elif select == ISSUE_BOOK:
			issue_book()
		elif select == RETURN_BOOK:
			return_book()
		elif select == LIST_MEMBER:
			list_member(members)
		elif select == LIST_BOOK:
			list_book(books)
		elif select == HELP:
			command_help()

		select = int(input('Select the menu 0 ~ 10 (help: 0): '))


main()