import unittest
from src.project.format_data import *

class TestFormatData(unittest.TestCase):
    
    def setUp(self):
        self.maxDiff = None
        self.sample_data = {
            'data': {
                'segments': [
                    {
                        'id': 'eyJzZWdtZW50SUQiOiIwMTYyNmZjMC0wOWMyLTRiMzctODE2MC04YWI3Nzg3MmY0ZWUiLCJpc29ZZWFyIjoyMDI1LCJpc29XZWVrIjo0OH0=', 
                        'start_time': '2025-11-24T21:00:00Z', 
                        'end_time': '2025-11-25T01:00:00Z', 
                        'title': 'STREAM', 
                        'canceled_until': None, 
                        'category': None, 
                        'is_recurring': True
                    },
                    {
                        'id': 'eyJzZWdtZW50SUQiOiJlYzg2MWVlMS01MTBjLTRkNGYtOTI3ZC0yMzBiYWMzMzcxNzYiLCJpc29ZZWFyIjoyMDI1LCJpc29XZWVrIjo0OH0=', 
                        'start_time': '2025-11-25T21:00:00Z', 
                        'end_time': '2025-11-26T01:00:00Z', 
                        'title': 'COOL STREAM', 
                        'canceled_until': None, 
                        'category': 'Just Chatting', 
                        'is_recurring': False
                    }
                ]
            }
        }
    
    def test_format_schedule_array(self):
        expexted_output = [
            {
                'title': 'STREAM',
                'start_time': 'November 24 2025 @ 1:00 PM',
                'end_time': 'November 24 2025 @ 5:00 PM',
                'category': None
            },
            {
                'title': 'COOL STREAM',
                'start_time': 'November 25 2025 @ 1:00 PM',
                'end_time': 'November 25 2025 @ 5:00 PM',
                'category': 'Just Chatting'
            }
        ]
        result = format_schedule_array(self.sample_data)
        self.assertEqual(result, expexted_output)
        
    def test_print_schedule_array(self):
        formatted_schedule = format_schedule_array(self.sample_data)
        from io import StringIO
        import sys

        captured_output = StringIO()
        sys.stdout = captured_output
        print("CAP")
        print(captured_output.getvalue())
        print("END CAP")

        print_schedule_array(formatted_schedule)

        sys.stdout = sys.__stdout__

        expected_output = (
            "--------------------\n"
            "Title: STREAM\n"
            "Start Time: November 24 2025 @ 1:00 PM\n"
            "End Time: November 24 2025 @ 5:00 PM\n"
            "Category: None\n"
            "--------------------\n"
            "--------------------\n"
            "Title: COOL STREAM\n"
            "Start Time: November 25 2025 @ 1:00 PM\n"
            "End Time: November 25 2025 @ 5:00 PM\n"
            "Category: Just Chatting\n"
            "--------------------\n"
        )

        self.assertEqual(captured_output.getvalue(), expected_output)