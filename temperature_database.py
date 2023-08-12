import sqlite3
import visualise_json
import numpy as np

def insert_temperature_data(temperature_data):

    # Connect to the database (creates a new database if not exists) 
    conn = sqlite3.connect('temp_db')

    # Create a cursor object to execute SQL commands 
    cursor = conn.cursor()

    # prep data for insertion 

    #load in data
    temp_data = visualise_json.load_data_from_json(temperature_data)

    #turn into writable form 
    timestamps, temperatures = visualise_json.extract_timestamps_and_temperatures(temp_data) 
    
    if len(timestamps) == len(temperatures):
        data_to_add = np.vstack([timestamps, temperatures])
    else:
        print('Times and temps not equal')
    #print(np.shape(data_to_add))
    
    # delete current data from table 

    #cursor.execute("DELETE FROM temperature")

    for row in data_to_add.T:

        time = row[0]
        temp = row[1]

    # Execute a query 
    #cursor.execute("INSERT INTO temperature_data (timestamp, temperature) VALUES (?, ?)", )
        #print(time)
        #print(temp)
        cursor.execute("CREATE TABLE IF NOT EXISTS temperature (timestamp TEXT, temperature REAL);")

        query = f"INSERT INTO temperature (timestamp, temperature) VALUES (\"{time}\", {temp});"

        cursor.execute(query)

    cursor.execute("SELECT * FROM temperature")

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)


    # this 'saves' the database in the new state #

    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()
    print('SQLite Connection closed')

if __name__ == "__main__":
    json_data = 'temperature_data_uk.json'
    insert_temperature_data(json_data)