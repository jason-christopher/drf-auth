# LAB - Class 33

## Project: Django REST Framework - Authentication & Production Server

## Author: Jason Christopher

### Links and Resources

* Django Libraries
* PostgreSQL
* Gunicorn

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

* Install `pip install djangorestframework-simplejwt`
* In `settings.py`:

  ```python
  
  REST_FRAMEWORK = {
      'DEFAULT_PERMISSION_CLASSES': [
          'rest_framework.permissions.IsAuthenticated',
      ],
      # NEW!
      'DEFAULT_AUTHENTICATION_CLASSES': [
          'rest_framework_simplejwt.authentication.JWTAuthentication',
          'rest_framework.authentication.BasicAuthentication',
          'rest_framework.authentication.SessionAuthentication',
      ],
  }
  
  STATIC_ROOT = BASE_DIR / "staticfiles"
  ```
  
* In project's `urls.py` add: `from rest_framework_simplejwt import views as jwt_views` and `path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),` and `path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),`.
* Comment out PostgreSQL DATABASE in `settings.py` and comment in SQLite DATABASE in order to run the server without going into the Docker container.
* Make sure there has been a ***superuser*** created and run `python manage.py runserver`.
* Open up Thunder Client in VS Code:
  * ***POST*** request with `127.0.0.1:8000/api/token/` as the address and `{"username":"admin", "password":"12345"}` as the ***BODY***.
  * Should return JWT in `refrsh` and `access` sections.