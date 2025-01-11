import pymysql
import matplotlib.pyplot as plt
try:
            # Establish a connection to the MySQL database
            conn = pymysql.connect(host="127.0.0.1",
                                   user="root",
                                   password="Vedant@2001",
                                   database="crime_database")

            # Execute SQL query to retrieve latitude and longitude information
            cursor = conn.cursor()
            query = """
            SELECT LAT, LON FROM crime_database;
            """
            cursor.execute(query)
            results = cursor.fetchall()

            # Extract latitude and longitude data from results
            latitudes = [result[0] for result in results if result[0] is not None]
            longitudes = [result[1] for result in results if result[1] is not None]

            # Close cursor and connection
            cursor.close()
            conn.close()

            # Plotting crime hotspots on a map
            plt.figure(figsize=(10, 8))
            plt.scatter(longitudes, latitudes, s=10, alpha=0.5)
            plt.title('Crime Hotspots')
            plt.xlabel('Longitude')
            plt.ylabel('Latitude')
            plt.grid(True)
            plt.tight_layout()
            plt.show()

except pymysql.Error as e:
            print("Error:", e)
