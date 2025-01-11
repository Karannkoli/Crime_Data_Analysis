import pymysql
import matplotlib.pyplot as plt

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="Vedant@2001",
                           database="crime_database")

    # Analyze the distribution of reported crimes based on Crime Code
    with conn.cursor() as cursor:
        crime_code_query = """
        SELECT Crm_Cd, Crm_Cd_Desc, COUNT(*) AS Crime_Count
        FROM crime_database
        WHERE Crm_Cd IS NOT NULL
        GROUP BY Crm_Cd, Crm_Cd_Desc
        ORDER BY Crime_Count DESC;
        """
        cursor.execute(crime_code_query)
        crime_code_results = cursor.fetchall()

        # Extracting crime codes, descriptions, and crime counts for plotting
        crime_codes = [result[0] for result in crime_code_results]
        descriptions = [result[1] for result in crime_code_results]
        crime_counts = [result[2] for result in crime_code_results]

        # Print out the distribution of reported crimes based on Crime Code
        print("Distribution of Reported Crimes Based on Crime Code:")
        for code, description, count in crime_code_results:
            print(f"Crime Code: {code}, Description: {description}, Crime Count: {count}")

        # Plotting the distribution of reported crimes based on Crime Code
        plt.figure(figsize=(12, 8))
        plt.barh(descriptions[:10], crime_counts[:10], color='skyblue')
        plt.xlabel('Crime Count')
        plt.ylabel('Crime Description')
        plt.title('Distribution of Reported Crimes Based on Crime Code')
        plt.gca().invert_yaxis()  # Invert y-axis to display top crimes at the top
        plt.tight_layout()  # Adjust layout to prevent clipping of labels
        plt.show()

except pymysql.Error as e:
    print("Error:", e)

finally:
    if conn:
        conn.close()
