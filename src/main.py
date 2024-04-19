import pypresence
import os
import sys
import time
import psutil
import json
import cpuinfo
import datetime
import requests
from colorama import Fore as fore
from multiprocessing import freeze_support
#Ideas: CPU and RAM usage, local time, weather, other whatnot


#CPU:      vendor_id_raw (GenuineIntel)       brand_raw (Intel(R) Core???? @ ???GHz)   <- Remove @ ???Ghz         hz_advertised (2800000????) remove extra zeros by dividing by (1024*1024*1024)

#Vars
version = "v1.0.1"



customSave1 = []
customSave2 = []
customSave3 = []
settings = []
weatherConfig = []
cpu = None
app_id = None
state = None
detail = None
largeImage = None
largeImageText = None
smallImage = None
smallImageText = None
buttonText = None
buttonURL = None
currentPath = os.path.dirname(os.path.abspath(__file__))



#Functions
def clear():
    os.system('cls')

def program():
    clear()
    print("CustomRPC by deR0R0 on Github")
    time.sleep(3)
    checkForUpdates()

def checkForUpdates():
    global version
    print("Checking for Updates...")
    latestVersion = requests.get("https://api.github.com/repos/der0r0/DiscordRPC/releases/latest").json()
    latestVersion = latestVersion["name"]
    if latestVersion == version:
        clear()
        print("You are up to date!")
    else:
        clear()
        print(fore.RED + f"There is a new update available. https://github.com/deR0R0/DiscordRPC/releases/latest ({version} -> {latestVersion})")
        time.sleep(7)
    time.sleep(3)
    clear()

def loadData():
    global customSave1
    global customSave2
    global customSave3
    global settings
    global weatherConfig
    global cpu
    global currentPath

    ipConsent = ""


    print("Loading Save Files...")
    time.sleep(1)
    #Check if user has run program before
    try:
        with open(f'{currentPath}\settings.json', 'r') as file:
            settings = json.load(file)
            print("Found settings!")
    except FileNotFoundError:
        print("Settings file not found! Currently writing a file...")
        settings = {
            "ipConsent": None
        }
        time.sleep(1)
        with open(f'{currentPath}\settings.json', 'w') as file:
            json.dump(settings, file, indent=4)
            print("Settings file created!")
    except Exception as e:
        print(e)
        time.sleep(10000)
        


    #Try Loading Save 1
    try:
        with open(f'{currentPath}\customSave1.json', 'r') as file:
            customSave1 = json.load(file)
            print("Custom Save 1 file found!")
    except FileNotFoundError:
        print("Save 1 file not found! Currently writing a file...")
        customSave1 = {
            "app_id": None,
            "state": None,
            "detail": None,
            "largeImage": None,
            "largeImageText": None,
            "smallImage": None,
            "smallImageText": None,
            "buttonText": None,
            "buttonURL": None
        }
        time.sleep(1)
        with open(f'{currentPath}\customSave1.json', 'w') as file:
            json.dump(customSave1, file, indent=4)
            print("Custom File 1 Successfully Created!")

    #Try Loading Save 2
    try:
        with open(f'{currentPath}\customSave2.json', 'r') as file:
            customSave2 = json.load(file)
            print("Custom Save 2 file found!")
    except FileNotFoundError:
        print("Save 2 file not found! Currently writing a file...")
        customSave2 = {
            "app_id": None,
            "state": None,
            "detail": None,
            "largeImage": None,
            "largeImageText": None,
            "smallImage": None,
            "smallImageText": None,
            "buttonText": None,
            "buttonURL": None
        }
        time.sleep(1)
        with open(f'{currentPath}\customSave2.json', 'w') as file:
            json.dump(customSave2, file, indent=4)
            print("File 2 Successfully Created!")



    #Try Loading Save 3
    try:
        with open(f'{currentPath}\customSave3.json', 'r') as file:
            customSave3 = json.load(file)
            print("Custom Save 3 file found!")
    #File not found, write file
    except FileNotFoundError:
        print("Custom Save 3 file not found! Currently writing a file...")
        customSave3 = {
            "app_id": None,
            "state": None,
            "detail": None,
            "largeImage": None,
            "largeImageText": None,
            "smallImage": None,
            "smallImageText": None,
            "buttonText": None,
            "buttonURL": None
        }
        time.sleep(1)
        with open(f'{currentPath}\customSave3.json', 'w') as file:
            json.dump(customSave3, file, indent=4)
            print("Custom File 3 Successfully Created!")

    time.sleep(1)
    clear()
    #Try loading weather config
    print("Loading weather config...")
    try:
        with open(f'{currentPath}\weatherConfig.json', 'r') as file:
            weatherConfig = json.load(file)
            print("Loaded Weather Config")
    except FileNotFoundError:
        print("File Not Found, Writing file...")
        weatherConfig = {
            "filledOut?": False,
            "apiKey": None,
            "displayLocation": None,
            "displayLastUpdated": None,
            "metric": None,
            "temp": None,
            "feelLike": None,
            "condition": None,
            "wind": None,
            "wind_direction": None,
            "pressure": None,
            "aqi": None,
            "uv": None
        }
        time.sleep(1)
        with open(f'{currentPath}\weatherConfig.json', 'w') as file:
            json.dump(weatherConfig, file, indent=4)
            print("Config File Successfully written.")
    time.sleep(1)
    clear()
    #Make sure the user has to wait MAXIMUM TIME BEFORE THEY CAN USE THE PROGRAM >:D JK JK JK JK JK JK JK
    print(f"Loading CPU Info... {fore.YELLOW}(this will take a moment if your computer is slow)")
    cpu = cpuinfo.get_cpu_info()
    #This wait is esstential!!! it makes sure the function doesn't loop while the program runs a subprocess to check the computer's stats! :> ~
    time.sleep(5)
    clear()
    print("Loaded CPU Info...")
    time.sleep(2)
    print(fore.WHITE + "Data has been loaded successfully")
    time.sleep(3)
    #Check if user has ipConsent
    clear()
    if settings["ipConsent"] != True:
        print(fore.YELLOW + "This program uses IP addresses to find location (for weather). Do you consent? (Y/N)")
        print("Your IP and location will only be stored on your computer. I'm not stealing data, I swear :C")
        ipConsent = input(fore.GREEN + "?: ")
        clear()
        if ipConsent == "y":
            ipConsent = True
        elif ipConsent == "n":
            ipConsent = False
        else:
            print("You didn't enter a correct thing, (Y/N), I will be putting it as 'NO'!")
            ipConsent = False
        settings = {
            "ipConsent": ipConsent
        }
        with open(f'{currentPath}\settings.json', 'w') as file:
            json.dump(settings, file, indent=4)
        clear()
        print("Done!")
        input(fore.GREEN + "[ENTER]")
    chooseRPC()

    


