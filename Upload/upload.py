from pydrive.drive import GoogleDrive

def upload(gauth):
	drive = GoogleDrive(gauth)
	#file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
	#file1.SetContentString('Hello World!') # Set content of the file from given string.
	#file1.Upload()
	file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
	for file1 in file_list:
		print('title: %s, id: %s' % (file1['title'], file1['id']))
