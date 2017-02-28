PLEASE PULL LASTEST CODE BEFORE PUSH
====================================

Requirements to Run Project
---------------------------
1.Python installed
2.Django installed (Intall Pip first!)

Installing Python and Pip
-------------------------
/* Pip is used to easily install Django onto your machine. 
get-pip.py file located in our repo in the folder named "Pip Install". */

If you are using Windows:
	Please refer to this link: https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation
	
If you are using mac (using Homebrew):
	type into Mac's cmd line: 
	
		1. brew install python
		
		2. python -V
		
		3. sudo pip install --upgrade pip
		
		4. pip -V

This will allow for python and pip to be run off your systems cmd line.

Installing Django
-----------------
/* REQUIRED: pip installed */

Type into cmd line: pip install django 
You can check to see if you have it installed by typing this into the cmd line: django-admin.py version

Django Projects
---------------
COMMON COMMANDS: python manage.py ___________

Running Project
---------------
1.To run the project, go INTO the "snake_pit" folder

2.You must first kick up the server by typing into the cmd line: python manage.py runserver

3.This should output something like this

	System check identified no issues (0 silenced).
	February 28, 2017 - 08:02:50
	Django version 1.10.5, using settings 'snake_pit.settings'
	Starting development server at http://127.0.0.1:8000/
	Quit the server with CTRL-BREAK.

4.You can now go to your web browser and type into the URL: localhost:(port number)

	//port number can be found on the line "Starting development server at http://?.?.?.?:(port number)/"
	//alternitively you can type this into the cmd line: python manage.py runserver 0.0.0.0:8000 
	//which will set the server port to be 8000 automatically. 

