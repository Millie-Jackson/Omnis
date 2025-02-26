import requests
import json

API_KEY = "DC4B5187E7466B969BDBB83072BE7329"
STEAM_ID = "76561197993343418"
url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&format=json"

response = requests.get(url)
try:
    data = response.json()
    with open("games.json", "w") as f:
        json.dump(data, f, indent=4)
    print("Game lis saved to games.json")
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON. Response:", response.text)
