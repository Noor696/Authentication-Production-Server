# Authentication-Production-Server


**Author: Noor Alkhateeb**

* admin : _noor_  / pass: _noor_

**the App. have One models**
Novel

* [JWT documentation](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html)

* [Customizing token claims](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/customizing_token_claims.html)

**Run:**

> python3 manage.py runserver


**update the database:**

> python manage.py makemigrations
> python manage.py migrate

**> docker-compose up**
when run this command:
* my image will be build
* my container will be build
* take all the project and put it inside the container
* then run the server inside the container.


**Dockerfile** : to build docker image, the data inside it same for all django application.

**docker-compose.yml** : responsible to create the container

