<!--
 * @Author: your name
 * @Date: 2021-04-29 23:11:51
 * @LastEditTime: 2021-04-30 02:06:30
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: /FlopFarmDjango/README.md
-->
# FlopFarmDjango
## Environment
Django 3.2  
AdminLTE
## File Structure
```
FlopFarmDjango
│   README.md  
└───flopfarm
    └───flopfarm
        │   settings.py
        |   urls.py
        │   ...
    └───flopfarm_admin
        └───static # CSS, JavaScript, png... any static files
        └───templates # HTML
            |   temp.html # General template for dashboard, user&provider pages
            |   dashboard.html
            |   market.html
            |   purchased.html
            |   idle_instance.html
            |   running_instance.html
            |   login.html
            |   ...
        |   models.py
        |   urls.py
        |   views.py
        |   ...
    |   manage.py
    |   ...
```
## Run Website
```
cd FlopFarmDjango/flopfarm
python manage.py runserver
```
and you can browse the website at 
```
127.0.0.1:8000
```
So far, the login function is not developed. You can skip login by directly clicking the **Flop**Farm title.

## Run Unit Test
```
// In flopfarm directory, should run migrate to ensure data model are correct.
python3 manage.py test
```

## Quick Tutorial
### Database schema
### Loading database
### Using static files