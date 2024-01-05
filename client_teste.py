import requests


i = 8
url = f"http://127.0.0.1:5000/{i}"
url = f"http://127.0.0.1:5000/cadastrar"
response = requests.get(url)

print(response.text)
