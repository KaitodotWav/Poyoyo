#HoloLinkSender

import discord, os, sys
from discord.ext import commands

def EXM(target=None, auth=None):
    if config["Poyoyo"]["Token"] == "Default":
        getToken = requests.get("https://public.sn.files.1drv.com/y4mUp_D7Mmsn-5tOf45TSsQIlmp0p31_GRBmwlvVdyax48a2zewBu9S3JEB-WSSZS3uUjrN3sMLcdrYHk6YeIji4bgNyc8D8XrEHuwskxJGtxtm4VR6G8MRatNMfa8_ySMKCfklssv9Lq9Qo1aWNa9SwJdyY8b_0nsUxdcASrU8lAVnTp2-K9OP5ujpTSnibpY6pzvDnxiKeOz574aDrm-_dplTWMvvaIJrPe1atGp-VD8?access_token=EwAIA61DBAAUmcDj0azQ5tf1lkBfAvHLBzXl5ugAAR6r/Os2txq5vkU%2bJKj3OqkTc8V7JHvxmrroIljJBfYLJ5noVE4bYGrSegV1U3kKmgRvndNlMHXx%2btVGU52fyCJOfcmZf5ar0yiqzSxkAMjW2weB6zX46Hklc5M9oUy0uKaGZFXZjwfkzqk5tD4Jj9tri%2bFIPyyNCDl0ZGXMiaL8OTU1zbBc5jQc9N/czsRRQczyPCbNAuQU4dBMRcAUBKpE5k5JEp%2bJjjPz8d0FAcGAHNocMzDVq6hDPxFnJejXPp7sdEGNLUr/XUNy4iNQgA3CZula6qESljly7VrmHVCRk%2bJabvB4T0kt4VnuF4X8dvswyDoz8FWlvYKzdHdn3QcDZgAACFqviq7BVShW2AEkYAiDmwz4DFm2z50TPsUC7uH9gjbT2yRNN9NQ/uQlyOd8jwehinOigxpZtFchnmunV71jt2znukrit7pJataT/ABtni2ZwgTtKicn8Mf8M14YCevHnoP7hTBsnwEiH9GAETZPDRZWoEJKdcSfDTeEpAELdYMalnqIEcb5hZx7N8Lg6qclss/IKQm1%2b0STiSFBr5PAp8Pg1tXlu3iLog%2bOJi6kiOsIfv0KNTi0iD98VLiWduV%2bEWffvIuBoTj3w2bVQPFnhj/rIjIEDHktyOHUDQnVl86issHxvhcpa7NVE4ODpnPdk5JLsbYc0J3goyEQHM1CvToqrbmGVYJfqAFlsPRtC3abho7d56hn77dVyFcQWPW4beyVM4DleBqhp4YNSFpO5nXPFP7ThnyUaNR7hiWuuqfWhRgWVnkj/mT0PXhgE/5Bdw%2bVPSOY0OpPzrzQ702kOfAaofQn58BPvUxSHo9N3WgSCjtq0zIWWCz5gqKwBoNE7Y9YV4dsteb2muWjgT5Vy2tUJntOzFyirWEfvTO5x3lUE4tUHovkfWDpJD4ZUlMbVckG6w7qnzX3uZPt25muLw4QK0KNMx3i%2bMsyiEIozRmDIVVyiHj/4BrOveLSObF9G%2b7gDgI%3d")
        Otoken = json.loads(getToken.text)
        fetch_token = Otoken["Poyoyo"]
        Token = str(fetch_token["token"])
    else:
        Token = str(config["Poyoyo"]["Token"])
    client = commands.Bot(command_prefix = str(config["Poyoyo"]["Prefix"]))
    pidID = os.getpid()
    EINZEIG = int(config["Poyoyo"]["Owner_ID"])
    AyamTat = "https://cdn.discordapp.com/attachments/823857829235785768/834401157223940106/HDayame_tatoo2.jpg"
    
    
    #set Default if none channel
    cache = [line.strip() for line in open("Data/Chat.txt")]
    if target == None:
        target = int(cache[0])
    channel = client.get_channel(int(target))

    @client.event
    async def on_ready():
        channel = client.get_channel(int(target))
        report = client.get_channel(int(config["MessageChannel"]["Report"]))
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
