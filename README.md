## Django Blog

This is a simple blogging application built with Django.
### Features
-	User registration and authentication
-	Create, update, and delete posts
-	View all posts or only those authored by the current user

### Requirements
-	Python 3.6 or later
-	Django 3.1 or later
-	See requirements.txt for full list of dependencies

### Installation
1. Clone the repository:
```
git clone https://github.com/<your-username>/django-blog.git 
```
2.	Install dependencies:
```
pip install -r requirements.txt 
```
3.	Set up the database:
```
python manage.py migrate
```
4.	Create a superuser:
```
python manage.py createsuperuser 
```
5.	Run the development server:
```
python manage.py runserver 
```
6.	Access the application at ```http://localhost:8000/```

### Usage
-	Navigate to http://localhost:8000/ to see all posts
-	Click on `"Log in"` to authenticate or `"Sign up"` to create an account
-	After logging in, you can view only your own posts by clicking on `"My posts"`
-	To create a new post, click on `"New post"` and fill out the form
-	To edit or delete a post, go to its detail page and click on `"Edit"` or `"Delete"`
### License
This project is licensed under the MIT License. See LICENSE for details
