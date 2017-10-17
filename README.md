# Orchard

A Python and Django web app itemising the Orchard at Fiddleford.

To run the app you will need python and django installed. You can then create a virtual environment and install the requirements using the commands below.

An inventory of existing trees can be imported by running the importer.

## Development

Create and activate the virtual environment and install requirements:
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Run the database migration:
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create a .env file with the following vars:
```
$ touch fruitapp/.env
---
GEOPOSITION_GOOGLE_MAPS_API_KEY=' '
SECRET_KEY=' '
```

(Get a [google maps API Key](https://developers.google.com/maps/documentation/javascript/get-api-key) and generate a [django secret key](https://www.miniwebtool.com/django-secret-key-generator/))

Run the app:
```
$ python manage.py runserver --insecure
$ open localhost:8000
```

Deactivate the virtual environment when finished:
```
$ deactivate
```

Run the importer:
```
$ python import.py
```
