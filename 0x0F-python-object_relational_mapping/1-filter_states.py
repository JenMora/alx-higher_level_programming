#!/usr/bin/python3
"""
 List all states from a MySQL database that start with the letter N

    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database.

    Returns:
        None: Results are printed to the console.

    Note:
        This function connects to a MySQL server and retrieves a list of
        states that stat with the letter N
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
    """
    Connects to a MySQL server at a local host and port 3306
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    """
    interact the object to interact with database through a cursor
    """
    cursor = conn.cursor()
    cursor.execute("""SELECT id, name FROM states WHERE name LIKE _utf8mb4 'N%'
                  COLLATE utf8mb4_0900_as_cs  ORDER BY id ASC""")

    states = cursor.fetchall()
    for state in states:
        print(state)
    """
    close the connection and the cursor
    """
    cursor.close()
    conn.close()
