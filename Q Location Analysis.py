import pymysql
import matplotlib.pyplot as plt

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="Vedant@2001",
                           database="crime_database")

    # Determine where most crimes occur based on the "Location" column
    with conn.cursor() as cursor:
        location_query = """
        SELECT Location, COUNT(*) AS Crime_Count
        FROM crime_database
        WHERE Location IS NOT NULL
        GROUP BY Location
        ORDER BY Crime_Count DESC;
        """
        cursor.execute(location_query)
        location_results = cursor.fetchall()

        # Extracting locations and crime counts for plotting
        locations = [location[0] for location in location_results]
        crime_counts = [count[1] for count in location_results]

        # Print out where most crimes occur
        print("Locations Where Most Crimes Occur:")
        for location, count in location_results:
            print(f"Location: {location}, Crime Count: {count}")

        # Plotting the locations where most crimes occur
        plt.figure(figsize=(10, 6))
        plt.bar(locations[:10], crime_counts[:10], color='skyblue')
        plt.xlabel('Location')
        plt.ylabel('Crime Count')
        plt.title('Locations Where Most Crimes Occur')
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

except pymysql.Error as e:
    print("Error:", e)

finally:
    if conn:
        conn.close()
