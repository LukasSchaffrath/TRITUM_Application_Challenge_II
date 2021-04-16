A website that visualizes data by retrieving it from sqlite database.

NOTE:

Ensure that python 3.7.9, pip and django 3.1.7 is installed on your machine.

HOW DOES IT WORK?

Navigate to the folder where the manage.py file is located using terminal.
Afterwards type command: python manage.py runserver and visit http://127.0.0.1:8000/ 

You may access the sqlite database by first creating a superuser by using the following command:
python manage.py createsuperuser

After successfully creating the superuser, navigate to the folder where the manage.py file is located
and then run: python manage.py runserver

Navigate to  http://127.0.0.1:8000/admin and enter your credentials, you'll see a table named data where the data has been stored.
