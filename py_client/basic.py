import requests

endpoint ="http://localhost:8000/api/"  # http://localhost:8000/

get_response = requests.post(endpoint,json={"title":"hello","content":"Hello world","price":123}) #http request it will genrate a url and it will hit the url
print(get_response.text) # print a row text response
print(get_response.status_code)

print(get_response.json())
