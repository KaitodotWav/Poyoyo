#HoloLinkSender

import discord
from discord.ext import commands

Token = "ODE4ODg3NTYyNzY0MzUzNTg4.YEemeQ.VGPJ7EP-IwJaNPG421-QUU5jym4"
client = commands.Bot(command_prefix = "p!")

cache = [line.strip() for line in open("Data/Chat.txt")]
target = int(cache[0])
channel = client.get_channel(int(target))
#target = int(802882963809239050)


@client.event
async def on_ready():
    channel = client.get_channel(int(target))
    report = client.get_channel(824950744477990942)
    print("We have logged in as {0.user}".format(client))
    #await channel.send("successfully connected to this channel.")
    await report.send("Poyoyo send is now connected to {}".format(target))
    
    while True:
        content = input("Message: ")
        if "/report" in content:
            Replace = content.replace("/report", "Owner")
            await report.send(Replace)
        else:
            convert = str(content)
            await channel.send(convert)

client.run(Token)
