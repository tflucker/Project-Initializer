# Project-Initializer 
 
This project creates a new shell command that is usable from Git Bash. You can call it like this:
	`create "<project_name>"`

You can also delete a project by running the command: `remove "<project_name>"
** Using this command will also delete its folder on your computer as well **

## Installation instructions: 

1. Clone this project into a directory on your computer
2. cd into newly cloned project
3. Run this command: `pip install -r requirements.txt`
 - if you have issues with this you may need to download pip
4. Run this command: source ~/.my_commands.sh
5. Open the create.py, remove.py, and .my_commands.sh files and replace the Github user credentials and the path where you want your projects.

## Troubleshooting

- If you have issues with this, try to run the commands in the '.my_commands.sh' manually to see if that is the issue. 

- If you plan on saving your files in the C: drive, then delete instance where i mention the D: drive. 

- if you accidentally create a git repo in a location you didn't mean to, run this command to undo the git init command: `rm -rf .git`

- if you are having issues related to the chromedriver, then download it and add its location in the PATH environment variable
