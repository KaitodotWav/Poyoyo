#Main Poyoyo

import discord
from discord.ext import commands
import CMD, time, sys
from tkinter import *
from threading import Thread
import BotFunctions as BF
import tkinter.messagebox as TKmsg
import configparser, requests, json

#Auth
config = configparser.ConfigParser()
config.read("Properties.ini")
if config["Poyoyo"]["Token"] == "Default":
    getToken = requests.get("https://public.sn.files.1drv.com/y4mUp_D7Mmsn-5tOf45TSsQIlmp0p31_GRBmwlvVdyax48a2zewBu9S3JEB-WSSZS3uUjrN3sMLcdrYHk6YeIji4bgNyc8D8XrEHuwskxJGtxtm4VR6G8MRatNMfa8_ySMKCfklssv9Lq9Qo1aWNa9SwJdyY8b_0nsUxdcASrU8lAVnTp2-K9OP5ujpTSnibpY6pzvDnxiKeOz574aDrm-_dplTWMvvaIJrPe1atGp-VD8?access_token=EwAIA61DBAAUmcDj0azQ5tf1lkBfAvHLBzXl5ugAAR6r/Os2txq5vkU%2bJKj3OqkTc8V7JHvxmrroIljJBfYLJ5noVE4bYGrSegV1U3kKmgRvndNlMHXx%2btVGU52fyCJOfcmZf5ar0yiqzSxkAMjW2weB6zX46Hklc5M9oUy0uKaGZFXZjwfkzqk5tD4Jj9tri%2bFIPyyNCDl0ZGXMiaL8OTU1zbBc5jQc9N/czsRRQczyPCbNAuQU4dBMRcAUBKpE5k5JEp%2bJjjPz8d0FAcGAHNocMzDVq6hDPxFnJejXPp7sdEGNLUr/XUNy4iNQgA3CZula6qESljly7VrmHVCRk%2bJabvB4T0kt4VnuF4X8dvswyDoz8FWlvYKzdHdn3QcDZgAACFqviq7BVShW2AEkYAiDmwz4DFm2z50TPsUC7uH9gjbT2yRNN9NQ/uQlyOd8jwehinOigxpZtFchnmunV71jt2znukrit7pJataT/ABtni2ZwgTtKicn8Mf8M14YCevHnoP7hTBsnwEiH9GAETZPDRZWoEJKdcSfDTeEpAELdYMalnqIEcb5hZx7N8Lg6qclss/IKQm1%2b0STiSFBr5PAp8Pg1tXlu3iLog%2bOJi6kiOsIfv0KNTi0iD98VLiWduV%2bEWffvIuBoTj3w2bVQPFnhj/rIjIEDHktyOHUDQnVl86issHxvhcpa7NVE4ODpnPdk5JLsbYc0J3goyEQHM1CvToqrbmGVYJfqAFlsPRtC3abho7d56hn77dVyFcQWPW4beyVM4DleBqhp4YNSFpO5nXPFP7ThnyUaNR7hiWuuqfWhRgWVnkj/mT0PXhgE/5Bdw%2bVPSOY0OpPzrzQ702kOfAaofQn58BPvUxSHo9N3WgSCjtq0zIWWCz5gqKwBoNE7Y9YV4dsteb2muWjgT5Vy2tUJntOzFyirWEfvTO5x3lUE4tUHovkfWDpJD4ZUlMbVckG6w7qnzX3uZPt25muLw4QK0KNMx3i%2bMsyiEIozRmDIVVyiHj/4BrOveLSObF9G%2b7gDgI%3d")
    Otoken = json.loads(getToken.text)
    fetch_token = Otoken["Poyoyo"]
    Token = str(fetch_token["token"])
else:
    Token = str(config["Poyoyo"]["Token"])

def BOOL(Bool):
    check = Bool.lower()
    if check == "true":
        return True
    elif check == "false":
        return False
    else:
        return False

Debug = BOOL(config["Poyoyo"]["Debug"])
#print(Debug)

client = commands.Bot(command_prefix = str(config["Poyoyo"]["Prefix"]))

#Commands = CMD.CMD(client)
def Commands():
    global client
    coms = CMD.CMD(client)

def WriteF(txt, Directory):
    with open(f"{Directory}", "w") as F:
        F.write(txt)  

#Instance Checker
def ShowWarning(TITLE, MESSAGE):
    root = Tk()
    root.withdraw()
    TKmsg.showwarning(title=TITLE, message=MESSAGE)

from tendo import singleton
try:
    me = singleton.SingleInstance()
except:
    warnThread = Thread(target=ShowWarning, args=("Error: Multiple Instance", "Main program is already running."))
    warnThread.start()
    WriteF("Error: Reject launch\nMain program is already running", "MainReport.txt")
    print("done")
    sys.exit(-1)
else:
    pass

#Threads
run_cmd = Thread(target=Commands)

def CheckUp():
    CMDLines = len([line.strip("\ufeff \n") for line in open("CMD.py", encoding="utf8")])
    BotLines = len([line.strip() for line in open("BotFunctions.py")])
    RaphLines = len([line.strip() for line in open("Raphael.pyw", encoding="utf8")])
    oldLines = [line.strip() for line in open(r"Data\Lines.txt")]
    Line1 = ""
    Line2 = ""
    Line3 = ""
    Save1 = 0
    Save2 = 0
    Save3 = 0
    if int(oldLines[0]) > CMDLines:
        Line1 = "{} Line/s of code has been removed from CMD.py total of {}".format(int(oldLines[0]) - CMDLines, CMDLines)
    elif int(oldLines[0]) < CMDLines:
        Line1 = "{} Line/s of code has been added from CMD.py total of {}".format(CMDLines - int(oldLines[0]), CMDLines)
    elif int(oldLines[0]) == CMDLines:
        if Debug:
            Line1 = "CMD.py has no changes"
    if int(oldLines[1]) > BotLines:
        Line2 = "{} Line/s of code has been removed from BotFunctions.py total of {}".format(int(oldLines[1]) - BotLines, BotLines)
    elif int(oldLines[1]) < BotLines:
        Line2 = "{} Line/s of code has been added from BotFunctions.py total of {}".format(BotLines - int(oldLines[1]), BotLines)
    elif int(oldLines[1]) == BotLines:
        if Debug:
            Line2 = "BotFunctions.py has no changes"
    if int(oldLines[2]) > RaphLines:
        Line3 = "{} Line/s of code has been removed from Raphael.py total of {}".format(int(oldLines[2]) - RaphLines, RaphLines)
    elif int(oldLines[2]) < RaphLines:
        Line3 = "{} Line/s of code has been added from Raphael.py total of {}".format(RaphLines - int(oldLines[2]), RaphLines)
    elif int(oldLines[2]) == RaphLines:
        if Debug:
            Line2 = "Raphael.py has no changes"
    Save = open(r"Data\Lines.txt", "w")
    Save.write("{}\n{}\n{}".format(CMDLines, BotLines, RaphLines))
    Save.close()
    return Line1, Line2, Line3


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))
    report = client.get_channel(int(config["MessageChannel"]["Report"]))
    await report.send("Konnakiri!! {0.user} is online.".format(client))
    if Debug:
        await report.send("Warning {0.user} is running on debug mode.".format(client))
    #Diagnose
    rpt1, rpt2, rpt3 = CheckUp()
    if rpt1 != "":
        await report.send(rpt1)
    if rpt2 != "":
        await report.send(rpt2)
    if rpt3 != "":
        await report.send(rpt3)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=str(config["Poyoyo"]["Presence"])))

#run
run_cmd.start()
client.run(Token)
