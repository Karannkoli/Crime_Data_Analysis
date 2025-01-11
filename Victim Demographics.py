import pymysql
import matplotlib.pyplot as plt

try:
                # Establish a connection to the MySQL database
                conn = pymysql.connect(host="127.0.0.1",
                                       user="root",
                                       password="Vedant@2001",
                                       database="crime_database")

                # Execute SQL query to investigate the distribution of victim ages
                cursor = conn.cursor()
                age_query = """
                SELECT Vict_Age, COUNT(*) AS Age_Count
                FROM crime_database
                WHERE Vict_Age IS NOT NULL
                GROUP BY Vict_Age
                ORDER BY Vict_Age;
                """
                cursor.execute(age_query)
                age_results = cursor.fetchall()

                # Extract age data from results
                ages = [result[0] for result in age_results]
                age_counts = [result[1] for result in age_results]

                # Plotting victim age distribution
                plt.figure(figsize=(10, 6))
                plt.bar(ages, age_counts, color='skyblue')
                plt.title('Victim Age Distribution')
                plt.xlabel('Age')
                plt.ylabel('Count')
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                # Execute SQL query to investigate the distribution of victim genders
                gender_query = """
                SELECT Vict_Sex, COUNT(*) AS Gender_Count
                FROM crime_database
                WHERE Vict_Sex IS NOT NULL
                GROUP BY Vict_Sex;
                """
                cursor.execute(gender_query)
                gender_results = cursor.fetchall()

                # Extract gender data from results
                genders = [result[0] for result in gender_results]
                gender_counts = [result[1] for result in gender_results]

                # Plotting victim gender distribution
                plt.figure(figsize=(6, 6))
                plt.pie(gender_counts, labels=genders, autopct='%1.1f%%', startangle=140,
                        colors=['lightcoral', 'lightskyblue'])
                plt.title('Victim Gender Distribution')
                plt.axis('equal')
                plt.tight_layout()
                plt.show()

                # Close cursor and connection
                cursor.close()
                conn.close()

except pymysql.Error as e:
                print("Error:", e)
