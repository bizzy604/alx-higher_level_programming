-- create a database hbtn_0d_usa, table states on MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREAMENT PRIMARY KEY,
	name VARCHAR(256));
