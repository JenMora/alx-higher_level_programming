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
        conn = MySQLdb.connect(host='localhost', port=3306, user=username,
                               passwd=password, db=database_name)
        cursor = conn.cursor()

        # Retrieve the states by executing the SQL query
        cursor.execute("SELECT * FROM states ORDER BY id")
        states = cursor.fetchall()

        # Display the results
        for state in states:
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
        username, password, database_name = sys.argv[1],
        sys.argv[2], sys.argv[3] list_states(username, password, database_name)
