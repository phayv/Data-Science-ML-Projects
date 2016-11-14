create table temp_drivers   (col_value STRING);
create table temp_timesheet (col_value STRING);

LOAD DATA INPATH '/hive-files/drivers.csv' OVERWRITE INTO TABLE temp_drivers;
LOAD DATA INPATH '/hive-files/drivers.csv' OVERWRITE INTO TABLE temp_timesheet;

CREATE TABLE drivers (driverId INT, name STRING, ssn BIGINT, location STRING, certified STRING, wageplan STRING);
CREATE TABLE timesheet (driverId INT, week INT, hours_logged INT , miles_logged INT);

INSERT OVERWRITE TABLE drivers  
SELECT  
  regexp_extract(col_value, '^(?:([^,]*),?){1}', 1) driverID,  
  regexp_extract(col_value, '^(?:([^,]*),?){2}', 1) name,  
  regexp_extract(col_value, '^(?:([^,]*),?){3}', 1) ssn,
  regexp_extract(col_value, '^(?:([^,]*),?){4}', 1) location,  
  regexp_extract(col_value, '^(?:([^,]*),?){5}', 1) certified,  
  regexp_extract(col_value, '^(?:([^,]*),?){6}', 1) wageplan
FROM temp_drivers;

INSERT OVERWRITE TABLE timesheet  
SELECT  
  regexp_extract(col_value, '^(?:([^,]*),?){1}', 1) driverId,  
  regexp_extract(col_value, '^(?:([^,]*),?){2}', 1) week,  
  regexp_extract(col_value, '^(?:([^,]*),?){3}', 1) hours_logged,
  regexp_extract(col_value, '^(?:([^,]*),?){4}', 1) miles_logged  
FROM temp_timesheet;

--Joining the two tables (righton and lefton equals driverID)
--timesheet squashed to unique ID's using GROUP BY
SELECT d.driverId, d.name, t.total_hours, t.total_miles from drivers d  
JOIN (SELECT driverId, sum(hours_logged)total_hours, sum(miles_logged)total_miles FROM timesheet GROUP BY driverId ) t  
ON (d.driverId = t.driverId);