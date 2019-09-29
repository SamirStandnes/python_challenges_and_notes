from pydrive.drive import GoogleDrive 
from delete_items_in_gdrive_folder import delete_items_in_gdrive_folder
from upload_handler import upload_handler
#from pydrive.auth import GoogleAuth
#import upload
#import os
#import os


def upload(gauth):

	#gauth = GoogleAuth()
	#gauth.LocalWebserverAuth()

	drive = GoogleDrive(gauth)
	folder_id = '15vYFyHRd83FZgyfjAJ0XQtl8gm7-3WFy'
	
	print(drive, vars(gauth))

	delete_items_in_gdrive_folder(gauth, folder_id)

	path = '/Users/samir/desktop/sync notes/' # move to top run file

	upload_handler(gauth, path, folder_id)



#upload()	






	




"""
	file1 = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}]})  # Create GoogleDriveFile instance with title 'Hello.txt'.
	file1.SetContentString('Hello World!') # Set content of the file from given string.
	file1.Upload()
	
attachments_id = '1524ZHIYyABnv21xXau-A0hlKaFUd6-kn'


	notes_id = '1GOVpJIV4FyLF38Ab-dS4vPSXsTxV88YT'



"""





	

