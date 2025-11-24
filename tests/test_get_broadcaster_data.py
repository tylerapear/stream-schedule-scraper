import unittest, os
from src.get_broadcaster_data import *
from dotenv import load_dotenv

class TestGetBroadcasterData(unittest.TestCase):
    
    def setUp(self):
        load_dotenv()
        self.CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
        self.token = get_token(self.CLIENT_ID, self.CLIENT_SECRET)
    
    def test_get_broadcaster(self):
        user = get_broadcaster("tpear123", self.token, self.CLIENT_ID)
        self.assertEqual(user["data"][0]["login"], "tpear123")
        
    def test_get_broadcasters(self):
        usernames = ["tpear123", "majinphil"]
        broadcasters = get_broadcasters(usernames, self.token, self.CLIENT_ID)
        self.assertEqual(broadcasters[0]["data"][0]["login"], "tpear123")
        self.assertEqual(broadcasters[1]["data"][0]["login"], "majinphil")
        self.assertEqual(len(broadcasters), 2)