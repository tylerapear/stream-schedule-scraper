import unittest, os
from dotenv import load_dotenv
from src.project.get_broadcaster_data import *

class TestGetBroadcasterData(unittest.TestCase):
    
    def setUp(self):
        load_dotenv("src/envs/.env.local")
        self.CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
        self.CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")
        self.token = get_token(self.CLIENT_ID, self.CLIENT_SECRET)
    
    def test_get_broadcaster(self):
        user = get_broadcaster("tpear123", self.token, self.CLIENT_ID)
        self.assertEqual(user["data"][0]["login"], "tpear123")
        
    def test_get_broadcaster_error(self):
        with self.assertRaises(ValueError):
            user = get_broadcaster("tpear1235678", self.token, self.CLIENT_ID)
        
    def test_get_broadcasters_2_valid(self):
        usernames = ["tpear123", "majinphil"]
        broadcasters = get_broadcasters(usernames, self.token, self.CLIENT_ID)
        self.assertEqual(broadcasters[0]["data"][0]["login"], "tpear123")
        self.assertEqual(broadcasters[1]["data"][0]["login"], "majinphil")
        self.assertEqual(len(broadcasters), 2)
        
    def test_get_broadcasters_1_valid_1_invalid(self):
        usernames = ["tpear123", "blablablainvaliduser"]
        broadcasters = get_broadcasters(usernames, self.token, self.CLIENT_ID)
        self.assertEqual(broadcasters[0]["data"][0]["login"], "tpear123")
        self.assertEqual(len(broadcasters), 1)
        
    def test_get_broadcaster_schedule(self):
        schedule = get_broadcaster_schedule("majinphil", self.token, self.CLIENT_ID)
        self.assertTrue(len(schedule["data"]["segments"]) > 0)
        self.assertTrue("id" in schedule["data"]["segments"][0])
        self.assertTrue("start_time" in schedule["data"]["segments"][0])
        self.assertTrue("end_time" in schedule["data"]["segments"][0])
        self.assertTrue("title" in schedule["data"]["segments"][0])
        self.assertTrue("canceled_until" in schedule["data"]["segments"][0])
        self.assertTrue("category" in schedule["data"]["segments"][0])
        self.assertTrue("is_recurring" in schedule["data"]["segments"][0])
        
        schedule = get_broadcaster_schedule("Linkus7", self.token, self.CLIENT_ID)
        self.assertEqual(None, schedule)