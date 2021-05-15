from BotFunctions import *
from threading import Thread
import random, os, subprocess, AsacocoModule, time, sys, json, codecs, pickle
from beepy.make_sound import beep
from plyer.utils import platform
from plyer import notification
from NHentai import NHentai
import asyncio, configparser
import threading as tthread

config = configparser.ConfigParser()
config.read("Properties.ini")

SharkTrigger = ["a", "shark", "A", "あ"]
afk_user = []
prefix = "p!"
DPGS = False
CHANNEL = None
RecentChat = None
RecentChannel = None
NotifTriggers = ["<@!492610607733014528>", "<@492610607733014528>", "kaito", "poyoyo", "<@!818887562764353588>", "<@818887562764353588>"]
Takodachi = "https://pbs.twimg.com/profile_images/1305491092918292485/q6p8QmUl_400x400.jpg"
EINZEIG = int(config["Poyoyo"]["Owner_ID"])
AyamTat = "https://cdn.discordapp.com/attachments/823857829235785768/834401157223940106/HDayame_tatoo2.jpg"

def update_afk_list(GUILD):
    global afk_user
    try:
        afk_user = GetAFKlist(GUILD)
    except:
        pass

def LtoS(List):
    build = ""
    for i in List:
        build += f" {i},"
    return build[1:len(build)-1]

