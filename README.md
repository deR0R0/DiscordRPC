# DiscordRPC
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)

A simple python program that changes your discord rich presence/game activity. 

Disclaimer!!!: This program uses your IP to determine your **nearby** location for the weather mode. Nothing is stored/sent to my end. :)

The program will bug you about it though... D:

## Use
This program has already been turned into a .exe file for ease of use. (thanks PyInstaller!)

But, if you would like to use it with python, the libraries are down below.

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

If you have any mode ideas, please go into "issues" and create an issue for a "New Mode".

## Other Stuff
This program isn't really made for you to enter the wrong thing (but there are some error handling) please just enter information carefully!

The program will loop the title and the update checker... multiprocesser 🙄

If any other issues arise, please create an issue or if you know how to fix it, you're welcome to send a pull request! :D

  
