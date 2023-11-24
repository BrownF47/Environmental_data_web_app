import json
import matplotlib.pyplot as plt
import datetime

# opens and loads in data from json file #

def load_data_from_json(json_file):
    f = open(json_file)
    data = json.load(f)
    return data

# get dates and times of temp data from last 24 hours, this will need to be stored in some kind of data base #

def extract_timestamps_and_temperatures(data):
    timestamps = []
    temperatures = []
    #print(data)
    for day in data:
        #print(day['value'])
        the_day = day['value']

        for observation in day['Rep']:
            try:
                #timestamp = datetime.datetime.strptime(observation['$'], '%H%M')
                #print(datetime.datetime.strptime(the_day + observation['$'], '%Y-%M-%dZ %H%M'))
                hours = round(float(observation['$'])/60)

                timestamp = (datetime.datetime.strptime(the_day+str(hours), '%Y-%m-%dZ%H'))
                temperature = float(observation['T'])
                
                timestamps.append(timestamp)
                temperatures.append(temperature)
            except:
                print(f'missing temperatre data at {timestamp}' )

    return timestamps, temperatures

# visualises temperature data #

def plot_temperature_data(timestamps, temperatures):
    #print(timestamps)
    #print(temperatures)
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b')
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('Temperature Data for 24 period')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('Environmental_data_website/assets/img/portfolio/Temp_graph.png')
    plt.show()

if __name__ == "__main__":
    json_data = 'temperature_data_uk.json' # Replace this with the actual JSON data
    data = load_data_from_json(json_data)
    timestamps, temperatures = extract_timestamps_and_temperatures(data)
    plot_temperature_data(timestamps, temperatures)






#f = open('temperature_data_uk.json')
#data  = json.load(f)
