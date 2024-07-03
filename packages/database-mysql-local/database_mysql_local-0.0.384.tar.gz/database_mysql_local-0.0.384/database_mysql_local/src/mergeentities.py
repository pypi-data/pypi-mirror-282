import datetime

import mysql.connector
from mysql.connector import errorcode

def merge_entities(entity_id1: int, entity_id2: int, main_entity_ml_id: int = None):
    global conn, cursor
    database = {
        'user': 'gabriel.d',
        'password': 'gab1Riel!Circ',
        'host': 'mysql-db.dvlp1.circ.zone',
        'database': 'location'
    }
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(**database)
        cursor = conn.cursor()

        # establish which id is being merged/ended and which one it is being merged into
        end_id = entity_id1
        main_id = entity_id2

        # Set the main id
        if main_entity_ml_id is not None:
            update_main_query = """
            UPDATE city_ml_table
            SET is_main = %s
            WHERE city_ml_id = %s
            """
            execute_sql_query(conn, cursor, True, main_entity_ml_id, update_main_query)

        # look for the former in id of city_ml_table and replace it with the latter

        # Define the SQL UPDATE statement
        update_query = """
        UPDATE city_ml_table
        SET city_id = %s
        WHERE city_id = %s
        """

        # Data to update
        old_id = end_id
        new_id = main_id

        execute_sql_query(conn, cursor, new_id, old_id, update_query)

        end_timestamp_query = """
        UPDATE city_table
        SET end_timestamp = %s
        WHERE city_id = %s
        """

        execute_sql_query(conn, cursor, datetime.datetime.now(), old_id, end_timestamp_query)



    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(error)
    finally:
        # Close the cursor and connection
        cursor.close()
        conn.close()


def execute_sql_query(conn1, cursor2, new_id, old_id, update_query):
    # Execute the SQL statement
    cursor2.execute(update_query, (new_id, old_id))
    # Commit the transaction
    conn1.commit()
    # Check if the update was successful
    if cursor.rowcount > 0:
        print("Update successful")
    else:
        print("No records updated")
        exit()










