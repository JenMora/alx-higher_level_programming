#!/usr/bin/python3
"""
 a script that takes in an argument and displays all values in the states
 table of hbtn_0e_0_usa where name matches the argument.
    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database.

    Returns:
        None: Results are printed to the console.

    Note:
        This function connects to a MySQL server and retrieves a list of
        states from a specific data
        the  script that takes in an argument and displays all values in the
        states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        state_name_searched = sys.argv[4]
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
    query = """SELECT id, name FROM states
    WHERE name = _utf8mb4 %s COLLATE utf8mb4_0900_as_cs
    ORDER BY id ASC"""
    cursor.execute(query, ('{:s}'.format(state_name_searched),))
    states = cursor.fetchall()
    for state in states:
        print(state)
    """
    close the connection and the cursor
    """
    cursor.close()
    conn.close()
