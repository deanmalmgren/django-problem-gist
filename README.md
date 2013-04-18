This is a simple gist to illustrate the peculiar behavior with django 1.5 and DEBUG=False when running locally (and in production?...haven't gotten that far yet).

To see the problem in action, make sure you have django 1.5.1 installed and run the following commands:

cd project/
python manage.py runserver
google-chrome http://localhost:8000

STRANGE!!!
