"""
_____________________ DATABASE OPERATIONS FUNCTIONS: _______________________

These functions will pass information into the database for particular circumstances.
All variables being passed through these functions must be strings. So, if you are
passing an integer, make sure to convert it into a string before passing it.

"""

# for database access
import mysql.connector
import db_reports

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


# _______________________ EDIT FUNCTION ___________________________________
def edit_classif(event_id, new_classif, ranger_id):
    # Connection variables
    servername = "SG-mldb7sdsu-7331-mysql-master.servers.mongodirector.com"
    username = "testuser1"
    password = "ON***user1"
    database = "mldb"

    # Database cursor and connection objects are created.
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database,
                                  autocommit=True)

    cursor1 = cnx.cursor()
    cursor2 = cnx.cursor()

    # Query 1: Updates classification
    query1 = 'UPDATE mldb.event ' \
             'SET class = %s ' \
             'WHERE (id = %s)'

    insert_data1 = (new_classif, event_id)
    cursor1.execute(query1, insert_data1)

    # Query 2: Updates ranger id
    query2 = 'UPDATE mldb.event ' \
             'SET ranger_id = %s ' \
             'WHERE (id = %s)'

    insert_data2 = (ranger_id, event_id)
    cursor2.execute(query2, insert_data2)

    # Commits changes
    cnx.commit()

    # Closes database
    cnx.close()
