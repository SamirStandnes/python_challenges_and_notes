
import os
from pydrive.drive import GoogleDrive 
from file_content import file_content

def upload_handler(gauth, os_folder_path, gdrive_root_folder_id):
	path = os_folder_path
	
	folder_id = gdrive_root_folder_id
	
	drive = GoogleDrive(gauth)

	folder_num = 0

	for dirpath, dirnames, files in os.walk(path):
		folder_num += 1


		print(os.path.isdir(dirpath))


#		print('Found directory: {dirpath}, {folder_num}'.format(dirpath=dirpath, folder_num=folder_num))
		for file_name in files:

			print(dirpath, file_name, files)

/Users/samir/Desktop/sync notes/attachments
/Users/samir/Desktop/sync notes/notes

#			print("{file_name} found file in {folder_num}".format(file_name=file_name, folder_num=folder_num)) 
"""
			#print(dirpath+file_name)
			new_file = drive.CreateFile({'title': file_name, "parents": [{"kind": "drive#fileLink", "id": folder_id}]})  # Create GoogleDriveFile instance to parentID.
			new_file.SetContentFile(path+dirnames+file_name) # Set content of the file from given string.
			print(new_file)
			new_file.Upload()
"""
""" 
with os.scandir(path) as items:
	for item in items:
		if item.is_dir():
			print(item.name, " is a directorry")

			with os.scandir(path+'/'+item.name) as sub_items:
				for sub_item in sub_items:
					if sub_item.is_dir():
						print(sub_item, "is a sub_directorry")
					else:
						print(sub_item, "is a sub_file")
		elif item.is_file():
			print(item.name, " is a file")

		else:
			print(item.name, " is unknown")


#files = os.scandir(path)

folder_ids = {


	
}

file_ids = {

'boostnote.json': '1s1ryVA7TnMWaC6J7Y44pTetvl12QldO_'

	
}








"""