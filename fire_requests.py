import requests
import time
import os
import asyncio

async def fire_request(url, method):
    # High timeout because we don't want failed requests caused by high server load. 
    # Only blocked requests caused by the rate limiting should be considered as failed requests.
    timeout = 20
    if method == 'GET':
        response = requests.get(url, timeout=timeout)
    elif method == 'POST':
        response = requests.post(url, timeout=timeout)
    elif method == 'PUT':
        response = requests.put(url, timeout=timeout)
    if response.status_code == 429:
        print(f"Request failed because of rate limiting.")
    elif response.status_code != 200:
        print(f"Request failed with status code {response.status_code}")
    else:
        print("Request successful")

if __name__ == '__main__':
    url = os.getenv('URL')
    method = os.getenv('METHOD')
    frequency = os.getenv('FREQUENCY')
    
    sleep_time = 1/float(frequency)
    
    while True:
        asyncio.run(fire_request(url, method))
        time.sleep(sleep_time)
        
    