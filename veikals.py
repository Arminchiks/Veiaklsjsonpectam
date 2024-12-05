from urllib import response
import requests

url='https://fakestoreapi.com/carts?limit=1'

try:
    response=requests.get(url)
    response.raise_for_status()
    data=response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")