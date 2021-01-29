# NGO_NAIROBI--INTERVIEW ASSIGNMENT ONB-KENYA

This is a geodjango project(NGO-NAIROBI) developed in geodjango for back-end, Leaflet.js for front-end and Postgresql for Database.
It uses the Geodjango module in Django to include the mapping aspect of the project. This is the entire project covered in all the episodes. 

## Set Up
To set up the project, follow the steps;
```
sudo apt-get install postgresql postgresql-contrib \ postgis \ git
```
## On a Virtual Environment

```
Sudo apt-get install python-virtualenv
virtualenv venv
cd venv && . bin/activate
```
## Clone the system
```
git clone https://github.com/DanielMawioo/NGO_NAIROBI.git
```
## Setting up DB
```
sudo -u postgres createuser -P USER_NAME_HERE
sudo -u postgres createdb -O USER_NAME_HERE DATABASE_NAME_HERE #Remember to change in settings.py
#Enable PostGIS
sudo -u postgres psql -c "CREATE EXTENSION postgis; CREATE EXTENSION postgis_topology;" DATABASE_NAME_HERE
```
## Installing Requirements
```
pip3 install -r requirements.txt
```
## Sync and Running application
```
cd agricom
python manage.py migrate
python manage.py runserver
on browser: localhost:8000
```
## Support
contact me here https://daniel-mawioo.herokuapp.com/   or Whatsap +254758578816.