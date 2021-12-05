# MyUBP - LAB-IV

## Steps for starting up the project
### - ***Install requirements***
```
$ pip install -r requirements.txt
```
### - ***Generate and make migrations***

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### - ***Load data from Fixtures***
```
$ python3 manage.py loaddata fixtures/fixture.json
```

### - ***Turn on server***

```
$ python manage.py runserver
```

***
## DER
![DER MyUBP](https://github.com/felipeBozzano/Proyecto-Lab-IV/blob/dev/myubp/assets/ERD.jpeg)
***

## Users
* __*ROOT*__
  * user_name: root@root.com
  * password: r00t1234
  
* __*TEST USERS:*__
  * __*TEST*__
    * user_name: test@test.com
    * password: test1234
  * __*Francisco*__
    * user_name: francisco@test.com
    * password: test1234
  * __*Felipe*__
    * user_name: felipe@test.com
    * password: test1234
  * __*Benjamin*__
    * user_name: benjamin@test.com
    * password: test1234
****
    
## Postman Collection
* ### Import the following collection: [MYUBP-POSTMAN-COLLECTION](https://github.com/felipeBozzano/Proyecto-Lab-IV/blob/dev/myubp/postman/MyUBP.postman_collection.json)
* ### Import the following environment: [MYUBP-LOCAL-ENVIRONMENT](https://github.com/felipeBozzano/Proyecto-Lab-IV/blob/dev/myubp/postman/Local.postman_environment.json)
****

# API DOCUMENTATION
  * Firts you need to have your server running
  * Then visit the following link: http://127.0.0.1:8000/api/v1/doc

****


# HOW TO START DOCKER CONTAINERS
```
  $ docker-compose build
  $ docker-compose up
  $ docker exec -it myubp_web_1 /bin/bash
  $ python manage.py migrate
  $ python manage.py loaddata fixtures/fixture.json
```
****

## Generate fixture from data base
```
  $ python manage.py dumpdata app.model_name
```
****

## How to run test
```
  $ python manage.py test app.tests.testCaseName
```


  


