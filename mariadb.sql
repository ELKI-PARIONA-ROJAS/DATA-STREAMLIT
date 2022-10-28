-- Exportando datos 
SELECT v.Anio, v.Mes, v.Dia, v.ID_Vuelo, v.ID_Aeropuerto_O, v.Hora_SalidaR, a.Latitud, a.Longitud
INTO OUTFILE 'F:/PROYECTO_GRUPAL/extracciones/vueloSA.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '
'
FROM vuelo as v
JOIN aeropuerto_o as a
ON v.ID_Aeropuerto_O = a.ID_Aeropuerto
WHERE v.ID_DepTime = 'A' and v.Anio = 2018;

-- Convertir a formato de fecha combinando 

ALTER TABLE vuelo_2018 ADD COLUMN Fecha DATE;
UPDATE vuelo_2018 SET Fecha = CONCAT(Anio,'-',Mes,'-',Dia);

-- Eliminar las columnas de Anio, Mes, Dia, Hora_SalidaR, Latitud, Longitud

ALTER TABLE vuelo_2018 DROP COLUMN Anio;
ALTER TABLE vuelo_2018 DROP COLUMN Mes;
ALTER TABLE vuelo_2018 DROP COLUMN Dia;
ALTER TABLE vuelo_2018 DROP COLUMN Hora_SalidaR;
ALTER TABLE vuelo_2018 DROP COLUMN Latitud;
ALTER TABLE vuelo_2018 DROP COLUMN Longitud;
ALTER TABLE vuelo_2018 DROP COLUMN ID_Aeropuerto_O;

-- Crear una tabla que por cada Fecha tenga la cantidad de vuelos que salieron de ese dia

CREATE TABLE vuelos_por_dia AS
SELECT Fecha, COUNT(*) AS Cantidad
FROM vuelo_2018
GROUP BY Fecha;

-- Exportar la tabla a un archivo csv

SELECT * INTO OUTFILE 'F:/PROYECTO_GRUPAL/extracciones/vuelos_por_dia.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '
'
FROM vuelos_por_dia;











































