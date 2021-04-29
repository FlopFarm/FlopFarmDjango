<!--
 * @Author: your name
 * @Date: 2021-04-29 23:11:51
 * @LastEditTime: 2021-04-29 23:28:39
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
            └───dashboard.html
            └───user.html
            └───edge.html
        |   ...
```
## Run Website
```linux
cd FlopFarmDjango/flopfarm
python manage.py runserver
```
and you can browse the website at 
```
127.0.0.1:8000
```