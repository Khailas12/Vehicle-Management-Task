# Vehicle-Management-Task

## Setup

Clone the repository:

```sh
$ git clone https://github.com/Khailas12/Vehicle-Management-Task
$ cd Vehicle-Management-Task
```

Install the dependencies:

```sh
(env)$ pip install -r requirements.txt
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

To run the tests, `cd` into the directory where `manage.py` is:
```sh
$ python manage.py test 
```

Seperate tests for `account` and `vehicle` apps:
```sh
$ python manage.py test account
$ python manage.py test vehicle
```
Please refer to the [Django App Test Documentation](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing) and [Unit Test Documentation](https://mkdev.me/posts/how-to-cover-django-application-with-unit-tests) for more details.
