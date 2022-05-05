# Overview
The purpose of this project is to find the most optimal compisition of TCNJ's vehicle fleet. TCNJ has a variety of vehicles in its vehicle fleet that use a variety of fuels(petroleuem, electric, hydrogen) and are from a variety of years. This project will allow a user to see results of cost-benefit analysis and environmental sustainability analysis for each type of vehicle within the fleet. Ideally, this project will allow TCNJ to compose a vehicle fleet that is both finacially and environmentally sustainable. 


# Installation

You must also clone the repository with the following command: 

```
git clone https://github.com/TCNJ-degoodj/cab-project-02-7.git
```

You must perform this one-time installation in the CSC 315 VM:

```
# install python pip and psycopg2 packages
sudo pacman -Syu
sudo pacman -S python-pip python-psycopg2

# install flask
pip install flask
```

# How to use

To run the Flask application, simply execute:

```
export FLASK_APP=app.py
flask run
# then browse to http://127.0.0.1:5000/
```
Once in the app, use the navigation bar at the top to toggle between the analysis screen and the information screen. The analysis page can be used to understand what vehicles are in the database and how they may be impacting the environment. The information page can be used to learn about the different types of emissions and why it is important to care about vehicle types.
