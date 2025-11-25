import os, json
from platformdirs import user_data_dir
from dotenv import load_dotenv
from src.project.get_broadcaster_data import *
            
data_dir = "./data"
filepath = data_dir + "/streamer_list.json"
            
def write_file(data):
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    with open(filepath, "w") as f:
        f.write(data)
            
def add_streamer(username, token, CLIENT_ID):
    if streamer_exists(username, token, CLIENT_ID):
        streamers = get_streamers()
        broadcaster_id = get_broadcaster(username, token, CLIENT_ID)["data"][0]["id"]
        if {"username": username, "broadcaster_id": broadcaster_id} not in streamers:
            streamers.append({
                "username": username, 
                "broadcaster_id": broadcaster_id
            })
        write_file(json.dumps({"streamers": streamers}))
        return True
    return False
        
def get_streamers():
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            data = f.read()
        if data:
            dict_data = json.loads(data)
            return dict_data["streamers"]
    return []

def remove_streamer(username):
    streamers = get_streamers()
    streamers = [s for s in streamers if s['username'] != username]
    write_file(json.dumps({"streamers": streamers}))
    
def streamer_exists(username, token, CLIENT_ID):
    try:
        user_data = get_broadcaster(username, token, CLIENT_ID)
        return True
    except:
        return False
    