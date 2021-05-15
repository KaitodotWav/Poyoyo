import discord
from discord.ext import commands
import CMD, time, sys, os, Darkness
from threading import Thread
import setproctitle as proTitle
from tkinter import *
import tkinter.messagebox as TKmsg

MCdir = "C:\\Users\\user\\AppData\\Roaming\\.minecraft\\screenshots"
MCcache = r"Data\GreatSage\MCscreenshots.txt"
NSFWdir = r"D:\NSFW"
NSFWcache = "Data\\LEWDS.txt"
OSUdir = r"D:\Program Files\osu!\Screenshots"
OSUcache = r"Data\GreatSage\OsuSC.txt"

loadToken = [line.strip() for line in open("Token.txt")]
Token = str(loadToken[0])
client = commands.Bot(command_prefix = "p!")
cache = [line.strip() for line in open(r"Data\Chat.txt")]
MCchannel = int(cache[0])

def LoadSettings(Variable, Bool=False):
    var = []
    val = []
    get = [line.strip("\n") for line in open(r"Data\GreatSageSettings.txt")]
    for i in get:
        Filter = i.split("=")
        remspace_var = ""
        remspace_val = ""
        for f in Filter[0]:
            if f == " ":
                pass
            else:
                remspace_var += f
        for f in Filter[1]:
            if f == " ":
                pass
            else:
                remspace_val += f
        var.append(remspace_var)
        val.append(remspace_val)
    get_index = var.index(Variable)
    if Bool:
        if int(val[get_index]) == 1:
            return True
        elif int(val[get_index]) == 0:
            return False
    else:
        return val[get_index]

def WriteF(txt, Directory):
    with open(f"{Directory}", "w") as F:
        F.write(txt)  

class SCREENSHOT():
    def __init__(self, Directory, Cache):
        self.Dir = Directory
        self.cache = Cache
        self.new = []
        self.for_save = []

    def CheckNew(self):
        pictures = os.listdir(self.Dir)
        oldPic = [line.strip() for line in open(f"{self.cache}")]
        new = []
        old = []
        converted = []
        for p in pictures:
            p = f"{self.Dir}\\{p}"
            converted.append(p)
            load = 0
            for o in oldPic:
                if p == o:
                    pass
                else:
                    load += 1
            if load == len(oldPic):
                self.new.append(f"{p}")
            else:
                old.append(f"{p}")
        self.for_save = converted
        build = ""
        for s in self.for_save:
            ne = s + "\n"
            build += ne
        WriteF(build, self.cache)
        return self.new

    def Save(self, target):
        for i in self.new:
            if i == target:
                self.for_save.append(target)
                build = ""
                for s in self.for_save:
                    ne = s + "\n"
                    build += ne
                self.new.remove(target)
                WriteF(build, self.cache)
        
Minecraft = SCREENSHOT(MCdir, MCcache)
Lewds = Darkness.LEWD(NSFWdir, NSFWcache)
Osu = SCREENSHOT(OSUdir, OSUcache)

def InstanceUpdate():
    run_cache = [line.strip() for line in open(r"Data\GreatSage\run.txt")]
    run_sys  = run_cache[0]
    if int(run_sys) == 0:
        sys.exit()

def ShowWarning(TITLE, MESSAGE):
    root = Tk()
    root.withdraw()
    TKmsg.showwarning(title=TITLE, message=MESSAGE)

#Instance Checker
from tendo import singleton
try:
    me = singleton.SingleInstance()
except:
    warnThread = Thread(target=ShowWarning, args=("Multiple Instance", "Great Sage is already running."))
    warnThread.start()
    WriteF("Great Sage is already running", "GreatSageReport.txt")
    print("done")
    sys.exit(-1)
else:
    pass

@client.event
async def on_ready():
    report = client.get_channel(824950744477990942)
    await report.send("Great Sage is active.")

    debug = LoadSettings("debug", True)
    if debug:
        await report.send("Warning Great Sage is running on debug mode")
    

    first_run = False
    loops = 0

    #Channels
    MCCH = client.get_channel(int(MCchannel))
    LewdCH = client.get_channel(int(535852756947304458))
    OSUCH = client.get_channel(int(801785825016807466))
    
    while True:
        debug = LoadSettings("debug", True)
        allow_send = LoadSettings("allow_send", True)
        
        #Minecraft
        MClist = Minecraft.CheckNew()
        if len(MClist)>=1:
            for i in MClist:
                if first_run:
                    if allow_send:
                        await MCCH.send(file=discord.File(f"{i}"))
                Minecraft.Save(i)
                if debug:
                    print(i)
                time.sleep(3)

        #LEWDS
        LewdList = Lewds.getNew()
        if len(LewdList)>=1:
            for i in LewdList:
                if allow_send:
                    await LewdCH.send(file=discord.File(f"{i}"))
                Lewds.Save2(i)
                if debug:
                    print(i)
                time.sleep(1)
        
        #Osu!
        Osulist = Osu.CheckNew()
        if len(Osulist)>=1:
            for i in Osulist:
                if first_run:
                    if allow_send:
                        await OSUCH.send(file=discord.File(f"{i}"))
                Osu.Save(i)
                if debug:
                    print(i)
                time.sleep(3)

        if not first_run:
            loops += 1
        if loops >= 3:
            first_run = True
        #print(first_run, loops)
        if debug:
            print(f"debug: {debug}\n" \
                  f"allow send:{allow_send}\n"
                  )
        InstanceUpdate()
        time.sleep(2)

#Instance check
run_cache = [line.strip() for line in open(r"Data\GreatSage\run.txt")]
run_sys  = run_cache[0]
if int(run_sys) == 1:
    #WriteF("Great Sage is already running", "GreatSageReport.txt")
    #sys.exit()
    pass
else:
    WriteF("1", r"Data\GreatSage\run.txt")
        
client.run(Token)
