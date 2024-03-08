<style>
h1, h2 {
    color: rgb(120, 150, 200);
}

.riverbot-div, .introduction-div, .requirements-div, .commands-div, .setup-div {
    background-color: rgb(25, 25, 25);
    padding: 15px;
    border-style: groove;
    border-width: 1px;
    border-color: rgb(120, 150, 200);
}

.riverbot-div {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px;
    padding-top: 20px;
    padding-bottom: 2px;
}
</style>

# RiverBot
<div class='riverbot-div'>
<div class='riverbot-img-div'>

![RiverBot icon](/img/icon.png)

</div>
</div>

</br>

## Introduction
<div class='introduction-div'>
    <p>This is the official repository for the Discord music bot application <b>RiverBot</b>. Here you can find all the information needed to set this bot up and all the available commands to use.</p>
</div>

</br>

## Commands
<div class='commands-div'>
<p>The bot supports the following commands:</p>

<p><b>[/rplay or /rp] [&lt;YT link&gt; or search]:</b> to play or add the song to the queue;</p>

<p>e.g.: </br>
    &emsp;/rplay https://www.youtube.com/watch?v=dQw4w9WgXcQ </br>
    &emsp;/rp The Sound of Silence</p>

<p><b>[/rqueue or /rq ]:</b> to show all songs queued;</p>

<p><b>[/rpause or /rs]:</b> to pause current song;</p>

<p><b>[/rresume or /rr]:</b> to resume playing;</p>

<p><b>[/rjoin or /rj]:</b> to join the channel;</p>

<p><b>[/rleave or /rl]:</b> to leave the channel;</p>

<p><b>[/rclean or /rc]:</b> to clean queue and stop playing.</p>
</div>

</br>

## Requirements
<div class="requirements-div">
<p>The initial requirements for this project are:</p>

<p><b>Python 3.10</b> -> <a href='https://www.python.org/downloads/'>https://www.python.org/downloads/</a></p>

<p><b>Pip 22.0.4</b>  -> Pip will come with Python 3.4+ or Python 2.7.9+</p>

<p><b>FFmpeg 6.1.1</b> -> <a href='https://www.ffmpeg.org/download.html'>https://www.ffmpeg.org/download.html</a></p>
</div>

</br>

## Setup
<div class='setup-div'>
<p>Sign up and sign in to your Discord account at <a href='https://discord.com/login'>https://discord.com/login</a>.</p>

<p>Access the Discord Developer Portal at <a href='https://discord.com/developers/applications'>https://discord.com/developers/applications</a>.</p>

<p>Click on the "New Application" button in the upper right corner, type the name of your bot, accept Discord's ToS and Policy and then hit the "Create" button.</p>

<p>Go to your application page (something like <a href='https://discord.com/developers/applications/1213555928457023568/information'>https://discord.com/developers/applications/1213555928457023568/information</a>), click on "OAuth2" in the left side, click on "Reset Secret" in the "Client information" area, confirm your password and copy your new "CLIENT SECRET" (something like ar567b1uS_-JZXwsG28Mmidm_j3j1jTC).</p>

<p>Still on this page, scroll down to "OAuth2 URL Generator", select the "bot" option on "SCOPES", select all permissions your bot will need on "BOT PERMISSIONS" (for a personal bot you can leave it as "Administrator"), copy and access the link on "GENERATED URL", select which server you want to invite the bot to and then click on "Authorize" button.</p>

<p>Go back to your application page and click on "Bot" in the left side, scroll down to "Privileged Gateway Intents" and make sure all three intents (Presence Intent, Server Members Intent and Message Content Intent) are turned on.</p>

<p>Download or clone the source code from this repository, place the unzipped ffmpeg folder (see Requirements above) in the project root, create a .env file and paste <i>DISCORD_TOKEN="YOUR_CLIENT_SECRET_HERE"</i> into it.</p>

<p>e.g.:</br>  &emsp;&emsp;<i>DISCORD_TOKEN="ar567b1uS_-JZXwsG28Mmidm_j3j1jTC"</i></p>

<p>Open a terminal/cmd window in the root of the project and type <i>python -m venv project_env</i> followed by <i>project_env\Scripts\activate.bat</i>. The first command creates a Virtual Environment for the project and the second one activates it. If you are using a Linux distro, switch the second command for <i>source project_env/bin/activate</i>.</p>
    
<p>After that, type <i>pip install -r requirements.txt</i> to download the additional dependencies.</p>

<p>Lastly, type <i>python main.py</i> to run your bot. You should see the bot going online on the Discord server you invited it to. You can now use the commands (see Commands above) to play songs on the server.</p>
</div>
