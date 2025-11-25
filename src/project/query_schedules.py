from datetime import datetime
from zoneinfo import ZoneInfo

def streams_between(start_date, end_date, schedule):
    matching_streams = []
    for stream in schedule:
        stream_start_date = (datetime.strptime(stream['start_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
        stream_end_date = (datetime.strptime(stream['end_time'], "%Y-%m-%dT%H:%M:%SZ")).replace(tzinfo=ZoneInfo("UTC")).astimezone()
        if stream_start_date >= start_date and stream_end_date <= end_date:
            matching_streams.append(stream)
    return matching_streams