import requests

endpoint ="http://127.0.0.1:8000//cardekho/functionbased/"

response = requests.get(endpoint)
print(response.json()) # Response will be in JSON Format and response.json() - python format convert 
print(response.status_code)