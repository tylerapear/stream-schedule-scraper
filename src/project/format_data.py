from datetime import datetime
from zoneinfo import ZoneInfo

def format_schedule_array(schedule_data):
    formatted_schedule = []
    for stream in schedule_data.get("data", {}).get("segments", []):
        if stream['start_time']:
            dt = (datetime.strptime(stream['start_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
            formatted_start_time = dt.strftime("%B %-d %Y @ %-I:%M %p")
        if stream['end_time']:
            dt = (datetime.strptime(stream['end_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
            formatted_end_time = dt.strftime("%B %-d %Y @ %-I:%M %p")
        formatted_stream = {
            "title": stream.get("title", "No Title"),
            "start_time": formatted_start_time if stream['start_time'] else "No Start Time",
            "end_time": formatted_end_time if stream['end_time'] else "No End Time",
            "category": stream.get("category", "Unknown")
        }
        formatted_schedule.append(formatted_stream)
    return formatted_schedule

def print_schedule_array(formatted_schedule):
    for stream in formatted_schedule:
        
        print("-" * 20)
        print(f"Title: {stream['title']}")
        print(f"Start Time: {stream['start_time']}")
        print(f"End Time: {stream['end_time']}")
        print(f"Category: {stream['category']}")
        print("-" * 20)