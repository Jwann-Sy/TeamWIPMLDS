"""
_____________________ DATABASE OPERATIONS FUNCTIONS: _______________________

These functions will pass information into the database for particular circumstances.
All variables being passed through these functions must be strings. So, if you are
passing an integer, make sure to convert it into a string before passing it.

"""

# for database access
import mysql.connector

# _______________________ INSERT FUNCTION __________________________________
# To be used when a ranger needs to identify a sound. Only use ranger_id
# and sensor_id that are in the ranger and sensor databases (see database
# document). Classifications can be 'definite', 'suspected', or 'false'.


# inserts an 'event' entry, given a ranger_id, classification, and sensor_id
def insert(classif, sensor_id, ranger_id):
    servername = "SG-mldb7sdsu-7331-mysql-master.servers.mongodirector.com"
    username = "testuser1"
    password = "ON***user1"
    database = "mldb"

    # Database cursor and connection objects are created.
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)
    cursor = cnx.cursor()

    # Query does an INSERT into the database using variables passed.
    query = 'INSERT INTO mldb.event(class, sensor_id, ranger_id)'\
            'VALUES(%s, %s, %s)'
    insert_data = (classif, sensor_id, ranger_id)
    cursor.execute(query, insert_data)

    # Commits changes
    cnx.commit()

    # Closes database
    cnx.close()


# _______________________ MAIN ____________________________________________
if __name__ == '__main__':

    classif = 'definite'
    sensor_id = '1001'
    ranger_id = '1213'

    # Inserts new event, given a classification, sensor id, & ranger id
    insert(classif, sensor_id, ranger_id)
