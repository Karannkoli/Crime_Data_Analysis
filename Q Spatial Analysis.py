import pymysql
import matplotlib.pyplot as plt

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="Vedant@2001",
                           database="crime_database")

    # Execute SQL query to find geographical hotspots for reported crimes
    with conn.cursor() as cursor:
        hotspot_query = """
        SELECT LAT, LON, COUNT(*) AS Crime_Count
        FROM crime_database
        GROUP BY LAT, LON
        ORDER BY Crime_Count DESC;
        """
        cursor.execute(hotspot_query)
        hotspot_results = cursor.fetchall()

        # Extracting latitude, longitude, and crime counts for plotting
        latitudes = [result[0] for result in hotspot_results]
        longitudes = [result[1] for result in hotspot_results]
        crime_counts = [result[2] for result in hotspot_results]

        # Print out the geographical hotspots for reported crimes
        print("Geographical Hotspots for Reported Crimes:")
        for lat, lon, count in hotspot_results:
            print(f"Latitude: {lat}, Longitude: {lon}, Crime Count: {count}")

        # Plotting the geographical hotspots
        plt.figure(figsize=(10, 8))
        plt.scatter(longitudes, latitudes, s=crime_counts, alpha=0.5)
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Geographical Hotspots for Reported Crimes')
        plt.show()

except pymysql.Error as e:
    print("Error:", e)

finally:
    if conn:
        conn.close()
