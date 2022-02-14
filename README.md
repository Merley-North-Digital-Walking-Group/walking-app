
The digital walking app is a group project as part of the TechUP Software Skills Developer Bootcamp.

The aim of the digital walking group is to create a social space online where older residents of the Merley North area can find walking groups. 
By joining a walking group members can find new places to walk and meet new people, helping to reduce loneliness and promote excercise.


Instructions to install and run on local machine:

Prerequisites:
- Python 3
- git


1 - Clone repository from GitHub on your local machine.

2 - Install and activate a python venv.

3 - Install required packages:
```
      $ pip install -r requirements.txt
```

4 - Initialise database:
```
      $ python manage.py migrate
```
5 - Run app on local server:
```
      $ python manage.py runserver
```
