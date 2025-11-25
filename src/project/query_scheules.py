

def streams_between(start_date, end_date, schedule):
    matching_streams = []
    for stream in schedule:
        if stream['start_time'] >= start_date and stream['end_time'] <= end_date:
            matching_streams.append(stream)
    return matching_streams