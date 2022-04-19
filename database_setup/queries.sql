SELECT Initial_Cost, Annual_Cost, Lifetime_Cost, GHG_Emissions
FROM view1
WHERE make ILIKE 'ford%' AND model ILIKE 'explorer%';


SELECT *
FROM view1
WHERE make ILIKE 'ford%' AND model ILIKE 'explorer%';


/* sort by engine type */
SELECT Make, Model, Year, Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions
FROM view1
WHERE Engine ILIKE 'PICE%';

/* table with all of them that sorts by age or efficiency */
SELECT Initial_Cost, Annual_Cost, Lifetime_Cost, GHG_Emissions, Timeline
FROM view1
ORDER BY ASC GHG_Emissions;