import requests

def get_token(CLIENT_ID, CLIENT_SECRET):
    response = requests.post(
        "https://id.twitch.tv/oauth2/token",
        params = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "client_credentials"
        }
    )
    return response.json()["access_token"]

def get_broadcaster(username, token, CLIENT_ID):
    response = requests.get(
        f"https://api.twitch.tv/helix/users?login={username}",
        headers = {
            "Client-ID": CLIENT_ID,
            "Authorization": f"Bearer {token}"
        }
    )
    if response.json()["data"] == []:
        raise ValueError(f"User '{username}' not found.")
    return response.json()
    
def get_broadcasters(usernames, token, CLIENT_ID):
    broadcasters = []
    for username in usernames:
        try:
            broadcasters.append(get_broadcaster(username, token, CLIENT_ID))
        except ValueError:
            continue
    return broadcasters

def get_broadcaster_schedule(username, token, CLIENT_ID):
    user = get_broadcaster(username, token, CLIENT_ID)
    user_id = user["data"][0]["id"]
    
    response = requests.get(
        f"https://api.twitch.tv/helix/schedule?broadcaster_id={user_id}",
        headers = {
            "Client-ID": CLIENT_ID,
            "Authorization": f"Bearer {token}"
        }
    )
    if response.json().get("error"):
        return None
    return response.json()