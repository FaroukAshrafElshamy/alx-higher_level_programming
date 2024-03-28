-- A script that converts hbtn_0c_0 database to UTF8
-- Convert DB to utf-8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
-- use DB
USE hbtn_0c_0;
-- Convert first table to utf-8
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;