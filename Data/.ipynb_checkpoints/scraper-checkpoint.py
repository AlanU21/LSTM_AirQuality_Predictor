import requests
import pandas as pd
from time import sleep

df = pd.DataFrame(list())
df.to_excel("data1.xlsx")

key = 'cd48675ad56e8c27e34745bb49fd7730d88a65a44c752ac3a8854c1f7aa3a620'

def fetch_data(param, date_from, date_to, city, country, limit=10000, sort='asc'):
    url = 'https://api.openaq.org/v2/measurements'
    query = {
        'date_from': date_from,
        'date_to': date_to,
        'parameter': param,
        'city': city,
        'country': country,
        'limit': limit,
        'sort': sort,
        'X-API-Key': key
    }
    
    
    response = requests.get(url, params=query)
    if response.status_code == 200:
        try:
            data = response.json()
            df = pd.DataFrame(data['results'])
            df.drop('unit', axis=1, inplace=True)
            df.drop('locationId', axis=1, inplace=True)
            return df
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return pd.DataFrame()
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return pd.DataFrame()

parameters = ['pm25', 'pm10']
date_from = '2023-01-01'
date_to = '2024-01-01'
city = 'PHILADELPHIA'
country = 'US'

for param in parameters:
    print(f"\nPARAM: {param}\n")
    air_quality_data = fetch_data(param, date_from, date_to, city, country)
    if not air_quality_data.empty:
        new_date_column = air_quality_data['date'].apply(lambda x: x.get('utc'))
        air_quality_data['date'] = new_date_column
        with pd.ExcelWriter("data1.xlsx", mode='a', engine='openpyxl') as writer:
            air_quality_data.to_excel(writer, sheet_name=param)
            print("Success")

        sleep(5)

    else:
        print("DataFrame empty")