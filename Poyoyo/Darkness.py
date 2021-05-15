import discord
from discord.ext import commands
import CMD, time, sys, os
from threading import Thread

def Arrange(file, past=None, NSFWdir=None):
    Send = []
    Folder = []
    for i in file:
        if past != None:
            if "." in str(i):
                Send.append(f"{past}\\{i}")
            else:
                Folder.append(f"{past}\\{i}")
        else:
            if "." in str(i):
                Send.append(f"{NSFWdir}\\{i}")
            else:
                Folder.append(f"{NSFWdir}\\{i}")
    return Send, Folder

def WriteF(txt, cache_file, debug=False):
    with open(f"{cache_file}", "w", encoding="utf8") as F:
        F.write(txt)
        if debug:
            print(txt)

def AddF(txt, cache_file, debug=False):
    with open(f"{cache_file}", "a", encoding="utf8") as F:
        print(txt, file=F)
        if debug:
            print(txt)

class LEWD():
    def __init__(self, Lewds, Cache):
        self.lewd = Lewds
        self.cache = None
        self.raid = os.listdir(self.lewd)
        self.Lfiles = []
        self.Lfolders = []
        self.horni = Cache
        self.for_save = []
        self.new = None

    def getNew(self):
        self.raid = os.listdir(self.lewd)
        self.cache = [line.strip("\ufeff \n") for line in open(f"{self.horni}", encoding="utf8")]
        Files, Folder = Arrange(self.raid, NSFWdir=self.lewd)
        self.Lfolders = Folder
        self.Lfiles = Files
        newData = Files
        oldData = self.cache
        
        for i in self.Lfolders:
            files = os.listdir(i)
            get, folder = Arrange(files, i)
            for g in get:
                self.Lfiles.append(g)
            for f in folder:
                self.Lfolders.append(f)
        self.new = []
        oldload = []
        for i in self.Lfiles:
            line_count = 0
            for S in oldData:
                if i == S:
                    pass
                else:
                    line_count += 1
            if line_count == len(oldData):
                self.new.append(i)
            else:
                oldload.append(i)
        self.for_save = oldload
        if len(self.Lfiles) < len(self.cache):
            print("update")
        build = ""
        for s in oldload:
            ne = s + "\n"
            build += ne
        WriteF(build, self.horni)
        #print(oldload)
        return self.new

    def Save(self, target):
        for i in self.new:
            if i == target:
                self.for_save.append(target)
                #print(self.for_save)
                build = ""
                for s in self.for_save:
                    ne = s + "\n"
                    build += ne
                self.new.remove(target)
                WriteF(build, self.horni)
                
    def Save2(self, target):
        for i in self.new:
            if i == target:
                self.for_save.append(target)
                self.new.remove(target)
                AddF(target, self.horni)

if __name__ == "__main__":
    NSFWdir = r"D:\NSFW"
    oldData = "Data\\LEWDS.txt"
    bonk = LEWD(NSFWdir, oldData)
    while True:
        send_list = bonk.getNew()
        if len(send_list)>=1:
            for i in send_list:
                print(f"//{i}")
                bonk.Save2(i)
                #time.sleep(3)
        time.sleep(1)
        #print(f"=={send_list}")
