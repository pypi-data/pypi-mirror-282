import datetime

import mysql.connector
from mysql.connector import errorcode
import connector
import generic_crud
import generic_crud_ml

def merge_entities(entity_id1: int, entity_id2: int, main_entity_ml_id: int = None):
    global conn, cursor
    try:
        # Connect to the MySQL database
        conn = connector.Connector.connect('location',)
        cursor = conn.cursor()

        # establish which id is being merged/ended and which one it is being merged into
        end_id = entity_id1
        main_id = entity_id2

        # Set the main id
        if main_entity_ml_id is not None:
            generic_crud_ml.GenericCRUDML.update_value_by_id(
                table_name="city_table",
                ml_table_name="city_ml_table",
                ml_table_id=main_entity_ml_id,
                is_main=True,
            )

        # look for the former in id of city_ml_table and replace it with the latter

        # Data to update
        old_id = end_id
        new_id = main_id

        generic_crud_ml.GenericCRUDML.update_value_by_id(
            table_name="city_table",
            ml_table_name="city_ml_table",
            ml_table_id= old_id,
            data_ml_dict={"city_id": new_id},
        )

        generic_crud.GenericCRUD.update_by_column_and_value(
            table_name="city_table",
            column_name="city_id",
            column_value=old_id,
            data_dict={"end_timestamp": datetime.datetime.now()},
        )



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










