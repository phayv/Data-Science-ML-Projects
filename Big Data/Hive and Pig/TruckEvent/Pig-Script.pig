truck_events = LOAD '/hive_tutorial/truck_event_text_partition.csv' 
			   USING PigStorage(',')
               AS (driverID:int, 
               	   truckID:int, 
                   event_time:chararray,
                   event_type:chararray,
                   longitude:double,
                   latitude:double,
                   event_key:chararray,
                   correlationID:long,
                   driver_name:chararray,
                   routeID:long,
                   route_name:chararray,
                   event_date:chararray);
DESCRIBE truck_events;