# Crime_Data_Analysis
In this capstone project, we will use Python, specifically the PyMySQL library, to interact with a MySQL database in order to analyze and gain insights from crime data. The dataset includes information such as DR NO, Date Reported, Date Occurred, Area Name, Crime Code, Crime Code Description, Victim Age, Victim Sex, Premises Description, Status, Location, Latitude, and Longitude.

# Crime Data Analysis Using Python and MySQL

This project involves analyzing crime data by connecting to a MySQL database, performing data exploration, and conducting temporal, spatial, and demographic analysis. The analysis is conducted using Python libraries like `PyMySQL`, `Matplotlib`, and `Seaborn` to generate meaningful insights from the data.

## Objectives:

1. **Database Setup and Import:**
   - Create a MySQL database.
   - Load the provided crime dataset into the MySQL database.

2. **Database Connection:**
   - Establish a connection to the database using `PyMySQL` in Python.
   - Verify successful import and connection using basic queries in Python.

3. **Data Exploration:**
   - Retrieve basic statistics such as the total number of records and unique values.
   - Identify distinct crime codes and their descriptions.

4. **Temporal Analysis:**
   - Analyze crime occurrence trends over time.
   - Determine crime trends based on time (e.g., year, month).

5. **Spatial Analysis:**
   - Perform spatial analysis using geographical information (Latitude and Longitude).
   - Visualize crime hotspots on a map.

6. **Victim Demographics:**
   - Investigate victim demographics, including age and gender.
   - Identify common premises descriptions where crimes occur.

7. **Status Analysis:**
   - Analyze the status of reported crimes (e.g., classified based on their current status).

## Key Questions Addressed:
- **Spatial Analysis**: Where are the geographical hotspots for reported crimes?
- **Victim Demographics**: What is the distribution of victim ages and genders in reported crimes? Is there a significant difference in crime rates between male and female victims?
- **Location Analysis**: Where do most crimes occur based on the "Location" column?
- **Crime Code Analysis**: What is the distribution of reported crimes based on Crime Code?

## Tools and Libraries:
- Python (PyCharm/VS Code for development)
- `PyMySQL` for connecting to MySQL
- `Matplotlib` and `Seaborn` for data visualization
- MySQL Server (for running the database)
- MySQL Workbench (or similar) for database management

## Setup and Installation:

1. **Install required libraries**:
   - Install Python libraries using pip:
     ```bash
     pip install pymysql matplotlib seaborn
     ```

2. **Database Setup**:
   - Install MySQL server and create a database (use MySQL Workbench or CLI).
   - Import the crime dataset into the MySQL database.

3. **Running the Scripts**:
   - Clone or download this repository.
   - Run the Python scripts to establish a connection, perform analysis, and visualize the results.

4. **Database Connection**:
   - Ensure your MySQL server is running and you have access credentials to connect via Python.

## Deliverables:
- Python scripts for database setup, data import, and analysis.
- Visualizations and insights derived from the analysis.
  
## Notes:
- Ensure that your MySQL server is running and accessible for the scripts to connect.
- Modify connection settings in the script if necessary (e.g., username, password, database name).

## Example Visualizations:
- **Crime Hotspot Map**: A visualization showing the locations of high crime rates.
- **Crime Trend Graphs**: Time-based visualizations showing the increase or decrease in crime frequency.
- **Victim Demographics**: Distribution of victims by age and gender.

## License:
This project is licensed under the MIT License.

## Acknowledgements:
- The crime dataset used in this project is available in files.


