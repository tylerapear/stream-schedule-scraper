import os
from dotenv import load_dotenv
from src.project.get_broadcaster_data import *
from src.project.format_data import *
from src.project.streamer_list import *

load_dotenv("src/envs/.env.local")

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

option = input("Enter 'a' to add a streamer, 'r' to remove a streamer, or 'v' to view schedule: ").strip().lower()

match option:
    case 'a':
        username = input("Enter the streamer's username: ").strip()
        if add_streamer(username, get_token(CLIENT_ID, CLIENT_SECRET), CLIENT_ID) == True:
            print(f"Streamer {username} added.")
        else:
            print(f"Streamer {username} does not exist.")