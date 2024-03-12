# Django Authentication Project
Web aplication was created using Python(Django Framework 5.0.1 version ), Bootstrap(3.3.7 version), CSS&HTML

## Features
* User Registration: Users can register for an account on the platform.

  ![User registration page](https://github.com/AndriiNorets/django_authentication/blob/master/READMEIMAGES/RegistrationPage.png)
* Login and Logout: Registered users can log in and out of their accounts.

  ![Login page](https://github.com/AndriiNorets/django_authentication/blob/master/READMEIMAGES/LoginPage.png)
* User Profile Data: When user is logged in, their profile data is displayed on the home page.

  ![Admin login page](https://github.com/AndriiNorets/django_authentication/blob/master/READMEIMAGES/homepagelogin.png)
* Users Page: There is a page named "Users" that displays a list of all users registered on the platform.

  ![Users page](https://github.com/AndriiNorets/django_authentication/blob/master/READMEIMAGES/UsersPage.png)
* Admin Access: The project includes an embedded Django admin page, contains a link in the navbar. Access to the admin page is restricted to superusers only.
  
  ![Admin login page](https://github.com/AndriiNorets/django_authentication/blob/master/READMEIMAGES/AdminPage.png)
## Functionality
### Registration system use:
* `register` method in [`views.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/views.py) file.
* `UserProfile` model in [`models.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/models.py).  
  Register our `UserProfile` model in [`admin.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/admin.py) file.
* `UserForm`, `UserProfileForm` forms in [`forms.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/forms.py).
* [`registration`](https://github.com/AndriiNorets/django_authentication/blob/master/templates/basic_app/registration.html) page with template tags using.
* Users data are uploding to db.sqlite3 database. Users profile pictures are also adding to `media/profile_pics/` directory.
### Login/Logout system use:
* `user_login` and `user_logout` methods in [`views.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/views.py) file.
  Contains built-in Django `login` and `logout` methods.  
  `user_logout` method use `@login_required` built-in Django decorator.
* [`login`](https://github.com/AndriiNorets/django_authentication/blob/master/templates/basic_app/login.html) page with template tags using.
  Contains `csrf_token `.
### User Profile Data displaing system use:
* [`index`](https://github.com/AndriiNorets/django_authentication/blob/master/templates/basic_app/index.html) page with template tags using.
  Cheaking `{% if user.is_authenticated %}` and displaing information.   
  `{{ user.username }}`, `{{ user.email }}` and `{{ user.profile.profile_pic.url }}` to get data from database and display them.

### Users Page use:
* [`users`](https://github.com/AndriiNorets/django_authentication/blob/master/templates/basic_app/users.html) page with template tags using.
* `users` method in [`views.py`](https://github.com/AndriiNorets/django_authentication/blob/master/basic_app/views.py) file.
* The same `{{ user.username }}`, `{{ user.email }}` and `{{ user.profile.profile_pic.url }}` tamplate tags using. 

### Admin Access use:
* Built-in admin's page's
* Login to Django admin page link is on navbar named `Admin`. 

## Project Structure
```
django_authentication/
│
├── django_authentication/
│   ├── init.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── basic_app/
│   ├── init.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── templates/
│ └── basic_app/
│     ├── base.html
│     ├── index.html
│     ├── login.html
│     ├── registration.html
│     └── users.html
│
├── media/
│ └── profile_pics/
|    └──               -uploading users profile pictures
│
├── static/
│ └── basic_app/
│     └── mystyle.css
│
├── db.sqlite3
└── manage.py
```

  
