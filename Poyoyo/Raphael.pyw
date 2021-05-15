import discord
from discord.ext import commands
import CMD, time, sys
from threading import Thread
import BotFunctions as BF
MaxPing = 15
WarningPing = 7
MissedPing = 0

loadToken = [line.strip() for line in open("Token.txt")]
Token = str(loadToken[0])
client = commands.Bot(command_prefix = "p!")

def WriteP(w):
    F = open(r"Data\Raphael\run.txt", "w")
    F.write(str(w))
    F.close()

@client.event
async def on_ready():
    report = client.get_channel(824950744477990942)
    await report.send("Raphael is successfuly connected.")
    WriteP(1)
    global MaxPing
    global MissedPing
    rep = client.get_channel(824950744477990942)
    while True:
        request = BF.RPing("Konpeko")
        if request:
            BF.Ping("Nyahallo")
            MissedPing = 0
        else:
            MissedPing += 1
        if MissedPing == WarningPing:
            await rep.send("『Raphael』\nNotice: Poyoyo missed {} pings main program is not responding or shutted down poyoyo will be closed after {} ping".format(WarningPing, MaxPing))
        if MissedPing == MaxPing:
            await rep.send("『Raphael』\nNotice: Poyoyo missed all pings commencing shutdown.")
            await rep.send("Jaa~ Otsunakiri!!")
            WriteP(0)
            sys.exit()
        time.sleep(2)

client.run(Token)
