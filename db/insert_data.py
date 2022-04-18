import csv 
import psycopg2

dbConnection = psycopg2.connect(database="vehicle_fleet", user='postgres', password='test')
dbConnection.autocommit = True
dbCursor = dbConnection.cursor()

#get values from vehicle csv
vehicleFile = open("Vehicles.csv", 'r')
vehicleCSV = csv.reader(vehicleFile)

vehicleHeader = next(vehicleCSV)


#insert vehicles into database
for row in vehicleCSV:
    if(row[2].isdigit()): #if vehicle has year
        dbCursor.execute('INSERT INTO Vehicle(VIN_Number, Department, Yearv, Make, Model, Vehicle_Type_Code, Typev, Time_Line) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    else: #year assigned to zero if none given as yearv has to be an integer
        dbCursor.execute('INSERT INTO Vehicle(VIN_Number, Department, Yearv, Make, Model, Vehicle_Type_Code, Typev, Time_Line) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], 0, row[3], row[4], row[5], row[6], row[7]))


#get values from vehicle type csv
vehicleTypeFile = open("Vehicle_Types.csv", 'r')
vehicleTypeCSV = csv.reader(vehicleTypeFile)

vehicleTypeHeader = next(vehicleTypeCSV)

#insert vehicleTypes into database
for row in vehicleTypeCSV:
    if(row[6].isdigit() and row[4].isdigit()):  #if vehicleType has incentives and estimated mpg
        dbCursor.execute('INSERT INTO Vehicle_Types(Vehicle_Type_Code, Vehicle_Type, Engine, Anticipated_Mileage, Estimated_MPG, Initial_Cost, Incentives, Annual_Fuel_Cost, Maintenance_Cost, Repairs, Tire_Replacement, Battery_Replacement, Insurance, Lifetime_Cost, Annual_Cost, GHG_Emissions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
    elif(row[6].isdigit()): #incentives given but estimated_mpg not given
        dbCursor.execute('INSERT INTO Vehicle_Types(Vehicle_Type_Code, Vehicle_Type, Engine, Anticipated_Mileage, Estimated_MPG, Initial_Cost, Incentives, Annual_Fuel_Cost, Maintenance_Cost, Repairs, Tire_Replacement, Battery_Replacement, Insurance, Lifetime_Cost, Annual_Cost, GHG_Emissions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], 0, row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))
    else: #incentives assigned to zero if none given as attribute has to be an integer
        dbCursor.execute('INSERT INTO Vehicle_Types(Vehicle_Type_Code, Vehicle_Type, Engine, Anticipated_Mileage, Estimated_MPG, Initial_Cost, Incentives, Annual_Fuel_Cost, Maintenance_Cost, Repairs, Tire_Replacement, Battery_Replacement, Insurance, Lifetime_Cost, Annual_Cost, GHG_Emissions) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], row[4], row[5], 0, row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15]))

#print(vehicleTypeData[0])

#get values from variables csv
variableFile = open("Variables.csv", 'r')
variableCSV = csv.reader(variableFile)

variableHeader = next(variableCSV)
#print(variableHeader)

#insert variables into database
for row in variableCSV:
  try: #carbon emissions and fuel cost are given
    float(row[6])   
    dbCursor.execute('INSERT INTO Variables(Vehicle_Type_Code, Fuel_Cost, GTE_Miles, GTE_Years, Maintenance_Per_Mile, Depreciation,Equal_Carbon_Emission) VALUES (%s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
  except: #carbon emissions are not given
    dbCursor.execute('INSERT INTO Variables(Vehicle_Type_Code, Fuel_Cost, GTE_Miles, GTE_Years, Maintenance_Per_Mile, Depreciation,Equal_Carbon_Emission) VALUES (%s, %s, %s, %s, %s, %s, %s)', (row[0], row[1], row[2], row[3], row[4], row[5], 0))    
dbCursor.close()
dbConnection.close()
