-- creates a database and table with id pk, not null, and auto increment constraints and state_id with not null and fk constraints
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
	id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	state_id INT,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
