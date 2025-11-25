import os, time
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from src.project.get_broadcaster_data import *
from src.project.format_data import *
from src.project.streamer_list import *
from src.project.query_schedules import *

load_dotenv("src/envs/.env.local")

CLIENT_ID = os.getenv("TWITCH_CLIENT_ID")
CLIENT_SECRET = os.getenv("TWITCH_CLIENT_SECRET")

def typewriter(text, newline=False, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    if newline:
        print()
        
def print_streamers():
    streamers = get_streamers()
    if streamers != []:
        typewriter("\n\033[32mYour Streamers:\033[0m\n")
        for streamer in sorted(streamers, key=lambda x: x['username'].lower()):
            typewriter(streamer['username'], newline=True)
        return True
    else:
        print("\nNo streamers added yet\n")
        time.sleep(1)
        typewriter("\n\033[34mReturning to main menu...\033[0m\n", delay=0.02)
        return False
        
def print_streamer_schedule(username, days):
    full_schedule_data = get_broadcaster_schedule(username, get_token(CLIENT_ID, CLIENT_SECRET), CLIENT_ID)
    if full_schedule_data:
        full_schedule = full_schedule_data['data']['segments']
        start_date = datetime.now().astimezone()
        end_date = start_date + timedelta(days=int(days))
        schedule = streams_between(start_date, end_date, full_schedule)
        typewriter(f"\n\033[32mUpcoming Streams for {username}:\033[0m\n", newline=True)
        typewriter(pretty_schedule(format_schedule_array(schedule)), delay=0.01)
    else:
        typewriter(f"\n\033[31mStreamer {username} does not have any upcoming streams.\033\n[0m")

def main():
    
    title = """\033[38;5;208m
    
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
___________       .__  __         .__        _________                    __   
\\__    ___/_  _  _|__|/  |_  ____ |  |__    /   _____/ ____  ____  __ ___/  |_ 
  |    |  \\ \\/ \\/ /  \\   __\\/ ___\\|  |  \\   \\_____  \\_/ ___\\/  _ \\|  |  \\   __|
  |    |   \\     /|  ||  | \\  \\___|   Y  \\  /        \\  \\__(  <_> )  |  /|  |  
  |____|    \\/\\_/ |__||__|  \\___  >___|  / /_______  /\\___  >____/|____/ |__|  
                                \\/     \\/          \\/     \\/                   
|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n\033[0m"""
    
    options = """
1) Add Streamer
2) Remove Streamer
3) List Streamers
4) View a Streamer's Schedule
5) View All Streamers' Schedules
6) Quit

\033[34mChoose an operation (1-6):\033[0m """

    typewriter(title, delay=0.0001)
    
    running = True
    while running:
        typewriter(options)
        option = input().strip().lower()
        match option:
            case '1':
                typewriter("\n\033[34mEnter the streamer's username: \033[0m")
                username = input().strip()
                if add_streamer(username, get_token(CLIENT_ID, CLIENT_SECRET), CLIENT_ID) == True:
                    print(f"\n\033[32mStreamer {username} added.\033[0m")
                else:
                    print(f"\n\033[31mStreamer {username} does not exist.\033[0m")
            case '2':
                typewriter("\n\033[34mEnter the streamer's username: \033[0m")
                username = input().strip()
                remove_streamer(username)
                typewriter(f"\n\033[32mStreamer {username} removed.\033\n[0m")
            case '3':
                print_streamers()
            case '4':
                if not print_streamers():
                    continue
                
                typewriter("\n\033[34mEnter streamer's username to retrieve their schedule: \033[0m")
                username = input().strip()
                if not streamer_exists(username, get_token(CLIENT_ID, CLIENT_SECRET), CLIENT_ID):
                    typewriter(f"\n\033[31mStreamer {username} does not exist.\033\n[0m")
                    time.sleep(1)
                    typewriter("\n\033[34mReturning to main menu...\033[0m\n", delay=0.02) 
                    continue
                
                typewriter("\033[34mHow many days forward would you like to look?: \033[0m")
                days = input().strip()
                if not days.isdigit():
                    typewriter(f"\n\033[31m{days} is not a valid number.\033\n[0m")
                    time.sleep(1)
                    typewriter("\n\033[34mReturning to main menu...\033[0m\n", delay=0.02) 
                    continue
                
                print_streamer_schedule(username, days)
                    
            case '5':
                if not print_streamers():
                    continue
                
                typewriter("\n\033[34mHow many days forward would you like to look?: \033[0m")
                days = input().strip()
                if not days.isdigit():
                    typewriter(f"\n\033[31m{days} is not a valid number.\033\n[0m")
                    time.sleep(1)
                    typewriter("\n\033[34mReturning to main menu...\033[0m\n", delay=0.02) 
                    continue
                
                typewriter(f"\n\033[32mUpcoming Streams for All Streamers:\033[0m", newline=True)
                
                streamers = get_streamers()
                for streamer in sorted(streamers, key=lambda x: x['username'].lower()):
                    print_streamer_schedule(streamer['username'], days)
            case '6':
                running = False
            case _:
                print("\nInvalid option selected.\n")
                
        time.sleep(1)     
        if running:
            typewriter("\n\033[34mReturning to main menu...\033[0m\n", delay=0.02)    
                
if __name__ == "__main__":
    main()