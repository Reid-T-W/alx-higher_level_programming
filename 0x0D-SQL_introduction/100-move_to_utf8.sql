-- convert character encoding of database, tables and fields to UTF8
-- converting tables
mysql \-\-database=hbtn_0c_0 -B -N -e "SHOW TABLES" | awk '{print "SET foreign_key_checks = 0; ALTER TABLE", $1, "CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci; SET foreign_key_checks = 1; "}' | mysql --database=dbname

-- converting database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
