import sys
import os
from os import path

from github import Github

# Replace with path where you want to save new projects
path = "/Git_Checkouts/"

# Github credentials
username = ""
password = ""

# Users the PyGithub library, no web involved
def create():
	# changes directory to 'D' drive, where i have my checkouts, comment this out if you save in the 'C' drive
	os.chdir("d:")
	
	folderName = str(sys.argv[1])
	
	if os.path.exists(path + folderName):
		print('Path already exists')
		exit(1)
	else:
		os.makedirs(path + str(folderName))
		
	user = Github(username, password).get_user()
	user.create_repo(folderName)
	print("Successfully created repository {}".format(folderName))

if __name__ == "__main__":
	create()