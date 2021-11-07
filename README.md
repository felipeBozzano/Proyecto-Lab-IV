# MyUBP - LAB-IV

## Pasos para levantar el proyecto
### - ***Instalar requerimientos***
```
$ pip install -r requirements.txt
```
### - ***Hacer las migraciones de la base de datos***

```
$ python manage.py makemigrations
$ python manage.py migrate
```

### - ***Popular tablas***
```
$ python3 manage.py loaddata fixture\fixture.json
```

### - ***Levantar servidor***

```
$ python manage.py runserver
```

## Nuestro DER
![DER MyUBP](https://github.com/felipeBozzano/Proyecto-Lab-IV/blob/dev/myubp/assets/ERD.jpeg)

## Usuarios
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
  


