from datetime import datetime
from zoneinfo import ZoneInfo

def format_schedule_array(schedule_data):
    formatted_schedule = []
    for stream in schedule_data:
        if stream['start_time']:
            dt = (datetime.strptime(stream['start_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
            formatted_start_time = dt.strftime("%B %-d @ %-I:%M %p")
        if stream['end_time']:
            dt = (datetime.strptime(stream['end_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
            formatted_end_time = dt.strftime("%B %-d @ %-I:%M %p")
        formatted_stream = {
            "title": stream.get("title", "No Title"),
            "start_time": formatted_start_time if stream['start_time'] else "No Start Time",
            "end_time": formatted_end_time if stream['end_time'] else "No End Time",
            "category": stream.get("category", "Unknown")
        }
        formatted_schedule.append(formatted_stream)
    return formatted_schedule

def pretty_schedule(formatted_schedule):
    string = ""
    for stream in formatted_schedule:
        
        string += ("-" * 20)
        string += "\n"
        string += (f"\033[33mTitle:\33[0m {str(stream['title'])}\n")
        string += (f"\033[33mStart Time:\33[0m {str(stream['start_time'])}\n")
        string += (f"\033[33mEnd Time:\33[0m {str(stream['end_time'])}\n")
        string += (f"\033[33mCategory:\33[0m {str(stream['category'])}\n")
        string += ("-" * 20)
        string += "\n"
        
    return string
        
def combine_schedules(schedules):
    combined = []
    for schedule in schedules:
        combined.extend(schedule)
    combined.sort(key=lambda x: x['start_time'])
    return combined