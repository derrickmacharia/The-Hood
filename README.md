# THE HOOD!!

### 10th Jan. 2022

## Author

[Derrick Macharia](https://github.com/derrickmacharia)

# Description
Neighborhood is a simple web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different users to meeting announcements or even alerts.

##  Live Link 
 (https://myhoody.herokuapp.com/)

## Screenshots
###### Screenshot 1
<img src="static/images/Screenshot (1).png">

###### Screenshot 2
<img src="static/images/Screenshot (2).png">

###### Screenshot 3
 <img src="static/images/Screenshot (3).png">

###### Screenshot 4
 <img src="static/images/Screenshot (4).png">

###### Screenshot 5
 <img src="static/images/Screenshot (5).png">

###### Screenshot 6
 <img src="static/images/Screenshot (6).png">

## Setup and Installation 

##### Clone the repository: 
 ```bash
 git@github.com:derrickmacharia/The-Hood.git
```
##### Navigate into the folder and install requirements 
 ```bash
cd The-Hood pip install -r requirements.txt
```
##### Install and activate Virtual 
 ```bash
- python3 -m venv virtual - source virtual/bin/activate
```
##### Install Dependencies 
 ```bash
 pip install -r requirements.txt
```
##### Setup Database 
  SetUp your database User,Password, Host then make migrate
 ```bash
python manage.py makemigrations app
 ```
 Now Migrate
 ```bash
 python manage.py migrate
```
##### Run the application 
 ```bash
 python manage.py runserver
```

##### Testing the application 
 ```bash
 python manage.py test
```
Open the application on your browser `127.0.0.1:8000`.