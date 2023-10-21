#!/usr/bin/python3
"""
 List all states from a MySQL database.

    Args:
        username (str): MySQL username for authentication.
        password (str): MySQL password for authentication.
        database_name (str): Name of the MySQL database.

    Returns:
        None: Results are printed to the console.

    Note:
        This function connects to a MySQL server and retrieves a list of
        states from a specific database.
        It sorts the results by the 'id' column and displays them.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    """
    Connects to a MySQL server running on localhost at port 3306
    """
    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                           passwd=mysql_password, db=database_name,
                           charset="utf8")
    """
    Cursor object to interact with database
    """
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
