import pymysql
import matplotlib.pyplot as plt

try:
    # Establish a connection to the MySQL database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="Vedant@2001",
                           database="crime_database")

    # Retrieve the distribution of victim ages in reported crimes
    with conn.cursor() as cursor:
        age_query = """
        SELECT Vict_Age, COUNT(*) AS Age_Count
        FROM crime_database
        WHERE Vict_Age IS NOT NULL
        GROUP BY Vict_Age
        ORDER BY Vict_Age;
        """
        cursor.execute(age_query)
        age_results = cursor.fetchall()

        # Extracting ages and counts for command-line output
        print("Distribution of Victim Ages in Reported Crimes:")
        for age, count in age_results:
            print(f"Age: {age}, Count: {count}")

        # Extracting ages and counts for plotting
        ages = [age[0] for age in age_results]
        age_counts = [count[1] for count in age_results]

        # Plotting the distribution of victim ages
        plt.figure(figsize=(10, 6))
        plt.bar(ages, age_counts, color='skyblue')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.title('Distribution of Victim Ages in Reported Crimes')
        plt.show()

    # Retrieve the distribution of victim genders in reported crimes
    with conn.cursor() as cursor:
        gender_query = """
        SELECT Vict_Sex, COUNT(*) AS Gender_Count
        FROM crime_database
        WHERE Vict_Sex IS NOT NULL
        GROUP BY Vict_Sex;
        """
        cursor.execute(gender_query)
        gender_results = cursor.fetchall()

        # Extracting genders and counts for command-line output
        print("\nDistribution of Victim Genders in Reported Crimes:")
        for gender, count in gender_results:
            print(f"Gender: {gender}, Count: {count}")

        # Extracting genders and counts for plotting
        genders = [gender[0] for gender in gender_results]
        gender_counts = [count[1] for count in gender_results]

        # Plotting the distribution of victim genders
        plt.figure(figsize=(6, 6))
        plt.pie(gender_counts, labels=genders, autopct='%1.1f%%', colors=['lightcoral', 'lightskyblue'])
        plt.title('Distribution of Victim Genders in Reported Crimes')
        plt.show()

    # Compare the crime rates between male and female victims
    with conn.cursor() as cursor:
        male_female_query = """
        SELECT Vict_Sex, COUNT(*) AS Gender_Count
        FROM crime_database
        WHERE Vict_Sex IN ('M', 'F')
        GROUP BY Vict_Sex;
        """
        cursor.execute(male_female_query)
        male_female_results = cursor.fetchall()

        # Extracting genders and counts for command-line output
        print("\nComparison of Crime Rates between Male and Female Victims:")
        for gender, count in male_female_results:
            print(f"Gender: {gender}, Crime Count: {count}")

        # Extracting genders and counts for plotting
        genders = [gender[0] for gender in male_female_results]
        gender_counts = [count[1] for count in male_female_results]

        # Plotting the comparison of crime rates between male and female victims
        plt.figure(figsize=(6, 6))
        plt.bar(genders, gender_counts, color=['blue', 'pink'])
        plt.xlabel('Gender')
        plt.ylabel('Crime Count')
        plt.title('Comparison of Crime Rates between Male and Female Victims')
        plt.show()

except pymysql.Error as e:
    print("Error:", e)

finally:
    if conn:
        conn.close()