def CMD(client):

    @client.command()
    async def NH(ctx, Code, Option="get"):
        async def get_doujin(msg, Code):
            Doujin = NH._get_doujin(str(Code))
            embD = discord.Embed(title=f"{Doujin.title}", description=f"{Doujin.id}", color=0xFF69B4)
            embD.add_field(name="Characters", value=f"{LtoS(Doujin.characters)}", inline=True)
            embD.add_field(name="Tags", value=f"{LtoS(Doujin.tags)}", inline=False)
            embD.add_field(name="Languages", value=f"{LtoS(Doujin.languages)}", inline=False)
            embD.add_field(name="Artists", value=f"{LtoS(Doujin.artists)}", inline=False)
            embD.add_field(name="Total Pages", value=f"{Doujin.total_pages}", inline=False)
            embD.set_footer(icon_url=Takodachi, text=f"Cultured Tako")
            embD.set_thumbnail(url=f"{Doujin.images[0]}")
            await msg.edit(embed=embD)
            
        option = Option.lower()
        NH = NHentai()
        with open(r"Data\Emoji.json", encoding="utf8") as F:
            JF = F.read()
            Json = json.loads(JF)
            GET = Json["default"]
            MEDIA = GET["Media"]
        embD = discord.Embed(title="Please wait.", description=f"Poyoyo is currently fetching {Code} doujin...", color=0xFF69B4)
        embD.set_footer(icon_url=Takodachi, text=f"Cultured Tako")
        EMSG = await ctx.send(embed=embD)
        if option == "get":
            await get_doujin(EMSG, Code)
        elif option == "open":
            Doujin = NH._get_doujin(str(Code))
            embD = discord.Embed(title=f"{Doujin.title}", description=f"{Doujin.id}", color=0xFF69B4)
            embD.add_field(name="Characters", value=f"{LtoS(Doujin.characters)}", inline=True)
            #embD.add_field(name="Tags", value=f"{LtoS(Doujin.tags)}", inline=False)
            embD.add_field(name="Languages", value=f"{LtoS(Doujin.languages)}", inline=False)
            embD.add_field(name="Artists", value=f"{LtoS(Doujin.artists)}", inline=False)
            embD.set_footer(icon_url=Takodachi, text=f"Cultured Tako")
            embD.set_image(url=f"{Doujin.images[0]}")
            embD.add_field(name="Total Pages", value=f"{Doujin.total_pages}", inline=False)
            Nn = MEDIA["Next"]
            Pp = MEDIA["Prev"]
            embD.add_field(name="Controls", value=f"{Pp} prev, {Nn} next", inline=False)
            await EMSG.edit(embed=embD)
            await EMSG.add_reaction(str(MEDIA["Prev"]))
            await EMSG.add_reaction(str(MEDIA["Next"]))
            with open(r"Data\NHdata.json", "r") as JF:
                Jfile = JF.read()
                JSON = json.loads(Jfile)
                pages = {}
                count = 1
                for i in Doujin.images:
                    pages[count] = i
                    count += 1
                JSON[EMSG.id] = {"pages":pages, "current":1, "channel":ctx.channel.id, "title":f"{Doujin.title}", "code":f"{Doujin.id}"}

            with open(r"Data\NHdata.json", "w") as JF:
                json.dump(JSON, JF, indent=2)
                
    @client.command()
    async def clear(ctx, amount=1):
        amount += 1
        await ctx.channel.purge(limit=amount)

    @client.command()
    async def status(ctx):
        await ctx.channel.send("Konnakiri!!! {0.user} is Online".format(client))

    @client.command()
    async def FAQ(ctx):
        await ctx.channel.send("NO U FAQ")

    @client.command()
    async def info(ctx):
        content = GetContents(r"Data\Info.txt")
        final = ''
        for i in content:
            final += i + "\n"
        await ctx.channel.send(final)

    @client.command()
    async def setafk(ctx, user, *msg):
        rebuild_msg = ""
        for i in msg:
            rebuild_msg += i + " "
        SERVER = ctx.guild.id
        SetAFKmsg(user, rebuild_msg, SERVER)
        update_afk_list(SERVER)
        await ctx.channel.send("AFK msg has been set.")

    @client.command()
    async def choose(ctx, *args):
        selection = []
        remove = ["or"]
        for i in args:
            Filter = i.lower()
            for R in remove:
                if Filter != str(R):
                    selection.append(i)
        result = random.choice(selection)
        await ctx.channel.send(f"i choose {result}")

    @client.command()
    async def culture(ctx, args="random", category="hololive"):
        lewds = [line.strip("\ufeff \n") for line in open(r"Data\LEWDS.txt", encoding="utf8")]
        anime = []
        hololive = []
        block_list = [line.strip("\ufeff \n") for line in open(r"Data\r18block.txt", encoding="utf8")]
        if str(ctx.message.author.id) in block_list or str(ctx.message.author) in block_list:
            InaStop = [line.strip() for line in open(r"Data\Messages\InaStop.txt")]
            choose = random.choice(InaStop)
            TITLE, DESC = choose.split("<split>")
            embedVar = discord.Embed(title=f"{TITLE}", description=f"{DESC}", color=0xff0000)
            embedVar.set_footer(icon_url=Takodachi, text="Security Tako")
            await ctx.channel.send(embed=embedVar)
            return
        else:
            if isinstance(ctx.channel, discord.channel.DMChannel) or ctx.channel.is_nsfw():
                for l in lewds:
                    if "Hololive" in l:
                        hololive.append(l)
                    elif "Anime" in l:
                        anime.append(l)
                cat = category.lower()
                if args == "random":
                    if cat == "hololive":
                        get = random.randint(0, len(hololive))
                        await ctx.channel.send(file=discord.File(hololive[get]))
                    elif cat == "anime":
                        get = random.randint(0, len(anime))
                        await ctx.channel.send(file=discord.File(anime[get]))
                    else:
                        get = random.randint(0, len(lewds))
                        await ctx.channel.send(file=discord.File(lewds[get]))
                elif args == "index":
                    if cat == "hololive":
                        await ctx.channel.send(f"Poyoyo currently has {len(hololive)} Hololive cultured images")
                    elif cat == "anime":
                        await ctx.channel.send(f"Poyoyo currently has {len(anime)} Anime cultured images")
                    else:
                        await ctx.channel.send(f"Poyoyo currently has {len(lewds)} cultured images")

                elif args == "Hololewd":
                    try:
                        open(f"Data\\Hololewd\\{ctx.message.guild.id}.txt")
                    except:
                        mk = open(f"Data\\Hololewd\\{ctx.message.guild.id}.txt", "w")
                        mk.write("")
                        mk.close
                    else:
                        pass
                    
                    cache = f"Data\\Hololewd\\{ctx.message.guild.id}.txt"
                    sent_list = [line.strip() for line in open(cache)]
                    ready = []
                    picF = [".jpg", ".png"]
                    
                    if cat == "hololive" or cat == "hot":
                        memes, titles, Time = AsacocoModule.getLewds("hot")
                        #print(1)
                        for m in memes:
                            load = 0
                            for s in sent_list:
                                if str(m) == str(s):
                                    pass
                                else:
                                    load += 1
                            if load == len(sent_list):
                                ready.append(m)

                    elif cat == "new":
                        memes, titles, Time = AsacocoModule.getLewds("new")
                        #print(2)
                        for m in memes:
                            load = 0
                            for s in sent_list:
                                if str(m) == str(s):
                                    pass
                                else:
                                    load += 1
                            if load == len(sent_list):
                                ready.append(m)
                    #print(ready, memes)
                    
                    run = True
                    while run:
                        select = random.choice(ready)
                        Filt2 = select.decode("utf8")
                        for i in picF:
                            if i in Filt2:
                                getTitle = memes.index(select)
                                sTitle = titles[getTitle]
                                TITLE = sTitle.decode("utf8")
                                TIME = Time[getTitle]
                                print(TITLE)
                                embedVar = discord.Embed(title=f"{TITLE}", url=f"{Filt2}", color=0xFF69B4)
                                embedVar.add_field(name="Posted on", value=f"{TIME}", inline=False)
                                embedVar.set_image(url=Filt2)
                                embedVar.set_footer(text="Powered by Asacoco")
                                await ctx.channel.send(embed=embedVar)
                                save = open(cache, "a")
                                print(select, file=save)
                                save.close
                                run = False
                            else:
                                pass

                else:
                    try:
                        if cat == "hololive":
                            await ctx.channel.send(file=discord.File(hololive[int(args)-1]))
                        elif cat == "anime":
                            await ctx.channel.send(file=discord.File(anime[int(args)-1]))
                        else:
                            await ctx.channel.send(file=discord.File(lewds[int(args)-1]))
                    except:
                        await ctx.channel.send("Sorry unknown argument.")
            else:
                InaWarn = [line.strip() for line in open(r"Data\Messages\InaWarning.txt")]
                choose = random.choice(InaWarn)
                TITLE, DESC = choose.split("<split>")
                embedVar2 = discord.Embed(title=f"{TITLE}", description=f"{DESC}", color=0xFFA500)
                embedVar2.set_footer(icon_url=Takodachi, text="Security Tako")
                await ctx.channel.send(embed=embedVar2)
                #await ctx.channel.send("Sorry this command is for NSFW channel and DM's only. Go get a Bonk!")

    @client.command()
    async def resen(ctx, *args):
        if int(ctx.author.id) != EINZEIG:
            rejectEB = discord.Embed(title="Request denied.", description=f"User: {ctx.author} ID: {ctx.author.id}", color=0x87CEFA)
            rejectEB.add_field(name="Error!", value="You don't have permission to use this command", inline=False)
            rejectEB.set_footer(icon_url=AyamTat, text=f"Security Unit")
            await ctx.channel.send(embed=rejectEB)
            return
        else:
            pass
        def create_puryufa():
            getID = ctx.channel.id
            getAuth = ctx.author.id
            os.system(f"python Puryufa.py {getID} {getAuth}")
        if args[0] == "deploy":
            if args[1] == "Puryufa" or "プリューファ" or "Prüfer" or "Puryūfa":
                summonEXM = Thread(target=create_puryufa)
                summonEXM.start()
        if args[0] == "shutdown":
            await ctx.send("shutdown sequence will start after 3secs.")
            time.sleep(3)
            await ctx.send("Bot shutting down. Jaa~ Otsunakiri!")
            sys.exit()
            

    @client.command()
    async def nextmeme(ctx):
        try:
            open(f"Data\\Holomemes\\{ctx.message.guild.id}.txt")
        except:
            mk = open(f"Data\\Holomemes\\{ctx.message.guild.id}.txt", "w")
            mk.write("")
            mk.close
        else:
            pass
        cache = f"Data\\Holomemes\\{ctx.message.guild.id}.txt"
        
        sent_list = [line.strip() for line in open(cache)]
        memes, titles, time = AsacocoModule.getMemes(50)
        ready = []
        picF = [".jpg", ".png"]
        for m in memes:
            load = 0
            for s in sent_list:
                if str(m) == str(s):
                    pass
                else:
                    load += 1
            if load == len(sent_list):
                ready.append(m)
        run = True
        while run:
            select = random.choice(ready)
            Filt2 = select.decode("utf8")
            for i in picF:
                if i in Filt2:
                    getTitle = memes.index(select)
                    sTitle = titles[getTitle]
                    TITLE = sTitle.decode("utf8")
                    TIME = time[getTitle]
                    print(TITLE)
                    embedVar = discord.Embed(title=f"{TITLE}", url=f"{Filt2}", color=0xfffafa)
                    embedVar.add_field(name="Posted on", value=f"{TIME}", inline=False)
                    embedVar.set_image(url=Filt2)
                    embedVar.set_footer(text="Powered by Asacoco")
                    await ctx.channel.send(embed=embedVar)
                    save = open(cache, "a")
                    print(select, file=save)
                    save.close
                    run = False
                else:
                    pass
    @client.command(pass_context=True)
    async def changenick(ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')
    
    @client.command()
    async def getmembers(ctx, *args):
        members = ctx.server.member
        print(members)

    @client.event
    async def on_raw_reaction_add(reaction):
        with open(r"Data\Emoji.json", encoding="utf8") as F:
            JF = F.read()
            Json = json.loads(JF)
            GET = Json["default"]
            MEDIA = GET["Media"]
            Nn = MEDIA["Next"]
            Pp = MEDIA["Prev"]
        def SetLink(lib, page):
            Title = lib["title"]
            code = lib["code"]
            pagelinks = lib["pages"]
            Link = pagelinks[f"{page}"]
            embD = discord.Embed(title=f"{Title}", description=f"{code}", color=0xFF69B4)
            embD.set_footer(icon_url=Takodachi, text="Cultured Tako")
            embD.set_image(url=Link)
            embD.add_field(name="Pages", value=f"{page} out of {len(pagelinks)}", inline=False)
            embD.add_field(name="Controls", value=f"{Pp} prev, {Nn} next", inline=False)
            return embD

        if reaction.member == client.user:
            return
        with open(r"Data\NHdata.json") as F:
            JF = F.read()
            JSON = json.loads(JF)
        cache = []
        for i in JSON:
            cache.append(int(i))
        if int(reaction.message_id) in cache:
            data = JSON[f"{reaction.message_id}"]
            if reaction.channel_id == data["channel"]:
                channel = client.get_channel(reaction.channel_id)
                msg = await channel.fetch_message(reaction.message_id)
                pages = []
                for i in data["pages"]:
                    pages.append(i)
                if str(reaction.emoji) == MEDIA["Prev"]:
                    page = data["current"]
                    if str(page) != str(pages[0]):
                        page -= 1
                        emm = SetLink(data, page)
                        await msg.edit(embed=emm)
                        data["current"] = page
                elif str(reaction.emoji) == MEDIA["Next"]:
                    page = data["current"]
                    if str(page) != str(pages[len(pages)-1]):
                        page += 1
                        emm = SetLink(data, page)
                        await msg.edit(embed=emm)
                        data["current"] = page
                with open(r"Data\NHdata.json", "w") as F:
                    json.dump(JSON, F, indent=2)

    @client.event
    async def on_raw_reaction_remove(reaction):
        with open(r"Data\Emoji.json", encoding="utf8") as F:
            JF = F.read()
            Json = json.loads(JF)
            GET = Json["default"]
            MEDIA = GET["Media"]
            Nn = MEDIA["Next"]
            Pp = MEDIA["Prev"]
        def SetLink(lib, page):
            Title = lib["title"]
            code = lib["code"]
            pagelinks = lib["pages"]
            Link = pagelinks[f"{page}"]
            embD = discord.Embed(title=f"{Title}", description=f"{code}", color=0xFF69B4)
            embD.set_footer(icon_url=Takodachi, text="Cultured Tako")
            embD.set_image(url=Link)
            embD.add_field(name="Pages", value=f"{page} out of {len(pagelinks)}", inline=False)
            embD.add_field(name="Controls", value=f"{Pp} prev, {Nn} next", inline=False)
            return embD

        if reaction.member == client.user:
            return
        with open(r"Data\NHdata.json") as F:
            JF = F.read()
            JSON = json.loads(JF)
        cache = []
        for i in JSON:
            cache.append(int(i))
        if int(reaction.message_id) in cache:
            data = JSON[f"{reaction.message_id}"]
            if reaction.channel_id == data["channel"]:
                channel = client.get_channel(reaction.channel_id)
                msg = await channel.fetch_message(reaction.message_id)
                pages = []
                for i in data["pages"]:
                    pages.append(i)
                if str(reaction.emoji) == MEDIA["Prev"]:
                    page = data["current"]
                    if str(page) != str(pages[0]):
                        page -= 1
                        emm = SetLink(data, page)
                        await msg.edit(embed=emm)
                        data["current"] = page
                elif str(reaction.emoji) == MEDIA["Next"]:
                    page = data["current"]
                    if str(page) != str(pages[len(pages)-1]):
                        page += 1
                        emm = SetLink(data, page)
                        await msg.edit(embed=emm)
                        data["current"] = page
                with open(r"Data\NHdata.json", "w") as F:
                    json.dump(JSON, F, indent=2)
        
    @client.event
    async def on_message(message):
        global DPGS
        global CHANNEL
        global RecentChat
        global RecentChannel
        if message.author == client.user:
            if message.author != RecentChat or message.channel != RecentChannel:
                print(f"+++++ Poyoyo Reply on [{message.channel}]")
            print(f"{message.content}")
            RecentChat = message.author
            return

        with open(r"Data\Emoji.json", encoding="utf8") as F:
            JF = F.read()
            Json = json.loads(JF)
            GET = Json["default"]
            MEDIA = GET["Media"]
            LETTER = GET["Alphabets"]

        channel = message.channel
        msg = message.content
        writer = message.author
        origin = message.channel
        try:
            serverID = message.guild.id
        except:
            pass
        if writer != RecentChat or message.channel != RecentChannel:
            print("======{} on [{}]".format(writer, origin))
        print(f"{msg}")
        RecentChat = writer
        RecentChannel = origin
        update_afk_list(serverID)

        for word in SharkTrigger:
            if msg.startswith(word):
                if len(str(msg)) == len(str(word)):
                    await channel.send(GetGuraResponse())
        #Auto Respond
        for s in afk_user:
            if s in msg:
                update_afk_list(serverID)
                AFK_msg = GetAFKmsg(s, serverID)
                fil= AFK_msg.replace("//u/", f"<@!{s}>")
                await channel.send(fil)

        #Notifications
        async def React(message):
            MM = ["KAITO", "YO", "NE", "KYAH", "HENTAI", "KUSA"]
            L = random.choice(MM)
            for i in L:
                await message.add_reaction(LETTER[i])
        lowmsg = msg.lower()
        for i in NotifTriggers:
            if i in lowmsg:
                replaceID = Convert(msg)
                notification.notify(
                    title=f'Notice: {writer} mentioned you',
                    message=f'{replaceID}',
                    app_name=f'Raphael',
                    app_icon='Ojou.' + ('ico' if platform == 'win' else 'png')
                )
                beep(sound="coin")
                await React(message)

        #MinGAe
        if int(writer.id) == 726477301658812568:
            select = ["YES"]
            for i in range(29):
                select.append("NO")
            decide = random.choice(select)
            #print(decide)
            if decide == "YES":
                react = ["GAE", "GAY", "IMGAE", "IMGAY"]
                send_react = random.choice(react)
                for i in send_react:
                    await message.add_reaction(LETTER[i])
                

        #RickRoll
        Rick = [line.strip() for line in open(r"Data\NeverGiveup.txt")]
        Roll = []
        for i in Rick:
            i = i.lower()
            Roll.append(i)
        if lowmsg in Roll:
            get = Roll.index(lowmsg)
            Next = get+1
            await channel.send(Rick[Next])
            if Next == 30:
                await channel.send(Rick[Next+1])

        trig = TRIGGERED(msg)
        if trig:
            await channel.send(file=trig)
            
        await client.process_commands(message)

if __name__ == "__main__":
    print("blocked")
    a = input("Proceed starting main program? ")
    if a == "y":
        os.system("main.pyw")
