from pydrive.auth import GoogleAuth
import upload

from upload import upload
#import os

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
		
upload(gauth)
