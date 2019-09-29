
def file_content(file_path):
	with open(file_path) as file:
		print(file.read())
		return str(file.read())


#file_content('/Users/samir/desktop/sync notes/boostnote.json')
