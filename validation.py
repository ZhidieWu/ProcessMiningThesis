import json
import random
import time
import requests
import pandas as pd
import numpy as np

# ## LHR_AMS
df = pd.read_csv('Data/LHR_AMS.csv', sep=";", parse_dates=True)

# ## add column name
df.columns = ["mainShipmentRouteNumber", "speed", "time", "truckNumber", "timestamp", "shipmentEndCity",
                "shipmentStartCity", "city", "country"]
print(df)

for index, row in df.iterrows():

    url = 'http://localhost:8081/DataLog'
    speed = np.int64(df['speed'][index])
    data = {'timestamp': str(df['timestamp'][index]), 'speed': int(speed), 'country': str(df['country'][index]),
            'city': str(df['city'][index])}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    time.sleep(0.5)

'''
while True:
    rnd = random.randint(10,50)
    print(rnd)
    url = 'http://localhost:8081/randomInt'
    data = {'value': int(rnd)}
    headers = {'content-type': 'application/json'}

    r = requests.post(url, data=json.dumps(data), headers=headers)
    time.sleep(0.5)
'''