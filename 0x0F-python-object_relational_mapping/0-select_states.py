#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, database_name):
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
    try:
        # Connect to the MySQL server
        conn = MySQLdb.connect(host='localhost', port=3306,
                               user=mysql_username, passwd=mysql_password,
                               db=database_name, charset="utf8")
        cursor = conn.cursor()

        # Retrieve the states by executing the SQL query
        cursor.execute("SELECT id, name  FROM states ORDER BY states.id ASC")
        tables = cursor.fetchall()

        # Display the results
        for state in tables:
            print(state)

        # Close the cursor and connection
        cursor.close()
        conn.close()

    except MySQLdb.Error as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database_name>")
    else:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]
        list_states(mysql_username, mysql_password, database_name)
