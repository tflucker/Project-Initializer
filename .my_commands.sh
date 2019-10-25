#!/bin/bash

## used to create new projects locally and sync it with Github account
function create () {

	#installs libraries
	pip install -r requirements.txt

	# change directory to base, so that this can be run anywhere
	cd 
	
	# call python script to create new local folder and create new repo in github
	python create.py $1

	# if there is an error a '1' is returned, if no error then create repository
	if [ $? -eq 1 ];  
	then
		echo 'Path already exists, no repo created.'
	else
		# navigate to the newly created folder, for this example i use the D: drive
		cd d:
		cd Git_Checkouts/$1

		# initialize git repo
		git init
			
		# creates empty README file
		echo "# $1" > README.md

		# add empty README file
		git add .
		
		# commit changes
		git commit -m "Initial commit"

		# adds origin remote, uses parameter as project name
		git remote add origin https://github.com/<username>/$1.git

		# force push changes to new repo
		git push -u origin master
		
		# changes branch to 'develop' so future commits and push create pull requests
		git checkout -b "develop"

		# opens visual studio code at base directory of new project
		code .
	fi

	cd ~
}

# removes repository based on name arguement
function remove() {

	# removes repo in github
	python remove.py $1

	# delete local folder
	cd d:
	rm -rf Git_Checkouts/$1

	cd ~
}