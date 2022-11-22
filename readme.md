# Vehicle-Management-Task

## Versions
Django: `4.0.8`

Python: `3.9.6`


## Setup

Clone the repository:

```sh
$ git clone https://github.com/Khailas12/Vehicle-Management-Task
$ cd Vehicle-Management-Task
```

Install the dependencies:

```sh
$ pip install -r requirements.txt
```

Once `pip` has finished downloading the dependencies:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Once you're done with DB migrations:
```sh
$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`.


## Tests

Test both the apps simultaneously:
```sh
$ python manage.py test 
```

Test `account` and `vehicle` apps separately:
```sh
$ python manage.py test account
$ python manage.py test vehicle
```
Please refer to the [Django App Test](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing) and [Unit Test](https://mkdev.me/posts/how-to-cover-django-application-with-unit-tests) Documentations for more details.
