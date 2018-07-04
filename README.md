## create virtualenv
$ virtualenv -p [python you wish to use] [NAMEOFVIRTUALENV]
i.e. virtualenv -p python3 venv

## Activate virtualenv
$ source [NAMEOFVIRTUALENV]/bin/activate

## Install via pip installing all dependencies in requirements.txt
$ pip install -Ur [FILE]
i.e. pip install -Ur requirements.txt

## Start a django project
$ django-admin startproject [NAME] [LOCATION]
i.e. django-admin startproject config .

## Deactivate virtualenv
(in virtualenv)
$ deactivate 

## Run Server
(in virtualenv)
$ ./manage.py runserver
