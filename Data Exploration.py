import pymysql

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="Vedant@2001",
                           database="crime_database")
    # Execute SQL queries to retrieve basic statistics
    cursor = conn.cursor()

    # Total number of records in the dataset
    query_total_records = "SELECT COUNT(*) FROM crime_database;"
    cursor.execute(query_total_records)
    total_records = cursor.fetchone()[0]
    print("Total number of records:", total_records)

    # Unique values in specific columns
    columns_to_analyze = ['AREA_NAME', 'Crm_Cd_Desc', 'Vict_Sex', 'Status']  # Add more columns as needed
    for column in columns_to_analyze:
        query_unique_values = f"SELECT COUNT(DISTINCT {column}) FROM crime_database;"
        cursor.execute(query_unique_values)
        unique_values_count = cursor.fetchone()[0]
        print(f"Number of unique values in {column}: {unique_values_count}")

    # Close cursor and connection
    cursor.close()
    conn.close()

except pymysql.Error as e:
    print("Error:", e)