def chooseRPC():
    clear()
    print(fore.CYAN + f"Need help? Type a {fore.GREEN}'?' {fore.CYAN}after the option to get details on it!")
    print(fore.WHITE + "[1] Custom RPC")
    print("[2] CPU Stats")
    print("[3] CPU and RAM Usage")
    print("[4] Local Time")
    print("[5] Local Weather")
    print("[6] MORE COMING SOON")
    print("[7] Exit")
    rpc_choice = input(fore.GREEN + "?: ")
    print(fore.WHITE)

    #Custom RPC
    if rpc_choice == "1":
        clear()
        startRPC("custom")
    elif rpc_choice == "1?":
        clear()
        print("Set a fully custom RPC that has buttons etc!")
        print(fore.YELLOW + "*A LOT OF INPUTS ARE NEEDED FOR THIS RPC*")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #Computer Stats
    elif rpc_choice == "2":
        clear()
        startRPC("compStats")
    elif rpc_choice == "2?":
        clear()
        print("Cycles through your cpu stats. E.G: Intel i7 13700KF")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #CPU and RAM Monitor
    elif rpc_choice == "3":
        clear()
        startRPC("compUsage")
    elif rpc_choice == "3?":
        clear()
        print("Will set your status to your current CPU and RAM usage")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #local time (the easiest one to code lol)
    elif rpc_choice == "4":
        clear()
        startRPC("localTime")
    elif rpc_choice == "3?":
        clear()
        print("Will set your presence to your local time/date and show the timezone you are in.")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #local weather (the literal hardest one to do... so many get and post requests.. please help me eeemememeememmeeeeeee)
    elif rpc_choice == "5":
        clear()
        startRPC("localWeather")
    elif rpc_choice == "5?":
        clear()
        print(f"Cycles through the weather detail of your location based on IP. {fore.YELLOW}*NO IP ADDRESSES ARE SENT ANYWHERE!!!!!*")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()
    #More coming never lmao
    elif rpc_choice == "6":
        clear()
        print("More coming soon! Send suggestions in the github issues tab.")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()
    elif rpc_choice == "6?":
        clear()
        print("More coming soon! Send suggestions in the github issues tab.")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #exit ze program
    elif rpc_choice == "7":
        clear()
        print("Exiting...")
        sys.exit()
    elif rpc_choice == "7?":
        clear()
        print("Exits the program")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()

    #bruv put a valid option already
    else:
        clear()
        print(fore.RED + "Not a valid option...")
        input(fore.GREEN + "[ENTER]")
        chooseRPC()


