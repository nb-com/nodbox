# Nodbox
Nodbox is an open source  **File Handling Deskapp**.The App is developed with **Django** at back-end and **Tailwind** at front-end.<br /> 

**Discord** - https://discord.gg/AQJtJfGwh7<br />




## Deployment
The Website is Deployed at https://nodbox.herokuapp.com (under development)

## Requirements
Required Packages can be found at **requirements.txt**

## Features

1) Convert Image to PDF
2) Convert PDF to Image (under development)

## Get Started

1. Clone Repository - https://github.com/nb-com/nb.git
2. Create a virtual environment <br />
a) To install virtual environment.
  
  ```
  pip install virtualenv
  ```
 
 ```
  virtualenv env
  ```
  
  b) Activate virtual environment according to your operating system. <br />
  
 **For Windows**
 ```
 .\env\Scripts\activate
 ```
 **For Mac OS**
 ```
 source env/bin/activate
 ```
3.Install Required Packages by

```
pip install -r requirements.txt
```
4. Start the server by
 ```
 python manage.py runserver
 ```
 Now the server will be serving at localhost 8000
 
 ## To Launch as a Deskapp
**Windows**
```
python3 nodbox.py
```
**Mac OS and other Operating Systems**
```
python nodbox.py
```
**(Has various bugs)**
