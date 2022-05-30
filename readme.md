<h1 align="center">OpenClassrooms Project 10</h1>

# Create a Secure RESTful API Using Django REST
> This is my tenth project for OpenClassrooms where I had to create a RESTful API using Django REST. The API is for an issue-tracking application for use by companies.


## Table of Contents
* [General Info](#general-information)
* [Prerequisite](#prerequisite)
* [Setup](#setup)


## General Information
- An issue tracking application for all three platforms (Web, Android, and iOS).
- The app would enable users to design different projects, add users to a particular project, create issues in the project, and label these issues as per their priorities, tags, etc.
- All of the three apps will leverage the API endpoints that would serve the data.


## Prerequisite
- [Python 3.10.4](https://www.python.org/ "Python") is installed

## Setup
1. Clone the repository

```Bash
git clone https://github.com/aschickhoff/OCproject10
```

2. Go to your work directory
```Bash
cd OCproject10
```

## for Windows
3. Create a virtual environment
```Bash
python -m venv env
```

4. Activate the virtual environment
```Bash
env\Scripts\activate
```

## for Linux
3. Create a virtual environment
```Bash
python3 -m venv env
```

4. Activate the virtual environment
```Bash
source env/bin/activate 
```

## Packages
5. Install needed packages

```Bash
pip install -r requirements.txt
```

## Start the server

6. Launch the Django server
```Bash
python manage.py runserver
```
