# Collab
- A Django Slack replica that is used for team communication and file sharing.
- Can import the exported slack channel data.

## Requires
 * [redis](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04)
 * [postgresql](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)
 * [nodejs and pm2](https://www.digitalocean.com/community/tutorials/how-to-install-node-js-on-ubuntu-16-04)
 * [apache2 and django](https://www.digitalocean.com/community/tutorials/how-to-serve-django-applications-with-apache-and-mod_wsgi-on-ubuntu-16-04)
 * python libraries:
    * django
    * pytz
    * redis
    * psycopg2
    ```
    pip install django pytz redis psycopg2
    ```
    
## Steps to start the App
1. start redis
 > ```
 > sudo systemctl start redis
 > ```
    
2. run chat.js present inside folder `nodejs`
 >  ```
 > cd nodejs
 > pm2 start chat.js
 > cd ..
 > ```
    
3. migrate db
 > ```
 > python manage.py makemigrations
 > python manage.py migrate
 > ```
    
4. run App
   1. if apache not configured run django
   > ```
   > python manage.py runserver
   > ```
   
   2. if apache configured restart apache2
   > ```
   > sudo service apache2 restart
   > ```
 
