import time
import json
import logging
import requests
from airflow import DAG
from kafka import KafkaProducer
from datetime import datetime
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'juyuta',
    'start_date': datetime(2025, 2, 21, 10, 00)
}

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()['results'][0]
    return res

def map_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{location['street']['number']} {location['street']['name']}" + "\n" + f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    currentTime = time.time()
    while True:
        if time.time() > currentTime + 60: #1 minute
            break
        try: 
            res = get_data()
            res = map_data(res)
            print(json.dumps(res, indent=3))
            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error("An error occured: {e}")
            continue

with DAG('user_automation',
         default_args=default_args,
         schedule='@daily',
         catchup=False
         ) as dag:
    
    streaming_task = PythonOperator(
        task_id = 'streaming_from_api',
        python_callable=stream_data
        )