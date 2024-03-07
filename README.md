## RiverBot

    This is a Discord music bot.


## Commands

    [/rplay or /rp] [<YT link> or search]: to play or add the song to the queue;
        e.g.:
            /rplay https://www.youtube.com/watch?v=dQw4w9WgXcQ
            /rp The Sound of Silence

    [/rqueue or /rq ]: to show all songs queued;

    [/rpause or /rs]: to pause current song;

    [/rresume or /rr]: to resume playing;

    [/rjoin or /rj]: to join the channel;

    [/rleave or /rl]: to leave the channel;

    [/rclean or /rc]: to clean queue and stop playing;


## Requirements

    The initial requirements for this project are:
        Python 3.10 -> https://www.python.org/downloads/
        Pip 22.0.4  -> Pip will come with Python 3.4+ or Python 2.7.9+
        FFmpeg 6.1.1 -> https://www.ffmpeg.org/download.html


## Setup

    Sign up and sign in to your Discord account at https://discord.com/login

    Access the Discord Developer Portal at https://discord.com/developers/applications

    Click on the "New Application" button in the upper right corner, type the name of your bot, accept Discord's ToS and Policy and then hit the "Create" button

    Go to your application page (something like https://discord.com/developers/applications/1213555928457023568/information), click on "OAuth2" in the left side, click on "Reset Secret" in the "Client information" area, confirm your password and copy your new "CLIENT SECRET" (something like ar567b1uS_-JZXwsG28Mmidm_j3j1jTC)

    Still on this page, scroll down to "OAuth2 URL Generator", select the "bot" option on "SCOPES", select all permissions your bot will need on "BOT PERMISSIONS" (for a personal bot you can leave it as "Administrator"), copy and access the link on "GENERATED URL", select which server you want to invite the bot to and then click on "Authorize" button

    Go back to your application page and click on "Bot" in the left side, scroll down to "Privileged Gateway Intents" and make sure all three intents (Presence Intent, Server Members Intent and Message Content Intent) are turned on

    Download or clone the source code from this repository, place the unzipped ffmpeg folder (see Requirements above) in the project root, create a .env file and paste *DISCORD_TOKEN="YOUR_CLIENT_SECRET_HERE"* into it

        e.g.:
            *DISCORD_TOKEN="ar567b1uS_-JZXwsG28Mmidm_j3j1jTC"*

    Open a terminal/cmd window in the root of the project and type *python -m venv project_env* followed by *project_env\Scripts\activate.bat*. The first command creates a Virtual Environment for the project and the second one activates it. If you are using a Linux distro, switch the second command for *source project_env/bin/activate*
    
    After that, type *pip install -r requirements.txt* to download the additional dependencies

    Lastly, type *python main.py* to run your bot. You should see the bot going online on the Discord server you invited it to. You can now use the commands (see Commands above) to play songs on the server
