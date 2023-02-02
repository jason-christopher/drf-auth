# LAB - Class 33

## Project: Django REST Framework - Authentication & Production Server

## Author: Jason Christopher

### Links and Resources

* Django Libraries
* PostgreSQL
* Thunder Client
* Gunicorn

### Setup

* Clone down repo to local machine
* Create and activate a virtual environment
* Run `pip install -r requirements.txt`
* In one tab of your terminal, run `docker compose up`.
* You won't able to access the database information without logging in. In the URL, add `/admin` and log in with:
  * Username: `admin`
  * Password: `12345`
* Now you can go `/api/v1/homes` to access, create, update, and delete homes in the database.

### JWT Notes

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
  ```
  
* In project's `urls.py` add: `from rest_framework_simplejwt import views as jwt_views` and `path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),` and `path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),`.
* Comment out PostgreSQL DATABASE in `settings.py` and comment in SQLite DATABASE in order to run the server without going into the Docker container.
* Make sure there has been a ***superuser*** created and run `python manage.py runserver`.
* Open up Thunder Client in VS Code:
  * ***POST*** request with `127.0.0.1:8000/api/token/` as the address and `{"username":"admin", "password":"12345"}` as the ***BODY***.
  * Should return JWT in `refresh` and `access` sections.

### Production Notes

* Run `pip install gunicorn`.
* ***Outside the virtual environment***, run `docker compose up --build`.
* ***Inside the virtual environment***, run `gunicorn homes_project.wsgi:application --bind 0.0.0.0:8000 --workers 4`
* You can go to the live site and the CSS will be all messed up.
* Shut down everything and run `pip install whitenoise` to create `static` assets.
* In `settings.py` in MIDDLEWARE, add `'whitenoise.middleware.WhiteNoiseMiddleware',` ***AFTER*** the `'django.middleware.security.SecurityMiddleware',` line.
* Also in `settings.py`, add `STATIC_ROOT = BASE_DIR / "staticfiles"` to the bottom of the file.
* ***Inside the virtual environment***, run `python manage.py collectstatic` to create the `staticfiles` directory.
* ***Inside the virtual environment***, run `gunicorn homes_project.wsgi:application --bind 0.0.0.0:8000 --workers 4` again and the CSS looks like normal.
* ***Outside the virtual environment***, run `docker compose up --build` (make sure to `pip freeze` before inside the virtual environment).
* ***In another terminal tab***, run `docker compose run web bash` and then `gunicorn homes_project.wsgi:application --bind 0.0.0.0:8000 --workers 4`.
* In the `docker-compose.yml` file, comment out the current `command` line and replace with: `command: gunicorn things_api_project.wsgi:application --bind 0.0.0.0:8000 --workers 4`. This will let you launch Gunicorn inside the Docker container by ***JUST*** running `docker compose up` outside the virtual environment.