def startRPC(type):
    global customSave1
    global customSave2
    global customSave3
    global app_id
    global state
    global detail
    global largeImage
    global largeImageText
    global smallImage
    global smallImageText
    global buttonText
    global buttonURL
    #Custom
    clear()
    if type == "custom":
        #I have to mf check every single string to make sure the user enters the correct format :(
        noLargeImage = False
        noSmallImage = False

        askLoad = input(fore.WHITE + "[Y/N] Do you want to load a save?")
        if askLoad.lower() == "n":
            print(fore.WHITE + "Follow the steps in the github README.")
            input(fore.GREEN + "[ENTER]")
            clear()
            app_id = input("*Application ID: ")
            state1 = input("State: ")
            detail = input("Details: ")
            largeImage = input("Large Image: ")
            if largeImage == "":
                noLargeImage = True
                noSmallImage = True
                pass
            else:
                largeImageText = input("Large Image Text: ")
                smallImage = input("Small Image: ")
                if smallImage == "":
                    noSmallImage = True
                    pass
                else:
                    smallImageText = input("Small Image Text: ")

            buttonText = input("Button Text: ")
            if buttonText == "":
                buttonText = "👀Want Custom Status Too?👀"
                buttonURL = "https://github.com/der0r0"
            else:
                buttonURL = input("Button URL: ")

            clear()
            askSave = input("[Y/N] Do you want to save this?")

            if askSave.lower() == "y":
                def tempFunction():
                    global app_id
                    global state
                    global detail
                    global largeImage
                    global largeImageText
                    global smallImage
                    global smallImageText
                    global buttonText
                    global buttonURL
                    print("[1/2/3] What do you want to save to?")
                    askSave2 = input(fore.GREEN + "?: ")
                    
                    if askSave2 == "1" or askSave2 == "2" or askSave2 == "3":
                        if noSmallImage:
                            smallImage = None
                            smallImageText = None
                        if noLargeImage:
                            largeImage = None
                            largeImageText = None

                        print(largeImage)

                        tempData = {
                            "app_id": app_id,
                            "state": state1,
                            "detail": detail,
                            "largeImage": largeImage,
                            "largeImageText": largeImageText,
                            "smallImage": smallImage,
                            "smallImageText": smallImageText,
                            "buttonText": buttonText,
                            "buttonURL": buttonURL
                        }
                        with open(f'customSave{askSave2}.json', 'w') as file:
                            json.dump(tempData, file, indent=4)

                        print("Data successfully written into the file!")

                    else:
                        clear()
                        print("Not a valid number...")
                        input(fore.GREEN + "[ENTER]")
                        tempFunction()

                tempFunction()


            elif askSave.lower() == "n":
                pass
                    






        elif askLoad.lower() == "y":
            clear()
            print("[1/2/3] What save file would you want to load?")
            print(f"Type {fore.GREEN}'?'{fore.WHITE} after a save file to see the contents")
            askLoad2 = input(fore.GREEN + "?: ")
            if askLoad2 == "1":
                #Check for some stuff idk
                if customSave1["app_id"] == None:
                    clear()
                    print(fore.WHITE + "This save is empty")
                    input("[ENTER]")
                    startRPC("custom")
                else:
                    app_id = customSave1["app_id"]
                    state1 = customSave1["state"]
                    detail = customSave1["detail"]
                    #Check for large image
                    if customSave1["largeImage"] != None:
                        largeImage = customSave1["largeImage"]
                        largeImageText = customSave1["largeImageText"]
                        if customSave1["smallImage"] != None:
                            smallImage = customSave1["smallImage"]
                            smallImageText = customSave1["smallImageText"]
                        else:
                            noSmallImage = True
                    else:
                        noLargeImage = True
                        noSmallImage = True
                        pass
                    

                    #Check for Button

                    if customSave1["buttonText"] != None:
                        buttonText = customSave1["buttonText"]
                        buttonURL = customSave1["buttonURL"]
                    else:
                        buttonText = "👀Want Custom Status Too?👀"
                        buttonURL = "https://github.com/der0r0"

            elif askLoad2 == "1?":
                clear()
                print(f"{fore.WHITE} Application ID: {customSave1["app_id"]}")
                print(f"State: {customSave1["state"]}")
                print(f"Detail: {customSave1["detail"]}")
                print(f"Large Image: {customSave1["largeImage"]}")
                print(f"Large Image Text: {customSave1["largeImageText"]}")
                print(f"Small Image: {customSave1["smallImage"]}")
                print(f"Small Image Text: {customSave1["smallImageText"]}")
                print(f"Button Text: {customSave1["buttonText"]}")
                print(f"Button URL: {customSave1["buttonURL"]}")
                input("[ENTER]")
                clear()
                startRPC("custom")




            elif askLoad2 == "2":
                #Check for some stuff idk
                if customSave2["app_id"] == None:
                    clear()
                    print(fore.WHITE + "This save is empty")
                    input("[ENTER]")
                    startRPC("custom")
                else:
                    app_id = customSave2["app_id"]
                    state1 = customSave2["state"]
                    detail = customSave2["detail"]
                    #Check for large image
                    if customSave2["largeImage"] != None:
                        largeImage = customSave2["largeImage"]
                        largeImageText = customSave2["largeImageText"]
                        if customSave2["smallImage"] != None:
                            smallImage = customSave2["smallImage"]
                            smallImageText = customSave2["smallImageText"]
                        else:
                            noSmallImage = True
                    else:
                        noLargeImage = True
                        noSmallImage = True
                        pass
                    

                    #Check for Button

                    if customSave2["buttonText"] != None:
                        buttonText = customSave2["buttonText"]
                        buttonURL = customSave2["buttonURL"]
                    else:
                        buttonText = "👀Want Custom Status Too?👀"
                        buttonURL = "https://github.com/der0r0"

            elif askLoad2 == "2?":
                clear()
                print(f"{fore.WHITE} Application ID: {customSave2["app_id"]}")
                print(f"State: {customSave2["state"]}")
                print(f"Detail: {customSave2["detail"]}")
                print(f"Large Image: {customSave2["largeImage"]}")
                print(f"Large Image Text: {customSave2["largeImageText"]}")
                print(f"Small Image: {customSave2["smallImage"]}")
                print(f"Small Image Text: {customSave2["smallImageText"]}")
                print(f"Button Text: {customSave2["buttonText"]}")
                print(f"Button URL: {customSave2["buttonURL"]}")
                input("[ENTER]")
                clear()
                startRPC("custom")


            elif askLoad2 == "3":
                #Check for some stuff idk
                if customSave3["app_id"] == None:
                    clear()
                    print(fore.WHITE + "This save is empty")
                    input("[ENTER]")
                    startRPC("custom")
                else:
                    app_id = customSave3["app_id"]
                    state1 = customSave3["state"]
                    detail = customSave3["detail"]
                    #Check for large image
                    if customSave3["largeImage"] != None:
                        largeImage = customSave3["largeImage"]
                        largeImageText = customSave3["largeImageText"]
                        if customSave3["smallImage"] != None:
                            smallImage = customSave3["smallImage"]
                            smallImageText = customSave3["smallImageText"]
                        else:
                            noSmallImage = True
                    else:
                        noLargeImage = True
                        noSmallImage = True
                        pass
                    

                    #Check for Button

                    if customSave3["buttonText"] != None:
                        buttonText = customSave3["buttonText"]
                        buttonURL = customSave3["buttonURL"]
                    else:
                        buttonText = "👀Want Custom Status Too?👀"
                        buttonURL = "https://github.com/der0r0"

            elif askLoad2 == "3?":
                clear()
                print(f"{fore.WHITE} Application ID: {customSave3["app_id"]}")
                print(f"State: {customSave3["state"]}")
                print(f"Detail: {customSave3["detail"]}")
                print(f"Large Image: {customSave3["largeImage"]}")
                print(f"Large Image Text: {customSave3["largeImageText"]}")
                print(f"Small Image: {customSave3["smallImage"]}")
                print(f"Small Image Text: {customSave3["smallImageText"]}")
                print(f"Button Text: {customSave3["buttonText"]}")
                print(f"Button URL: {customSave3["buttonURL"]}")
                input("[ENTER]")
                clear()
                startRPC("custom")

        

        #Attempt Discord RPC Connection
        try:
            RPC = pypresence.Presence(app_id)
            RPC.connect()

            #No Large Image + No Small Image
            if(noLargeImage & noSmallImage):
                RPC.update(
                    state = str(state1),
                    details = str(detail),
                    buttons = [{"label": str(buttonText), "url": str(buttonURL)}]
                )
            #Large Image + No Small Image
            elif(noLargeImage == False & noSmallImage):
                RPC.update(
                    state = str(state1),
                    details = str(detail),
                    large_image = str(largeImage),
                    large_text = str(largeImageText),
                    buttons = [{"label": str(buttonText), "url": str(buttonURL)}]
                )
            #Large Image + Small Image
            elif(noLargeImage == False & noSmallImage == False):
                RPC.update(
                    state = str(state1),
                    details = str(detail),
                    large_image = str(largeImage),
                    large_text = str(largeImageText),
                    small_image = str(smallImage),
                    small_text = str(smallImageText),
                    buttons = [{"label": str(buttonText), "url": str(buttonURL)}]
                )

            clear()
            print(fore.BLUE + "Successfully Connected To Discord and Started Status!")
            print("You can now minimize this window!")
            print(fore.YELLOW + "TO EXIT: PRESS 'CTRL + C' !")
            print(fore.WHITE + "")

            while True:
                time.sleep(5)
            


        except pypresence.exceptions.DiscordNotFound:
            clear()
            print(fore.RED + "Ensure Discord is Running!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()

        except pypresence.exceptions.PipeClosed:
            clear()
            print(fore.RED + "Discord was shut down. Please re-open discord for the RPC to work!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()

        except pypresence.exceptions.InvalidID:
            clear()
            print(fore.RED + "Application ID does not exist!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()
        
        except KeyboardInterrupt:
            pass
        
        except Exception as e:
            clear()
            print(fore.RED + "An unknown error has occurred! Please create an issue in the github respository with this error copy and pasted")
            print(e)
            input(fore.GREEN + "[EXIT]")

            sys.exit()



        RPC.close()
        chooseRPC()
        






    #Computer Stats
    elif type == "compStats":
        try:
            #vendor_id_raw (GenuineIntel)       brand_raw (Intel(R) Core???? @ ???GHz)   <- Remove @ ???Ghz         hz_advertised (2800000????) remove extra zeros by dividing by (1024*1024*1024)
            increment = 0
            vendor_id = cpu["vendor_id_raw"]
            cpuTypeBefore = cpu["brand_raw"]
            cpuType = ""
            for i in range(len(cpuTypeBefore)):
                if cpuTypeBefore[i] != "@":
                    cpuType = cpuType + cpuTypeBefore[i]
                else:
                    break
            cpuGhz = str(cpu["hz_advertised_friendly"])
            cpuCores = str(cpu["count"]) + " Cores"
            cpubite = cpu["bits"]
            cpuBits = str(cpu["bits"]) + " Bits"
            thingsToList = [vendor_id, cpuType, cpuCores, cpuBits, cpuGhz]
            RPC = pypresence.Presence(1215116173319086100)
            RPC.connect()
            clear()
            print(fore.BLUE + "Successfully Connected To Discord and Started Status!")
            print("You can now minimize this window!")
            print(fore.YELLOW + "TO EXIT: PRESS 'CTRL + C' !")
            print(fore.WHITE + "")
            while True:
                if increment == 0:
                    image = "company"
                elif increment == 1:
                    image = "cpu"
                elif increment == 2:
                    image = "cpucores"
                elif increment == 3:
                    if cpubite == 32:
                        image = "cpubit32"
                    elif cpubite == 64:
                        image = "cpubit64"
                    else:
                        image = "cpu"
                        #WTF? NO BIT?????
                elif increment == 4:
                    image = "cpughz"

                RPC.update(
                    state = str(thingsToList[increment]),
                    large_image = image,
                    large_text = "CPU Images"
                )
                time.sleep(3)
                if increment < 4:
                    increment += 1
                else:
                    increment = 0
        except pypresence.exceptions.DiscordNotFound:
            clear()
            print(fore.RED + "Ensure Discord is Running!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()

        except KeyboardInterrupt:
            pass

        except pypresence.exceptions.PipeClosed:
            clear()
            print(fore.RED + "Discord was shut down. Please re-open discord for the RPC to work!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()


        except Exception as e:
            clear()
            print(fore.RED + "An unknown error has occurred! Please create an issue in the github respository with this error copy and pasted")
            print(e)
            input(fore.GREEN + "[EXIT]")
            sys.exit()


        clear()
        chooseRPC()

            


    #CPU and RAM
    elif type == "compUsage":
        try:
            RPC = pypresence.Presence(1215050299488608296)
            RPC.connect()
            print(fore.BLUE + "Successfully Connected To Discord and Started Status!")
            print("You can now minimize this window!")
            print(fore.YELLOW + "TO EXIT: PRESS 'CTRL + C' !")
            print(fore.WHITE + "")
            try:
                while True:
                    cpuUsage = psutil.cpu_percent()
                    ramUsage = psutil.virtual_memory().used
                    totalRAM =  psutil.virtual_memory().total
                    time.sleep(0)
                    if cpuUsage <= 20:
                        largeImage = "low"
                    elif 20 < cpuUsage < 80:
                        largeImage = "medium"
                    elif cpuUsage >= 80:
                        largeImage = "high"


                    RPC.update(
                        state = "CPU: " + str(cpuUsage) + "%",
                        details = "RAM: " + str(round(ramUsage / (1024*1024*1024), 1)) + "/" + str(round(totalRAM / (1024*1024*1024), 1)) + "  GB",
                        large_image = largeImage,
                        large_text = "https://github.com/R0R0"
                    )
                    time.sleep(0.5)
            except KeyboardInterrupt:
                pass

            clear()
            RPC.close()
            chooseRPC()


        except pypresence.exceptions.DiscordNotFound:
            clear()
            print(fore.RED + "Ensure Discord is Running!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()

        except pypresence.exceptions.PipeClosed:
            clear()
            print(fore.RED + "Discord was shut down. Please re-open discord for the RPC to work!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()


        except Exception as e:
            clear()
            print(fore.RED + "ERR 0")
            print(fore.RED + "An unknown error has occurred! Please create an issue in the github respository with this error copy and pasted")
            print(e)
            input(fore.GREEN + "[EXIT]")
            sys.exit()



    #Local Time
    elif type == "localTime":
        try:
            currentTime = datetime.datetime.now()
            currentDate = datetime.date.today()
            currentDateFormatted = currentDate.strftime("%A, %m/%d/%Y")
            timezone = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo

            RPC = pypresence.Presence(1217252464491888801)
            RPC.connect()

            clear()
            print(fore.BLUE + "Successfully Connected To Discord and Started Status!")
            print("You can now minimize this window!")
            print(fore.YELLOW + "TO EXIT: PRESS 'CTRL + C' !")
            print(fore.WHITE + "")

            while True:
                currentTime = datetime.datetime.now()
                RPC.update(
                    state = str(currentTime.hour) + ":" + str(currentTime.minute) + ":" + str(currentTime.second) + "     "  + str(timezone),
                    details = currentDateFormatted,
                    large_image = "clock",
                    large_text = "https://github.com/R0R0"
                )
                time.sleep(1)
        except pypresence.exceptions.DiscordNotFound:
            clear()
            print(fore.RED + "Ensure Discord is Running!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()

        except KeyboardInterrupt:
            pass

        except pypresence.exceptions.PipeClosed:
            clear()
            print(fore.RED + "Discord was shut down. Please re-open discord for the RPC to work!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()


        except Exception as e:
            clear()
            print(fore.RED + "An unknown error has occurred! Please create an issue in the github respository with this error copy and pasted")
            print(e)
            input(fore.GREEN + "[EXIT]")
            sys.exit()


    #Local Weather
    elif type == "localWeather":
        global settings
        global weatherConfig
        global currentPath
        #Useful Vars
        apiKey = weatherConfig["apiKey"]
        displayLocation = weatherConfig["displayLocation"]
        displayLastUpdated = weatherConfig["displayLastUpdated"]
        displayMetric = weatherConfig["metric"]
        displayTemp = weatherConfig["temp"]
        displayFeelLike = weatherConfig["feelLike"]
        displayCondition = weatherConfig["condition"]
        displayWind = weatherConfig["wind"]
        displayWind_direction = weatherConfig["wind_direction"]
        displayPressure = weatherConfig["pressure"]
        displayAqi = weatherConfig["aqi"]
        displayUV = weatherConfig["uv"]


        if settings["ipConsent"] == True:
            #Check if everything is filled out
            if weatherConfig["filledOut?"] == False:
                clear()
                apiKey = input(fore.GREEN + "[PASTE] API Key: ")
                displayLocation = input(fore.GREEN + "[T/F] Display (nearby) Location?: ")
                displayLastUpdated = input(fore.GREEN + "[T/F] Display Last Updated?: ")
                displayMetric = input(fore.GREEN + "[T/F] Metric?: ")
                displayTemp = input(fore.GREEN + "[T/F] Display Temp?: ")
                displayFeelLike = input(fore.GREEN + "[T/F] Display Feel Like Temp?: ")
                displayCondition = input(fore.GREEN + "[T/F] Display Conditions (e.g: cloudy)?: ")
                displayWind = input(fore.GREEN + "[T/F] Display Wind Speed?: ")
                displayWind_direction = input(fore.GREEN + "[T/F] Display Wind Direction?: ")
                displayPressure = input(fore.GREEN + "[T/F] Display Pressure?: ")
                displayAqi = input(fore.GREEN + "[T/F] Display AQI? (MAY NOT BE ACCURATE!): ")
                displayUV = input(fore.GREEN + "[T/F] Display UV?: ")

                print("If you made any mistakes, you can go back and fix them later.")
                input(fore.GREEN + "[ENTER]")

                weatherConfig = {
                    "filledOut?": True,
                    "apiKey": apiKey,
                    "displayLocation": displayLocation,
                    "displayLastUpdated": displayLastUpdated,
                    "metric": displayMetric,
                    "temp": displayTemp,
                    "feelLike": displayFeelLike,
                    "condition": displayCondition,
                    "wind": displayWind,
                    "wind_direction": displayWind_direction,
                    "pressure": displayPressure,
                    "aqi": displayAqi,
                    "uv": displayUV
                }

                with open(f'{currentPath}\weatherConfig.json', 'w') as file:
                    json.dump(weatherConfig, file, indent=4)
                print("Successfully Saved Settings")
                clear()
                print(fore.WHITE + f"Done!")
                input(fore.GREEN + "[ENTER]")
                startRPC("localWeather")


            print(fore.WHITE + "[1] Start RPC")
            print("[2] Change Preferences")

            x = input(fore.GREEN + "?: ")

            if x == "1":
                pass
            elif x == "2":
                clear()
                apiKey = input(fore.GREEN + "[PASTE] API Key: ")
                displayLocation = input(fore.GREEN + "[T/F] Display (nearby) Location?: ")
                displayLastUpdated = input(fore.GREEN + "[T/F] Display Last Updated?: ")
                displayMetric = input(fore.GREEN + "[T/F] Metric?: ")
                displayTemp = input(fore.GREEN + "[T/F] Display Temp?: ")
                displayFeelLike = input(fore.GREEN + "[T/F] Display Feel Like Temp?: ")
                displayCondition = input(fore.GREEN + "[T/F] Display Conditions (e.g: cloudy)?: ")
                displayWind = input(fore.GREEN + "[T/F] Display Wind Speed?: ")
                displayWind_direction = input(fore.GREEN + "[T/F] Display Wind Direction?: ")
                displayPressure = input(fore.GREEN + "[T/F] Display Pressure?: ")
                displayAqi = input(fore.GREEN + "[T/F] Display AQI? (MAY NOT BE ACCURATE!): ")
                displayUV = input(fore.GREEN + "[T/F] Display UV?: ")

                print("If you made any mistakes, you can go back and fix them later.")
                input(fore.GREEN + "[ENTER]")

                weatherConfig = {
                    "filledOut?": True,
                    "apiKey": apiKey,
                    "displayLocation": displayLocation,
                    "displayLastUpdated": displayLastUpdated,
                    "metric": displayMetric,
                    "temp": displayTemp,
                    "feelLike": displayFeelLike,
                    "condition": displayCondition,
                    "wind": displayWind,
                    "wind_direction": displayWind_direction,
                    "pressure": displayPressure,
                    "aqi": displayAqi,
                    "uv": displayUV
                }

                with open(f'{currentPath}\weatherConfig.json', 'w') as file:
                    json.dump(weatherConfig, file, indent=4)
                print("Successfully Saved Settings")
                clear()
                print(fore.WHITE + f"Done!")
                input(fore.GREEN + "[ENTER]")
                startRPC("localWeather")
            else:
                clear()
                print(fore.WHITE + "Choose A Valid Choice!")
                input(fore.GREEN + "[ENTER]")
                startRPC("localWeather")

            try:
                apiKey = weatherConfig["apiKey"]
                ipRequest = requests.get("https://httpbin.org/ip")
                ip = ipRequest.json()["origin"]
                url = "https://api.weatherapi.com/v1/current.json?key=" + apiKey + "&q=" + ip + "&aqi=yes"
                weatherData = requests.get(url)
                weatherData = weatherData.json()
                weatherCycle = []
                weatherDataLocation = weatherData["location"]
                weatherDataCurrent = weatherData["current"]


                #This took like 10 minutes to write all out... I don't like this api ngl... though its useful :D
                conditionList = {
                    "1000": "Sunny",
                    "1003": "Partly Cloudy",
                    "1006": "Cloudy",
                    "1009": "Overcast",
                    "1030": "Mist",
                    "1063": "Patchy Rain Possible",
                    "1066": "Patchy Snow Possible",
                    "1069": "Patchy Sleet Possible",
                    "1072": "Patchy Freezing Drizzle Possible",
                    "1087": "Thunder Outbreaks Possible",
                    "1114": "Blowing Snow",
                    "1117": "Blizzard",
                    "1135": "Fog",
                    "1147": "Freezing Fog",
                    "1150": "Patchy Light Drizzle",
                    "1153": "Light Drizzle",
                    "1168": "Freezing Drizzle",
                    "1171": "Heavy Freezing Drizzle",
                    "1180": "Patchy Light Rain",
                    "1183": "Light Rain",
                    "1186": "Moderate Rain at Times",
                    "1189": "Moderate Rain",
                    "1192": "Heavy Rain at Times",
                    "1195": "Heavy Rain",
                    "1198": "Light Freezing Rain",
                    "1201": "Moderate or Heavy Freezing Rain",
                    "1204": "Light Sleet",
                    "1207": "Moderate or Heavy Sleet",
                    "1210": "Patchy Light Snow",
                    "1213": "Light Snow",
                    "1216": "Patchy Moderate Snow",
                    "1219": "Moderate Snow",
                    "1222": "Patchy Heavy Snow",
                    "1225": "Heavy Snow",
                    "1237": "Ice Pellets",
                    "1240": "Light Rain Shower",
                    "1243": "Moderate or Heavy Rain Shower",
                    "1246": "Torrential Rain Shower",
                    "1249": "Light Sleet Showers",
                    "1252": "Moderate or Heavy Sleet Showers",
                    "1255": "Light Snow Showers",
                    "1258": "Moderate or Heavy Snow Showers",
                    "1261": "Light Showers of Ice Pellets",
                    "1264": "Moderate or Heavy Showers of Ice Pellets",
                    "1273": "Patchy Light Rain with Thunder",
                    "1276": "Moderate or Heavy Rain with Thunder",
                    "1279": "Patchy Light Snow with Thunder",
                    "1282": "Moderate or Heavy Snow with Thunder"
                }


                #Handle the error in which case, the api key either doesn't exist or the api can't find the location on where the user is.
                try:
                    clear()
                    if weatherData["error"]["message"] == "No matching location found":
                        print(fore.WHITE + "No location")
                    elif weatherData["error"]["message"] == "API key has been disabled.":
                        print(fore.WHITE + "API Key doesn't exist :O")
                    input(fore.GREEN + "[ENTER]")
                    clear()
                    return
                except:
                    pass
                

                def updateData():
                    if weatherConfig["displayLocation"] == "t":
                        if weatherDataLocation["country"] == "United States of America":
                            weatherCycle.append(f"{weatherDataLocation["name"]}, {weatherDataLocation["region"]}, USA")
                        else:
                            weatherCycle.append(f"{weatherDataLocation["name"]}, {weatherDataLocation["region"]}, {weatherDataLocation["country"]}")
                    else:
                        pass

                    if weatherConfig["displayLastUpdated"] == "t":
                        weatherCycle.append(f"Last Updated: {weatherDataCurrent["last_updated"]}")
                    else:
                        pass
                    
                    if weatherConfig["temp"] == "t":
                        if weatherConfig["metric"] == "f":
                            weatherCycle.append(f"Temperature (F): {weatherDataCurrent["temp_f"]}")
                        else:
                            weatherCycle.append(f"Temperature (C): {weatherDataCurrent["temp_c"]}")
                    else:
                        pass

                    if weatherConfig["feelLike"] == "t":
                        if weatherConfig["metric"] == "f":
                            weatherCycle.append(f"Feels Like (F): {weatherDataCurrent["feelslike_f"]}")
                        else:
                            weatherCycle.append(f"Feels Like (C): {weatherDataCurrent["feelslike_c"]}")
                    else:
                        pass

                    if weatherConfig["condition"] == "t":
                        conditionCode = weatherDataCurrent["condition"]["code"]
                        weatherCycle.append(f"Condition: {conditionList[str(conditionCode)]}")
                    else:
                        pass

                    if weatherConfig["wind"] == "t":
                        if weatherConfig["metric"] == "f":
                            weatherCycle.append(f"Wind Speed (MPH): {weatherDataCurrent["wind_mph"]}")
                        else:
                            weatherCycle.append(f"Wind Speed (KPH): {weatherDataCurrent["wind_kph"]}")
                    else:
                        pass

                    if weatherConfig["wind_direction"] == "t":
                        weatherCycle.append(f"Wind Direction: {weatherDataCurrent["wind_dir"]}")
                    else:
                        pass

                    if weatherConfig["pressure"] == "t":
                        if weatherConfig["metric"] == "f":
                            weatherCycle.append(f"Pressure (IN): {weatherDataCurrent["pressure_in"]}")
                        else:
                            weatherCycle.append(f"Pressure (MB): {weatherDataCurrent["pressure_mb"]}")
                    else:
                        pass

                    
                    if weatherConfig["aqi"] == "t":
                        #Ze calculations for the aqi!
                        airQuality = weatherDataCurrent["air_quality"]["pm2_5"]
                        if airQuality <= 12:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(50/12), 1)} (Good)")
                        elif 12.1 <= airQuality <= 35.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(100/35.4), 1)} (Moderate)")
                        elif 35.5 <= airQuality <= 55.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(150/55.4), 1)} (Unhealthy for Sensitives)")
                        elif 55.5 <= airQuality <= 150.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(200/150.4), 1)} (Unhealthy)")
                        elif 150.5 <= airQuality <= 250.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(300/250.4), 1)} (Very Unhealthy)")
                        elif 250.5 <= airQuality <= 350.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(400/350.4), 1)} (Hazardous)")
                        elif 350.5 <= airQuality <= 500.4:
                            weatherCycle.append(f"Air Quality (PM_2.5): {round(airQuality*(500/500.4), 1)} (DEAD)")
                        else:
                            weatherCycle.append(f"Air Quality (PM_2.5): OFF THE CHARTS!")
                    else:
                        pass


                    if weatherConfig["uv"] == "t":
                        weatherCycle.append(f"UV/10: {str(weatherDataCurrent["uv"])}")
                    else:
                        pass

                updateData()


                if len(weatherCycle) < 1:
                    print(fore.RED + "There is nothing to cycle through! Change Preferences so at least 1 is enabled.")
                    input(fore.GREEN + "[ENTER]")
                    return
                

                #Temp Vars
                increment1 = 0
                increment2 = 0
                #Start da mother frickin presence :D
                RPC = pypresence.Presence(1217258775027777627)
                RPC.connect()
                clear()
                print(fore.BLUE + "Successfully Connected To Discord and Started Status!")
                print("You can now minimize this window!")
                print(fore.YELLOW + "TO EXIT: PRESS 'CTRL + C' !")
                print(fore.WHITE + "")
                while True:
                    RPC.update(
                        state = weatherCycle[increment1]
                    )
                    time.sleep(5)
                    if increment1 < (len(weatherCycle)-1):
                        increment1 += 1
                    else:
                        increment1 = 0
                        increment2 += 1
                    if increment1 % 60 == 0 & increment1 > 59:
                        print("Updated Weather...")
                        updateData()


            except pypresence.exceptions.DiscordNotFound:
                clear()
                print(fore.RED + "Ensure Discord is Running!")
                input(fore.GREEN + "[ENTER]")
                chooseRPC()

            except KeyboardInterrupt:
                pass

            except pypresence.exceptions.PipeClosed:
                clear()
                print(fore.RED + "Discord was shut down. Please re-open discord for the RPC to work!")
                input(fore.GREEN + "[ENTER]")
                chooseRPC()


            except Exception as e:
                clear()
                print(fore.RED + "An unknown error has occurred! Please create an issue in the github respository with this error copy and pasted")
                print(e)
                input(fore.GREEN + "[EXIT]")
                sys.exit()
        else:
            clear()
            print(fore.RED + "IP Consent is disabled, please rerun the program to get the ip consent prompt!")
            input(fore.GREEN + "[ENTER]")
            chooseRPC()


        clear()
        chooseRPC()


    


#Start it
clear()
program()

#freeze the supportingingignigngin
if __name__ == '__main__':
    freeze_support()


loadData()



