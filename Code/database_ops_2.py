"""
_____________________ DATABASE OPERATIONS FUNCTIONS: _______________________

These functions will pass information into the database for particular circumstances.
All variables being passed through these functions must be strings. So, if you are
passing an integer, make sure to convert it into a string before passing it.

FUNCTIONS:

insert() --- Creates an entry with the classification, sensor id, ranger_id
    and current time on the computer.

insert_sensor() --- Creates a new entry by with the sensor id and current
    date and time.

edit_classif() --- Edits the classification of an already existing entry. Takes
    in the event id, classification, and ranger id

cur_time() --- Function that returns the current time in a database formatted
    string.

"""

# for database access
import mysql.connector

# for datetime objects
import datetime
from datetime import datetime

# _______________________ INSERT FUNCTION __________________________________
# To be used when a ranger needs to identify a sound. Only use ranger_id
# and sensor_id that are in the ranger and sensor databases (see database
# document). Classifications can be 'definite', 'suspected', or 'false'.


# inserts an 'event' entry, given a ranger_id, classification, and sensor_id
def insert(classif, sensor_id, ranger_id):
    # stores current computer time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

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
    cursor = cnx.cursor()

    # Query does an INSERT into the database using variables passed.
    query = 'INSERT mldb.event(class, date_time, sensor_id, ranger_id)'\
            'VALUES(%s, %s, %s, %s)'
    insert_data = (classif, date_time, sensor_id, ranger_id)
    cursor.execute(query, insert_data)

    # Commits changes
    cnx.commit()

    # Closes database
    cnx.close()

# ======================= INSERT SENSOR FUNCTION ==========================
# Inserts sensor_id into a database, creating an event.
def insert_sensor(sensor_id):
    # stores current computer time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

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
    cursor = cnx.cursor()

    # Query does an INSERT into the database using variables passed.
    query = 'INSERT mldb.event(sensor_id, date_time)'\
            'VALUES(%s, %s)'
    insert_data = (sensor_id, date_time)
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


# _______________________ CURRENT TIME FUNCTION ___________________________
# Returns the current time as a string, formatted for database insertion
# as a DATETIME variable.
def cur_time():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
    # print("date and time =", dt_string)

    return dt_string


# _______________________ MAIN ____________________________________________
if __name__ == '__main__':
    # test variables
    classif = 'definite'
    new_classif = 'suspected'
    sensor_id = '1003'
    ranger_id = '1415'
    event_id = '8'

    # ======= INSERT ENTRY ===========================
    # Inserts new event, given a classification, sensor id, & ranger id
    # insert(classif, sensor_id, ranger_id)

    # ======= INSERT SENSOR ==========================
    # Creates an event entry with the sensor_id
    # insert_sensor(sensor_id)

    # ======= EDIT CLASSIFICATION ====================
    # edit_classif(event_id, new_classif, ranger_id)

    # ======= DATE TIME ==============================
    # cur_time()
