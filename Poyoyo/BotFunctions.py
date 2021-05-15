import discord
import os
import requests, json, random

def GetGuraResponse(select="random"):
    Shark = [line.strip("") for line in open(r"Data\SharkTalk.txt")]
    recent = 0
    if select == "random":
        selector = random.randint(0, len(Shark)-1)
        return str(Shark[selector])


def clean(target):
    sweept = target.strip("< @ ! >")
    return sweept


def writeF(file, content):
    target = open("AFKmsg/{}.txt".format(file), "w", encoding="utf8")
    target.write(content)
    target.close()


def openF(file):
    # print(file)
    msg_file = [line.strip("\ufeff \n") for line in open("AFKmsg/{}.txt".format(file),encoding="utf8")]
    return msg_file[0]


def SetAFKmsg(user, message="n/a", Guild=None):
    with open(r"Data\AFKmsg.json", "r", encoding="utf8") as F:
        readF = F.read()
        buildJSON = json.loads(readF)
    target_user = clean(user)
    try:
        server = buildJSON[f"{Guild}"]
        server[f"{target_user}"] = message
    except:
        buildJSON[f"{Guild}"] = {target_user:message}
        
    with open(r"Data\AFKmsg.json", "w", encoding="utf8") as F:
        json.dump(buildJSON, F, indent=2,ensure_ascii=False)
    
    #writeF(target_user, message)


def GetAFKmsg(user, Guild):
    target_U = clean(user)
    with open(r"Data\AFKmsg.json", encoding="utf8") as F:
        readF = F.read()
        JSON = json.loads(readF)
    try:
        afk_msg = JSON[f"{Guild}"][f"{target_U}"]
    except:
        return "No AFK message has been set"
    else:
        return afk_msg

def GetAFKlist(Guild):
    users = []
    with open(r"Data\AFKmsg.json", "r", encoding="utf8") as F:
        readF = F.read()
        JSON = json.loads(readF)
    for i in JSON[f"{Guild}"]:
        users.append(i)
    """
    raw = os.listdir("AFKmsg")
    users = []
    for i in raw:
        s = i.split(".")
        users.append(s[0])
    """
    return users

def GetContents(fileDir, index=0):
    filet = [line.strip() for line in open("{}".format(fileDir))]
    if index == 0:
        return filet
    else:
        return filet[index]

def Save_User(user_id, user_name):
    save_user = False
    cache = [line.strip() for line in open(r"Data\reg_user.txt")]
    U_id = []
    U_name = []
    for i in range(len(cache)):
        filt = str(cache[i])
        filt2 = filt.split(":")
        U_id.append(filt2[1])
        U_name.append(filt2[0])
    for i in range(len(U_id)):
        if str(U_id[i]) == str(user_id):
            return "User {} is already added as {}".format(user_id, U_name[i])
        else:
            save_user = True
    if save_user:
        filet = open(r"Data\reg_user.txt", "a")
        print("{}:{}".format(user_name, user_id), file=filet)
        filet.close()
        return "User {} has been saved as {}.".format(user_id, user_name)
    else:
        pass

def OpenRecent():
    pass

def SaveRecent(channel):
    fileT = open("Recent.txt", "w")
    fileT.write(channel)
    fileT.close

def Ping(msg="request"):
    F = open("ping.txt", "w")
    F.write(msg)
    F.close()
    
def RPing(args="request"):
    F = [line.strip() for line in open("ping.txt")]
    cache = str(F[0])
    if cache == str(args):
        return True
    else:
        return False

def Convert(target):
    user = []
    userid = []
    cache = [line.strip() for line in open(r"Data\reg_user.txt")]
    final = target
    for i in cache:
        Filt = i.split(":")
        user.append(Filt[0])
        userid.append(Filt[1])
    for i in userid:
        if i in target:
            coords = userid.index(i)
            replace = target.replace(i, user[coords])
            final = replace
    return final

def TRIGGERED(msg):
    triggers = [["min", "gae"]]
    for t in triggers:
        point = 0
        for g in t:
            if g in msg:
                point += 1
        if point == 2:
            return discord.File(r"C:\Users\user\Desktop\GAE.PNG")
    pass
