"""
__________________Database Reports Generator____________________________
This program will print 6 of the 7 required reports. The reports are
numbered as such:

- Report 1: Returns all entries made within the last 30 days.

- Report 2: Alert Summary of all entries made
    - > 30 days
    - <= 365 days

- Report 3: Returns all entries ordered by most recent date first.

- Report 4: Returns all entries with a specific classification.

- Report 5: Returns all entries made by a specific sensor.

- Report 6: Returns all entries made by a specific ranger.

- Report 7: Returns a graphical report that includes:
    - Map of park
    - Sensor plot points
    - Color coded plot points that show a 'heat map' of entries at each
    sensor location.
    - Summary info underneath the graphical report.
------------------------------------------------------------------------
"""

# for database access
import mysql.connector

# Connection credentials
servername = "SG-mldb7sdsu-7331-mysql-master.servers.mongodirector.com"
username = "testuser1"
password = "ON***user1"
database = "mldb"


# Prints all events made within 30 days.
def report_1():
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)

    # Query finds events made within the last 30 days
    mycursor = cnx.cursor()
    mycursor.execute("SELECT * FROM mldb.event \
                    WHERE date_time >= \
                    DATE(adddate(curdate(), interval -30 day)) \
                    AND date_time <= DATE(curdate())")
    # Prints entries made within the last 30 days
    report = ""
    for db in mycursor:
        # print(db[0], db[1], db[2], db[3], db[4])
        report += str(db).rstrip() + "\n"

    # closes database
    cnx.close()
    return report


# Prints month-to-year summary of alert events
def report_2():
    # Stores total number of events
    total_events = 0

    # Stores total number of events in each classification
    total_by_class = []

    # Stores total number of events by each sensor
    total_by_sensor = []

    report = "MONTH TO YEAR SUMMARY:\n"

    # Connects to database

    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)
    # Define cursor objects
    cursor1 = cnx.cursor()
    cursor2 = cnx.cursor()
    cursor3 = cnx.cursor()

    # Query returns the month-to-year out number of events
    cursor1.execute("SELECT COUNT(*) \
                   FROM mldb.event \
                   WHERE date_time >= \
                   DATE(adddate(curdate(), interval -365 day)) \
                   AND date_time <= DATE(adddate(curdate(), interval -30 day));")

    # Prints number of events
    for event in cursor1.fetchall():
        report += "Number of total alerts: " + str(event[0])

    # Query returns the month-to-year out number of events by sensor
    cursor2.execute("SELECT sensor_id, location_name, COUNT(*) \
                    FROM mldb.event, mldb.sensor \
                    WHERE sensor_id = sensor.id\
                    AND date_time >= \
                    DATE(adddate(curdate(), interval -365 day))\
                    AND date_time <= DATE(adddate(curdate(), interval -30 day))\
                    GROUP BY location_name;")

    # Prints number of entries made by each sensor
    report += "\nNumber of alerts by sensor location:\n"
    for sensor in cursor2.fetchall():
        report += "\t\t" + str(sensor[1]) + "=" + str(sensor[2]) + "\n"

    # Query counts number of month-to-year events by classification
    cursor3.execute("SELECT class, COUNT(*) \
                    FROM mldb.event \
                    WHERE date_time >= \
                    DATE(adddate(curdate(), interval -365 day)) \
                    AND date_time <= DATE(adddate(curdate(), interval -30 day)) \
                    GROUP BY class;")

    # Prints number of entries by classification
    report += "Number of alerts by classification:\n"
    for classif in cursor3.fetchall():
        report += "\t\t" + str(classif[0]) + "=" + str(classif[1]) + "\n"

    # Closes connection
    cnx.close()
    return report


# Prints all entries from most recent to least recent.
def report_3():
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)

    # Prints view of 30 day report
    mycursor = cnx.cursor()
    mycursor.execute("SELECT * FROM mldb.event \
                        ORDER BY date_time DESC;")
    report = ""
    for event in mycursor:
        report += str(event).rstrip() + "\n"

    # closes database
    cnx.close()
    return report


# Prints entries of a specific classification.
def report_4(classification):
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)
    # Define cursor object
    cursor = cnx.cursor()

    # Query prep
    query = ('SELECT * FROM mldb.event '
             'WHERE class = %s '
             'ORDER BY date_time DESC')
    classification_data = (classification,)

    # Execute query
    cursor.execute(query, classification_data)

    report = ""
    # Prints events
    for event in cursor.fetchall():
        report += str(event).rstrip() + "\n"

    # Closes connection
    cnx.close()
    return report


# Prints entries made by a specific sensor
def report_5(sensor_id):
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)
    # Define cursor object
    cursor = cnx.cursor()

    # Query prep
    query = ('SELECT * FROM mldb.event '
             'WHERE sensor_id = %s '
             'ORDER BY date_time DESC')
    sensor_data = (sensor_id,)

    # Execute query
    cursor.execute(query, sensor_data)

    report = ""
    # Print events
    for event in cursor.fetchall():
        report += str(event).rstrip() + "\n"

    # closes database
    cnx.close()
    return report

# Prints entries made by a specific ranger
def report_6(ranger_id):
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)
    # Define cursor object
    cursor = cnx.cursor()

    # Query prep
    query = ('SELECT * FROM mldb.event '
             'WHERE ranger_id = %s '
             'ORDER BY date_time DESC')
    ranger_data = (ranger_id,)

    # Execute query
    cursor.execute(query, ranger_data)

    report = ""
    # Prints events
    for event in cursor.fetchall():
        report += str(event).rstrip() + "\n"

    # Closes connection
    cnx.close()
    return report


def report_7():
    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)

    # Cursor to find longitude/latitude values
    # Cursor to find number of hits at each 
    cursor_coor = cnx.cursor()
    cursor_quantity = cnx.cursor()

    cursor_coor.execute("SELECT * FROM mldb.sensor;")

    # Prints entries made within the last 30 days
    for db in cursor_coor:
        # print(db[0], db[1], db[2], db[3], db[4])
        print(db)

    # closes database
    cnx.close()


# # _______________________ MAIN ____________________________________________
# if __name__ == '__main__':
#     report1 = report_2()
#     print(report1)
