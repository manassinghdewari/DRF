import requests

endpoint ="http://localhost:8000/api/products/1/detail/"  # http://localhost:8000/

get_response = requests.get(endpoint)
print(get_response.text) # print a row text response
print(get_response.status_code)

print(get_response.json())
