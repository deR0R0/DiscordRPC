# DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

This program (after extensive testing) is found to not be able to save data. Please do not use the save data feature! (Unless you download from src)

A simple python program that changes your discord rich presence/game activity. 

Disclaimer!!!: This program uses your IP to determine your **nearby** location for the weather mode. Nothing is stored/sent to my end. :)

The program will bug you about it though... D:

Status: 🔵 (Done but will add requested features)

## How to Download
On the right, there should be releases. Click on the latest release and __***download the zip folder***__


## Use
1. Download zip file
2. Unzip
3. Download python (preferably from website but from microsoft store works too)
4. Navigate to directory of the folder
5. Run ```python -m pip install -r requirements.txt``` in command prompt
6. Run the program

Below is all the libraries used

- pypresence
- os
- sys
- time
- psutil
- json
- cpuinfo
- datetime
- requests
- colorama
- multiprocessing (freeze support)  ```from multiprocessing import freeze_support```

## Modes

1. Custom RPC
2. CPU Stats
3. CPU and RAM Usage (real time)
4. Local Time
5. Local Weather

If you have any mode ideas, feel free to go into "issues" and create an issue for a "New Mode".

## Creating a Custom RPC

1. Create a application at the [discord developer portal](https://discord.com/developers/applications)

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/7f2cff0a-be77-4405-b09d-907c6254d3b0)

2. Name the application and create it (your discord status will be set as this application name!)

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/e416cf42-1337-442d-a24f-bb7e7784f7ce)

3. Copy the application ID and paste it into the prompt

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/cd050fcc-1e77-4058-9eb8-f853fdd2c839)

4. Go to the "Rich Presence" tab on the left and click on "Visualizer"

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/790541ae-18cf-4eba-9cfd-80bc9b84d796)

5. State & Details (state cannot be empty!!!!!)

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/71114849-98c2-4832-bd6f-2cb11ce5de1e)

![image](https://github.com/deR0R0/DiscordRPC/assets/126121919/f2495544-9eab-4704-b3ea-bd2930cf4d07)

6. Large Image & Large Image Text (If large image -> large image text (required) if not large image then no text)

Go to the tab "Rich Presence" and go to "Art Assets" and upload an image (size has to be 512x512 and max is 1024x1024)

(i will not be doing this for the sake of this tutorial)

7. Small Image & Small Image Text (same as large image, just a smaller image 👍 and small image has to be with large image)

8. Button

Enter the button text and the url it will redirect you to when you click it.


Congrats, you are done! You may save if you would like (or not)


## Weather!!! (my fav)

1. Go to [weatherapi.com](https://www.weatherapi.com/)
2. Create an account
3. Once you're at the dashboard, copy your API key
4. Paste it into the program
5. Answer either T/F in the prompts (it will ask you if you want to display a certain thing)
6. Done :)

## Other Stuff

This program isn't really made for you to enter the wrong thing (but there are some error handling) please just enter information carefully!

The program will loop the title and the update checker... multiprocesser 🙄

If any other issues arise, please create an issue or if you know how to fix it, you're welcome to send a pull request! :D


## Changelog

- 4/19/24 - v1.0.0 - Release
- 4/19/24 - v1.0.1 - Minor Bugfix
- 4/21/24 - v1.1.0 - Changed from .exe file to python file (pyinstaller doesn't allow of writing files... so no saving)

  
