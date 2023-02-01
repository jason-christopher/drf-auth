# LAB - Class 32

## Project: Django REST Framework Permissions & PostgreSQL

## Author: Jason Christopher

### Links and Resources

* Django Libraries
* PostgreSQL

### Setup

* Clone down repo to local machine
* Create and activate a virtual environment
* Run `pip install -r requirements.txt`
* In one tab of your terminal, run `docker compose up`.
* In another tab in your terminal, run `docker-compose run web bash` to create a terminal inside the Docker container.
  * In that same tab, run `python manage.py makemigrations` and `python manage.py migrate`.
  * Run `python manage.py runserver` and open the URL into your browser.
* You won't able to access the database information without logging in. In the URL, add `/admin` and log in with:
  * Username: `admin`
  * Password: `12345`
* Now you can go `/api/v1/homes` to access, create, update, and delete homes in the database.

### Tests

* Tests can be run by running `python manage.py test`.
* All 7 tests are passing.

### Notes

* In the beginning of the project, run `pip install django`, `pip install djangorestframework`, and `pip install psycopg2-binary` before creating the project and app.
* Once the project and app are made, in the project's `settings.py` file:
  * Comment out DATABASES and add:

  ```python
  DATABASES = {
      "default": {
          "ENGINE": "django.db.backends.postgresql",
          "NAME": "postgres",
          "USER": "postgres",
          "PASSWORD": "postgres",
          "HOST": "db",
          "PORT": 5432,
      }
  }
  ```

* In the `docker-compose.yml` file, add:

    ```python
    db:
        image: postgres
        environment:
          - POSTGRES_DB=postgres
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=postgres
    ```
* In one tab of your terminal, run `docker compose up`.
* In another tab in your terminal, run `docker-compose run web bash` to create a terminal inside the Docker container.
  * In that same tab, run `python manage.py makemigrations` and `python manage.py migrate`.
  * Run `python manage.py createsuperuser` and add a username, email(optional), and password.
  * Run `python manage.py runserver` and open the URL into your browser.
  * Exit the Docker container terminal with `exit`.
