#file that builds the database
#Benjamin Lifshey

import psycopg2

connection = psycopg2.connect(database="postgres", user='postgres', password='test')
connection.autocommit = True

cursor = connection.cursor()

#drop previous version of vehicle fleet
dropDB = 'DROP DATABASE IF EXISTS vehicle_fleet;'
cursor.execute(dropDB)

#create database
createDB = 'CREATE DATABASE vehicle_fleet;'
cursor.execute(createDB)

cursor.close()
connection.close()

dbConnection = psycopg2.connect(database="vehicle_fleet", user='postgres', password='test')
dbConnection.autocommit = True
dbCursor = dbConnection.cursor()

#create tables and views

vehicleTable = 'CREATE TABLE Vehicle ( Make varchar(50), Model varchar(50), Typev varchar(50), Department varchar(50) NOT NULL, VIN_Number int PRIMARY KEY, Yearv int NOT NULL, Vehicle_Type_Code varchar(50), Time_Line varchar(50) NOT NULL );'
dbCursor.execute(vehicleTable)

vehicleTypeTable = 'CREATE TABLE Vehicle_Types ( Vehicle_Type_Code varchar NOT NULL, Vehicle_Type varchar(50) NOT NULL, Engine varchar(50) NOT NULL, Anticipated_Mileage int NOT NULL, Estimated_MPG int, Initial_Cost int NOT NULL, Incentives int, Annual_Fuel_Cost int NOT NULL, Maintenance_Cost int NOT NULL, Repairs int NOT NULL, Tire_Replacement int NOT NULL, Battery_Replacement int NOT NULL, Insurance int NOT NULL, Lifetime_Cost int NOT NULL, Annual_Cost float NOT NULL, GHG_Emissions float, PRIMARY KEY (Vehicle_Type_Code) );'
dbCursor.execute(vehicleTypeTable)

variableTable = 'CREATE TABLE Variables ( Fuel_Cost float NOT NULL, GTE_Miles int NOT NULL, GTE_Years int NOT NULL, Maintenance_Per_Mile numeric(3,2) NOT NULL, Depreciation float NOT NULL, Equal_Carbon_Emission numeric(4,2), Vehicle_Type_Code varchar(50) REFERENCES Vehicle_Types, PRIMARY KEY (Vehicle_Type_Code) );'
dbCursor.execute(variableTable)

view1 = 'CREATE VIEW view1  AS SELECT * FROM Vehicle_Types NATURAL JOIN Vehicle;'
dbCursor.execute(view1)

dbCursor.close()
dbConnection.close()