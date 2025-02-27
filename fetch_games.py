# fetch_games.py

import os
import requests
import json
import time
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

API_KEY = os.getenv("STEAM_API_KEY")
STEAM_ID = os.getenv("STEAM_ID")

if not API_KEY or not STEAM_ID:
    raise ValueError("Missing API Key or Steam ID. Set them in the .env file.")

def fetch_games():
    """Fetch owned games from Steam API."""

    url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={API_KEY}&steamid={STEAM_ID}&format=json"

    response = requests.get(url)
    print("Raw API Response:", response.text)

    try:
        data = response.json()
        #with open("games.json", "w") as f:
        #    json.dump(data, f, indent=4)
        print("Game list saved to games.json")
        games = data.get("response", {}).get("games", [])
        return games
    except requests.exceptions.JSONDecodeError:
        print("Failed to decode JSON. Response:", response.text)
        return []

def get_game_titles(game_list):
    """Gat game titles from AppIDs"""

    steam_api_url =  "https://store.steampowered.com/api/appdetails"
    games_with_titles = []

    for game in game_list:
        appid = game["appid"]
        response = requests.get(f"{steam_api_url}?appids={appid}")

        if response.status_code == 200:
            data = response.json()
            if str(appid) in data and data[str(appid)].get("success", False):
                game["name"] = data[str(appid)]["data"]["name"]
            else:
                game["name"] = "Unkown Game"
        else:
            game["name"] = "API Error"

        games_with_titles.append(game)

    return games_with_titles

# Fetch and process games
games = fetch_games()
if games:
    updated_games = get_game_titles(games)

    # Extract only titles
    game_titles = [game["name"] for game in updated_games]

    # Save updated list with names
    with open("games.json", "w") as file:
        json.dump(game_titles, file, indent=4)

    print("Updated game list saved to games.json!")
else:
    print("No games found or failed to fetch data.")