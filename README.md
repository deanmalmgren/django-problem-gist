This is a simple gist to illustrate the peculiar behavior reported in
this
[SO post](http://stackoverflow.com/questions/16084688/variables-included-in-template-context-processors-not-in-template-with-debug-fal)
with django 1.5 and `DEBUG=False` when running locally. Not sure if
this behavior exists in production.

To see the problem in action, make sure you have django 1.5.1
installed and run the following commands:

    virtualenv --no-site-packages --setuptools env
    virtualenv env 
    ./env/bin/pip install -r REQUIREMENTS
    source env/bin/activate
    
    cd project/
    python manage.py runserver
    google-chrome http://localhost:8000 

As you can see, this causes a 500 error. huh.
