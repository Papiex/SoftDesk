# SoftDesk

SoftDesk is an API that allows you to report and track technical problems for three platforms :
(Websites, iOS, Android).

Authentified users will be able to create projects and in this created project :

- Add contributors
- Create issues and assign labels to these issues according to their priority.
- Add comment

<li><a href="#requirements">Requirements</a></li>
<li><a href="#gitbash">Gitbash</a></li>
<li><a href="#installation-on-windows">Installation on Windows</a></li>
<li><a href="#installation-on-linux">Installation on Linux</a></li>
<li><a href="#installation-on-mac">Installation on Mac</a></li>
<li><a href="#Screenshots">Screenshots</a></li>
<li><a href="#postman-documentation">Postman Documentation</a></li>


## Requirements
```bash
Python 3.9.0
```
## Gitbash
You have to clone the deposit with this command on gitbash :
```
git clone https://github.com/Papiex/SoftDesk
```

## Installation on Windows
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python -m venv env```

__2- Now you have to activate your virtual env, the default path is :__
- if you use PowerShell :
``` env/Scripts/activate.ps1```
- if you use CMD or terminal that supports __.bat__ :
``` env/Scripts/activate.bat```

## Installation on Linux
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Installation on Mac
__1- You need to create virtual env with this command :__

*The virtual env is installed in the directory where you are (the path) with your terminal*

- ```python3 -m venv env```

__2- Now you have to activate your virtual env, the command is :__
``` source env/bin/activate```

## Libraries
__This program need some libraries, for installing them, use this command (in your virtual env) :__

*View requirements.txt to know which library/version is used*

- ```pip3 install -r requirements.txt``` | Windows : ```pip install -r requirements.txt```

## Run the site
__To run the site, after activating your virtual environment
You need to start the server with this commands :__

- ```cd litreview```
- ```python3 manage.py runserver``` | Windows : ```python manage.py runserver```
- Open your browser and go to this url : 127.0.0.1:8000

## Screenshots

## Postman Documentation

Documentation of each endpoints of the API and their utility/fonctionnality is available at this url : 