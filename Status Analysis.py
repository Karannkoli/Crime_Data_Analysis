import pymysql

try:
                # Establish a connection to the MySQL database
                conn = pymysql.connect(host="127.0.0.1",
                                       user="root",
                                       password="Vedant@2001",
                                       database="crime_database")

                # Execute SQL query to examine the status of reported crimes
                cursor = conn.cursor()
                status_query = """
                SELECT Status, COUNT(*) AS Crime_Count
                FROM crime_database
                GROUP BY Status;
                """
                cursor.execute(status_query)
                status_results = cursor.fetchall()

                # Print out the status of reported crimes and their counts
                print("Status of Reported Crimes:")
                for status, count in status_results:
                    print(f"{status}: {count}")

                # Close cursor and connection
                cursor.close()
                conn.close()

except pymysql.Error as e:
                print("Error:", e)
