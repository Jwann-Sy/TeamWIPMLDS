import matplotlib.pyplot as plt
import mysql.connector

# ============= SENSOR DATA TO LIST =======================================
# This function takes latitude, longitude, and sensor hit count values and
# assigns them to their respective lists. The function appends to the lists
# created outside the scope of the function, in the main function.
#
# INPUT: None
# OUTPUT: longitudes list, latitudes list, sensor counts list, month count list
# ==========================================================================
def sensor_data_to_list():
    servername = "SG-mldb7sdsu-7331-mysql-master.servers.mongodirector.com"
    username = "testuser1"
    password = "ON***user1"
    database = "mldb"

    cnx = mysql.connector.connect(user=username,
                                  password=password,
                                  host=servername,
                                  port=3306,
                                  database=database)

    # A cursor for each query.
    cursor1 = cnx.cursor()
    cursor2 = cnx.cursor()

    # Query finds events made within the last 30 days
    cursor1.execute("SELECT longitude, latitude, COUNT(*) \
                     FROM mldb.event, mldb.sensor \
                     WHERE sensor_id = sensor.id \
                     GROUP BY sensor_id \
                     ORDER BY sensor_id;")

    # Lists of sensor column values.
    long = []           # longitude
    lat = []            # latitude
    count = []          # total sensor counts
    month_count = []    # sensor counts per month

    # Appends sensor values to lists, and converts Decimal() to float.
    for db in cursor1:
        long.append(float(db[0]))
        lat.append(float(db[1]))
        count.append(db[2])

    # Closes cursor 1
    cursor1.close()

    # Query finds the sensor count for 30 day 'definite' entries
    cursor2.execute("SELECT longitude, latitude, COUNT(*) \
                    FROM mldb.event, mldb.sensor \
                    WHERE sensor_id = sensor.id AND class = 'definite' \
                    AND (DATE(adddate(curdate(), interval -30 day)) \
                    AND date_time <= DATE(curdate())) \
                    GROUP BY sensor_id \
                    ORDER BY sensor_id;")

    for db in cursor2:
        month_count.append(db[2])

    # closes database
    cnx.close()

    return long, lat, count, month_count


# ============= GRAPHICAL REPORT ===========================================
# This function creates a scatter plot over an image of a map. The plot axes
# are aligned to the map's lat/long proportions. Plots longitude and latitude
# and colors points by value of count.
# Note: May need to pass other functions
#
# INPUT: long[], lat[], count[].
# OUTPUT: Graphical Report
# ==========================================================================
def graphical_report(long, lat, count, month_ct):
    # Scaling values to have readable circle sizes.
    big_month_ct = [i * 120 for i in month_ct]

    # Defines graph style
    plt.style.use('seaborn')

    # Plot axes bounds
    BBox = (-117.1214, -116.9707, 32.7783, 32.8868)

    # Reads image
    mtrp_map = plt.imread('mtrp.png')

    # Formats plot
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(long, lat, zorder=1, c=count, s=big_month_ct, cmap='autumn_r',
               linewidth=0.5, edgecolor='black', alpha=0.5)
    ax.set_title('Mission Trails Mountain Lion Sightings')
    ax.set_xlim(BBox[0], BBox[1])
    ax.set_ylim(BBox[2], BBox[3])
    ax.imshow(mtrp_map, zorder=0, extent=BBox, aspect='equal')


    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.show()


# Ensures correct values are being passed to the correct lists.
def unit_test_1():
    print("longitudes list:")
    print(longitude)

    print("\nlatitudes list:")
    print(latitude)

    print("\nsensor counts: ")
    print(sensor_count)


if __name__ == '__main__':
    # Returns list of sensor values from db
    longitude, latitude, sensor_count, sensor_month_count = sensor_data_to_list()

    # Creates plots the lists generated onto a map
    graphical_report(longitude, latitude, sensor_count, sensor_month_count)





