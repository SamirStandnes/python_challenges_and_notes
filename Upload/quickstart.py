from pydrive.auth import GoogleAuth
from upload import upload

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

upload(gauth)
