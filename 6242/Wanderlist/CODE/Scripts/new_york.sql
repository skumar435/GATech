-- New York Script

-- ------------------------------------------------ main area ------------------------------------------
-- create schema and tables--------------------------------

CREATE SCHEMA `new_york` ;

CREATE TABLE `new_york`.`restaurants_rawdata` (
  `id` VARCHAR(200) NOT NULL,
  `name` VARCHAR(100) NULL,
  `rating` FLOAT NULL,
  `price` VARCHAR(45) NULL,
  `location` VARCHAR(500) NULL,
  `url` VARCHAR(500) NULL,
  `category` VARCHAR(300) NULL,
  `coordinates` VARCHAR(200) NULL,
  `review_count` INT NULL,
  PRIMARY KEY (`id`));

-- import data from csv into tables using mySQL workbench--------------------
-- 1) click on import records from an external file
-- 2) select file to import
-- 3) select previously existing table and click import


-- data cleanup and view setup ------------------------------

CREATE VIEW `new_york`.`restaurants_view` AS SELECT id, name, rating, price, review_count, category,
REPLACE(REPLACE (location,'[',''),']','') AS location, url,
concat_ws(',',SUBSTRING_INDEX(SUBSTRING_INDEX(coordinates,',',1),': ',-1), REPLACE(SUBSTRING_INDEX(SUBSTRING_INDEX(coordinates,', ',-1),': ',-1),'}','')) AS coordinates
FROM `new_york`.`restaurants_rawdata`;

 
-- create tables for hotel data---------------------------------


CREATE TABLE `new_york`.`hotel_rawdata` (
  `hotel_name` VARCHAR(200) NULL,
  `url` VARCHAR(500) NULL,
  `locality` VARCHAR(45) NULL,
  `reviews` VARCHAR(45) NULL,
  `rating` VARCHAR(45) NULL,
  `check_in` VARCHAR(45) NULL,
  `check_out` VARCHAR(45) NULL,
  `price_per_night` VARCHAR(30) NULL,
  `booking_provider` VARCHAR(45) NULL);
  


-- import data from csv into tables using mySQL workbench--------------------
-- 1) click on import records from an external file
-- 2) select file to import
-- 3) select previously existing table and click import 

-- data clean up and view setup-----------------------------


CREATE VIEW `new_york`.`hotel_view` AS
SELECT hotel_name, locality, reviews,
STR_TO_DATE(check_in,'%m/%d/%Y') AS check_in,
STR_TO_DATE(check_out, '%m/%d/%Y') as check_out,
CONVERT(REPLACE (price_per_night,'$',''),UNSIGNED INTEGER) AS price_per_night, booking_provider
FROM `new_york`.`hotel_rawdata`; 



-- create tables for places of interest data---------------------------------

CREATE TABLE `new_york`.`poi` (
	format_address VARCHAR(50),
	loc_lat FLOAT,
	loc_long FLOAT,
	id VARCHAR(50), 
	name_poi VARCHAR(50),
    rating FLOAT,
    user_rat_total INT);



-- import data from csv into tables using mySQL workbench--------------------
-- 1) click on import records from an external file
-- 2) select file to import
-- 3) select previously existing table and click import 

-- data clean up and view setup-----------------------------


CREATE VIEW `new_york`.`poi_view` AS SELECT DISTINCT * FROM `new_york`.`poi`;

-- create tables for city data---------------------------------

CREATE TABLE `new_york`.`city_data` (city_name VARCHAR(50), city_code VARCHAR(50), places_id VARCHAR(50));

-- create tables for flight data---------------------------------

CREATE TABLE `new_york`.`prices_flights` (min_price INT, is_direct VARCHAR(10), date_inbound DATE, date_outbound DATE, carrier_id VARCHAR(50),
origin_id VARCHAR(50), dest_id VARCHAR(50));

-- create tables for carrier data---------------------------------

CREATE TABLE `new_york`.`carrier_data` (carrier_id VARCHAR(50), carrier_name VARCHAR(50));

-- Data Import for above three tables------------------------

-- data clean up and view setup-----------------------------

CREATE VIEW `new_york`.`flight_view` AS
SELECT a.is_direct, a.date_inbound, a.date_outbound,
a.min_price, b.city_name as source_city, c.carrier_name
FROM `new_york`.`prices_flights` AS a, `new_york`.`city_data` AS b, `new_york`.`carrier_data` AS c
WHERE a.origin_id = b.places_id
AND a.carrier_id = c.carrier_id;

-- End of Script---------------------------------------------