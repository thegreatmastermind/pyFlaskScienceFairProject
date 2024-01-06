# pyInventory
An inventory system developed in flask hosted in microsoft azure cloud

## Setup For deployment
1. Create  a resource group and an app service plan.
2. Make sure you the requirments.txt, or else you miss dependencies
3. In the APP Service plan make sure the configuration - general settings - 
    gunicorn --bind=0.0.0.0 --timeout 600 startup:app  
4. 

## Deployment

## libraries
py -m venv env
&env/scripts/activate.ps1 (to work in the env folder)
 py -m pip install --upgrade pip   (make sure you have the latest pip)
 pip install -r requirements.txt (this would install all the libraries)

go to vs code -> Run & debug
run -> will create a launch.json file ->  python -> flask -> startup.py
"version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Flask",
            "type": "python",
            "request": "launch",
            "module": "flask",
            "env": {
                "FLASK_APP": "startup.py",
                "FLASK_DEBUG": "1"
            },
            "args": [
                "run",
                "--no-debugger",
                "--no-reload"
            ],
            "jinja": true,
            "justMyCode": true
        }
    ]
    

 
(env) PS C:\projects\github\pyInventory> set FLASK_APP=app.py
(env) PS C:\projects\github\pyInventory> set FLASK_ENV=development


(env) PS C:\projects\github\pyInventory> $Env:FLASK_APP="startup:app"
(env) PS C:\projects\github\pyInventory> $Env:FLASK_ENV="development"

## future libraries
1. Pendulum - for datetime
2. pypdf - read / merge /split pdf documents
3. icecream - debugging easier
4. loguru - logging 
5. Xarray - multi dimensional data

https://stackoverflow.com/questions/19314342/python-sqlalchemy-pass-parameters-in-connection-execute