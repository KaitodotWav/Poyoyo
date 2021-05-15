#HoloLinkSender

import discord, os, sys
from discord.ext import commands

def EXM(target=None, auth=None):
    Token = "ODE4ODg3NTYyNzY0MzUzNTg4.YEemeQ.VGPJ7EP-IwJaNPG421-QUU5jym4"
    client = commands.Bot(command_prefix = "p!")
    pidID = os.getpid()
    EINZEIG = 492610607733014528
    AyamTat = "https://cdn.discordapp.com/attachments/823857829235785768/834401157223940106/HDayame_tatoo2.jpg"
    
    
    #set Default if none channel
    cache = [line.strip() for line in open("Data/Chat.txt")]
    if target == None:
        target = int(cache[0])
    channel = client.get_channel(int(target))

    @client.event
    async def on_ready():
        channel = client.get_channel(int(target))
        report = client.get_channel(824950744477990942)
        auth_user = await client.fetch_user(auth)

        if int(auth) != EINZEIG:
            rejectEB = discord.Embed(title="Request denied.", description=f"User: {auth_user.name} ID: {auth}", color=0x87CEFA)
            rejectEB.add_field(name="Error!", value="You don't have permission to deploy Prüfer Unit", inline=False)
            rejectEB.set_footer(icon_url=AyamTat, text=f"PF{pidID}")
            await channel.send(embed=rejectEB)
            embedVar = discord.Embed(title=f"PF{pidID} terminated.", description=f"Connection request by {auth_user.name} ID: {auth} to {channel} has been denied.", color=0x87CEFA)
            embedVar.add_field(name="Error!", value=f"User:{auth_user.name} don't have permission to use this command", inline=False)
            embedVar.set_footer(icon_url=AyamTat, text=f"PF{pidID}")
            await report.send(embed=embedVar)
            sys.exit()
        
        print(f"PF{pidID} is now active and connected to {channel}.")
        embedVar = discord.Embed(title=f"PF{pidID} is now active.", description=f"Connection request to {channel} has been accepted.", color=0x87CEFA)
        embedVar.set_footer(icon_url=AyamTat, text=f"PF{pidID}")
        await report.send(embed=embedVar)

        embedVar2 = discord.Embed(title=f"Unit: PF{pidID} is now deployed in this channel.", description=f"Connection request to {channel} has been accepted.", color=0x87CEFA)
        embedVar2.set_footer(icon_url=AyamTat, text=f"PF{pidID}")
        await channel.send(embed=embedVar2)
        
        while True:
            content = input("Message: ")
            if "/report" in content:
                Replace = content.replace("/report", "")
                embedrep = discord.Embed(title=f"PF{pidID} report.", description=f"{Replace}", color=0x87CEFA)
                embedrep.set_footer(text=f"PF{pidID}")
                await report.send(embed=embedrep)
            elif "/EXM" in content:
                Replace = content.replace("/EXM", "")
                embedmsg = discord.Embed(title=f"Notice:.", description=f"{Replace}", color=0x87CEFA)
                embedmsg.set_footer(icon_url=AyamTat, text=f"PF{pidID}")
                await channel.send(embed=embedmsg)
            else:
                if len(content) >= 1:
                    convert = str(content)
                    await channel.send(convert)

    client.run(Token)

if __name__ == "__main__":
    args = sys.argv
    if len(args) == 3:
        EXM(int(args[1]), int(args[2]))
    else:
        EXM(int(args[1]))
