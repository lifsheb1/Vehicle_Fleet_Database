SELECT Initial_Cost, Lifetime_Cost, Annual_Cost, GHG_Emissions
FROM view1
WHERE make ILIKE 'ford%' AND model ILIKE 'explorer%';


SELECT *
FROM view1
WHERE make ILIKE 'ford%' AND model ILIKE 'explorer%';
