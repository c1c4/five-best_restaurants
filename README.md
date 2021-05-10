# five-best_restaurants

This application has the purpose to test the search for the restaurants in csv files **restaurants.csv**
and **cuisines.csv**.

This application needs:

- Flask
- flask-restplus
- Werkzeug

For test
- pytest
- tox
- coverage

You can find all the requirements in requirements.txt

To run this application you have two options:

#**First Option:**
- **Requirements**:
  
    - Python 3.8 or later
    - python3 -m venv /path/to/new/virtual/environment
    - source /path/to/new/virtual/environment/bin/activate
    - pip install -r requirements.txt
    
- Open your terminal go to application folder and run the command:

    - flask run
    - access in your browser http://127.0.0.1:5000/
    
If you don't have or can't install the virtual environment, or has problemas with pip here the documentation:

 - Download and documentation for python https://www.python.org/
 - For virtual environment https://docs.python.org/3/library/venv.html
 - For pip https://pypi.org/project/pip/

#**Second Option:**
- **Requirements**:
  
    - Docker
    - docker-compose
    
- Open your terminal go to application folder and run the command:

    - docker-compose up 
    - access in your browser http://127.0.0.1:5000/
    
If you don't have or can't install the docker, or docker-compose here the documentation:

 - Download and documentation for docker https://docs.docker.com/get-docker/
 - For docker-compose https://docs.docker.com/compose/install/


    