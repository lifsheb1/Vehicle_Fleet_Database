CREATE TABLE Vehicle (
    Make varchar(50),
    Model varchar(50),
    Typev varchar(50),
    Department varchar(50) NOT NULL,
    VIN_Number int PRIMARY KEY,
    Yearv int NOT NULL,
    Year_Incorporated int NOT NULL,
    Vehicle_Type_Code int NOT NULL,
    Time_Line varchar(50) NOT NULL
);

CREATE TABLE Vehicle_Types (
    Vehicle_Type_Code varchar NOT NULL,
    Vehicle_Type varchar(50) NOT NULL,
    Engine varchar(50) NOT NULL,
    Anticipated_Mileage int NOT NULL, 
    Estimated_MPG int, 
    Initial_Cost int NOT NULL,
    Incentives int,
    Annual_Fuel_Cost int NOT NULL,
    Maintenance_Cost int NOT NULL,
    Repairs int NOT NULL,
    Tire_Replacement int NOT NULL,
    Battery_Replacement int NOT NULL,
    Insurance int NOT NULL,
    Lifetime_Cost int NOT NULL,
    Annual_Cost int NOT NULL,
    GHC_Emissions int,
    Vehicle_Type_Code int REFERENCES Vehicle,
    PRIMARY KEY (Vehicle_Type_Code)
);



CREATE TABLE Variables (
    Fuel_Cost int NOT NULL,
    GTE_Miles int NOT NULL,
    GTE_Years int NOT NULL,
    Maintenance_Per_Mile numeric(3,2) NOT NULL,
    Depreciation int NOT NULL,
    Equal_Carbon_Emission numeric(4,2),
    Vehicle_Type_Code int REFERENCES Vehicle_Types,
    PRIMARY KEY (Vehicle_Type_Code)
);

CREATE VIEW view1  AS
	SELECT *
    FROM Vehicle_Types NATURAL JOIN Vehicle;




