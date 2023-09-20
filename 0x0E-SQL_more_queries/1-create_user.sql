-- a script that creates the MySQL server user user_0d_1
-- user_0d_1 should have all privileges on your MySQL server
-- user_0d_1 password should be set to user_0d_1_pwd
-- If the user user_0d_1 already exists, your script should not fail
-- Check if the user exists
SELECT EXISTS(SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost') INTO @user_exists;

-- If the user doesn't exist, create it with all privileges
IF @user_exists = 0 THEN
  CREATE USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
  GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
  FLUSH PRIVILEGES;
-- this statement is used to reload the server's privilege tables, which
-- store information about user accounts and their associated privileges.
-- When you execute commands that modify user privileges or create new users
-- (such as CREATE USER, GRANT, REVOKE, ALTER USER, etc.)
  SELECT 'User user_0d_1 created and granted all privileges.';
ELSE
  SELECT 'User user_0d_1 already exists.';
END IF;

