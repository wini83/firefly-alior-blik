import json
import requests

def load_token(filename='token.json'):
    with open(filename, 'r') as f:
        return json.load(f)

access_token = load_token()['access_token']

# 4. LISTOWANIE ZAKUPÓW
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/vnd.allegro.public.v1+json',
}
response = requests.get('https://api.allegro.pl/me', headers=headers)

if response.ok:
    results = response.json()
    print (results)
else:
    print("Błąd przy pobieraniu danych:", response.status_code, response.text)
