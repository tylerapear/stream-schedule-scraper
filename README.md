# Twitch-Scout

A Python command line tool for quickly checking the upcoming schedules of your favorite streamers on [Twitch](https://twitch.tv).

## Installation (Linux)

1. Clone the repository:

    ```bash
    git clone https://github.com/tylerapear/NESY-Engine.git
    ```
2. Cd into the project directory

    ```bash
    cd Twitch-Scout
    ```
4. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Ensure you have a [Python3 environment](https://docs.python.org/3/using/index.html) set up on your machine with pip
4. Install dependencies from pyproject.toml:
    
    ```bash
    pip install -e .
    ```
5. [Register an application on Twitch](https://dev.twitch.tv/docs/api/get-started). Generate a Client Secret. Make note of your Client ID and Client Secret.
6. Copy a `.env.local` file in src/envs from the `.env.template`:
    ```bash
    cp src/envs/.env.template src/envs/.env.local
    ```
7. Replace the `TWITCH_CLIENT_ID` and `TWITCH_CLIENT_SECRET` in your `.env.local` file with your own Client ID and Client Secret from the Twitch application you registered:
    ```bash
    TWITCH_CLIENT_ID=<your-client-id>
    TWITCH_CLIENT_SECRET=<your-client-secret>
    ```
8. Give it a test!
    ```bash
    python main.py
    ```

## Usage Instructions

Upon launching the app, you'll be given 6 options:

```
1) Add Streamer
2) Remove Streamer
3) List Streamers
4) View a Streamer's Schedule
5) View All Streamers' Schedules
6) Quit

Choose an operation (1-6):
```

You'll want to start by adding a streamer, since nothing else will work until you have a streamer in your list. Choose option 1, then provide the name of your favorite streamer:

```
Chose an option (1-6): 1

Enter the streamer's username: ThePrimagen

Streamer ThePrimagen added.

Returning to main menu...
```

You'll then return to the main menu. Note that whatever streamer you provide as input will be validated against Twitch and only added to the list if a streamer with that name exists. From here, the rest of the options are self explanatory.

You could remove a streamer from your list:

```
Choose an operation (1-6): 2                       

Enter the streamer's username: ThePrimagen

Streamer ThePrimagen removed.

Returning to main menu...
```

Or you could print out your list of streamers:

```
Choose an operation (1-6): 3

Your Streamers:
Linkus7
PointCrow
ThePrimagen

Returning to main menu...
```
But the real reason for using this app is to quickly look at streamer's schedules:

```
Choose an operation (1-6): 4

Your Streamers:
Linkus7
PointCrow
ThePrimagen

Enter streamer's username to retrieve their schedule: ThePrimagen
How many days forward would you like to look?: 5

Streamer ThePrimagen does not have any upcoming streams.

Returning to main menu...
```

Some streamers don't keep their schedules updated...

But others do! :

```
Choose an operation (1-6): 4

Your Streamers:
Linkus7
PointCrow
ThePrimagen

Enter streamer's username to retrieve their schedule: PointCrow
How many days forward would you like to look?: 2

Upcoming Streams for PointCrow:

--------------------
Title: STREAM
Start Time: November 25 @ 1:00 PM
End Time: November 25 @ 5:00 PM
Category: None
--------------------
--------------------
Title: STREAM
Start Time: November 26 @ 1:00 PM
End Time: November 26 @ 5:00 PM
Category: None
--------------------

Returning to main menu...
```

Option 5 does just what it says: lists the upcoming schedules of all the streamers in your list for however many days into the future you specify.

And option 6 quits the program.

Hope you enjoy!