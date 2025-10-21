-- 2-create_read_user.sql
-- This script creates the database hbtn_0d_2 and user_0d_2 with SELECT privileges

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Grant only SELECT privilege on the database to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;

