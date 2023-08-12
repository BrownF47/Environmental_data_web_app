import requests
import json


# Load API keys #

config = open('.config.json')
config_data = json.load(config)

# API to access met office server #

API_KEY = config_data['MET_OFFICE_API_KEY']


def get_temperature_data(api_key):
    base_url = 'http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/'

    # UK location ID for temperature data
    location_id = '310042'  # UK

    # Parameters for temperature observation data
    params = {
        'res': 'hourly',
        'key': api_key
    }

    url = f"{base_url}/{location_id}"

    # currently just using a hard coded url to get data #

    # data is observations from the past 24 hours #

    try:
        #response = requests.get(url, params=params)
        response = requests.get(f'http://datapoint.metoffice.gov.uk/public/data/val/wxobs/all/json/3772?res=hourly&key={API_KEY}')
        response.raise_for_status()
        #print(response.text)
        data = response.json()
        return data['SiteRep']['DV']['Location']['Period']
    except requests.exceptions.RequestException as e:
        print(f"Error accessing data: {e}")
        return None

# data is saved to a json file #

def save_temperature_data_to_json(data):
    if not data:
        return
    
    with open('temperature_data_uk.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)        


if __name__ == "__main__":
    temperature_data = get_temperature_data(API_KEY)
    if temperature_data:
        save_temperature_data_to_json(temperature_data)
        print("Temperature data collected and saved to temperature_data_uk.json")
    else:
        print("Failed to retrieve temperature data.")


        
