# django-Metallics_Optimization
It is django based RESTAPI for Metallics Optimization Service .

# Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/surajkarale15/Metallic_Optimization.git`<br>
  `cd Metallics_Optimization`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) Add 'service' to your 'INSTALLED_APPS' setting.
	INSTALLED_APPS={
		...
		'service'
		...
	}
	
	Add the following to your projects 'urls.py' file, substituting 'api/v1/'
	for whatever you want the service base url to be.
	urlpatterns = [
    ...
    path('api/v1/', include('service.urls')),
	...
	]
	
4) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
5) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

6) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
 

  
