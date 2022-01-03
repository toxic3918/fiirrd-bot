from collections import UserDict, UserList, UserString
from datetime import datetime
from discord import FFmpegPCMAudio
from discord import player
from discord import guild
import os
from discord.ext import commands
import random
import discord.ext.commands.bot
import discord
from discord_components import *
import aiohttp
from PIL import Image
from io import BytesIO
import asyncio
from dotenv import load_dotenv
import requests
import json
import bal
import youtube_dl
import textwrap
import urllib
import aiohttp
import argparse
import json
from os import listdir
import datetime
from discord_buttons_plugin import *
import discord
from discord import user
from discord.ext import commands
from datetime import datetime
import time
import random
import json
import os
from webserver import keep_alive
from discord.embeds import Embed
from discord import colour
import aiofiles
import discord
from discord.ext import commands
import math
import aiosqlite
import asyncio
import discord
from discord.ext import commands
import discord
import random
import asyncio
import string
from discord.ext import commands
import discord
from discord.ext import commands, tasks
import youtube_dl
import asyncio
from random import choice
import discord
from discord.ext import commands
from discord.utils import get
from discord import Embed, Color
import DiscordUtils
import os
from discord.ext.commands import has_permissions, MissingPermissions
import json
import discord
from discord.ext import commands
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import (
    ComponentContext,
    create_actionrow,
    create_button,
)






load_dotenv()
prefixes = '!', ">", "@firred bot#0756", "f!", "F!", "p.", "P."

client = commands.Bot(command_prefix = prefixes, intents=discord.Intents.all(), case_insensitive=True)
buttons = ButtonsClient(client)
slash = SlashCommand(client)

async def ch_pr():
    await client.wait_until_ready()

    statuses = ['p.help', f'On {len(client.guilds)} servers']

    while not client.is_closed():
        status = random.choice(statuses)
        await client.change_presence(status=discord.Status.idle, activity=discord.Game(name=status))
        # await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=status))
        await asyncio.sleep(5)

client.loop.create_task(ch_pr())
@client.command()
async def ticket(ctx, *, reason = None):
      guildid = ctx.guild.id
      guild = ctx.guild
      user = ctx.author
      amount2 = 1
      await ctx.channel.purge(limit=amount2)
      channel = await guild.create_text_channel(f'Ticket {user}')
      await channel.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
      perms = channel.overwrites_for(user)
      await channel.set_permissions(user, view_channel=not perms.view_channel)
      await channel.set_permissions(user, read_message_history=not perms.read_message_history)
      await channel.set_permissions(user, send_messages=not perms.send_messages)
      await channel.send(f"{user.mention}")
      supem = discord.Embed(title=f"{user} hi, wait for some time mods will help you.", description= "", color=0x00ff00)
      supem.add_field(name="wait", value=f"``{reason}``")
      supem.set_footer(text=f"thx for using me ")
      await channel.send(embed=supem)  



@client.event
async def on_member_remove(member):
    embed = discord.Embed(title="Goodbye from the server", description=f"Goodbye! {member.mention} from the server!", timestamp=datetime.utcnow(), color=discord.Color.random())

    await member.send(embed=embed)














     

@client.command(aliases=["approve"])
@commands.has_role(886557599636537365)
async def up(ctx):
    overwrites = {
        ctx.guild.me: discord.PermissionOverwrite(view_channel=True),
        ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        ticket_mod_role: discord.PermissionOverwrite(view_channel=None),
        management_role: discord.PermissionOverwrite(view_channel=True),
    }
    await ctx.channel.edit(overwrites=overwrites)

    await ctx.channel.send(
        "Ticket Approved!\nYour ticket has been approved and has been transferred through to the Management Team. They will assist you further with your enquiry."
    )




@client.event
async def on_member_join(member):
    with open('users.json', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


@client.event
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)

        await update_data(users, message.author)
        await add_experience(users, message.author, 5)
        await level_up(users, message.author, message)

        with open('users.json', 'w') as f:
            json.dump(users, f)

    await client.process_commands(message)


async def update_data(users, user):
    if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 1


async def add_experience(users, user, exp):
    users[f'{user.id}']['experience'] += exp


async def level_up(users, user, message):
    with open('levels.json', 'r') as g:
        levels = json.load(g)
    experience = users[f'{user.id}']['experience']
    lvl_start = users[f'{user.id}']['level']
    lvl_end = int(experience ** (1 / 4))
    if lvl_start < lvl_end:
        await message.channel.send(f'{user.mention} has leveled up to level {lvl_end}')
        users[f'{user.id}']['level'] = lvl_end

@client.command()
async def level(ctx, member: discord.Member = None):
    if not member:
        id = ctx.message.author.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'You are at level {lvl}!')
    else:
        id = member.id
        with open('users.json', 'r') as f:
            users = json.load(f)
        lvl = users[str(id)]['level']
        await ctx.send(f'{member} is at level {lvl}!')






@client.command()
@commands.has_role(886557599636537365)
async def close(ctx):
    await ctx.channel.delete()

   


@client.command(aliases=["bal"])
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    msg = discord.Embed(Title='dfwd', type='rich', color=discord.Color.green(), timestamp=ctx.message.created_at)
    msg.add_field(name=f"{ctx.author}'s balance :money_with_using:", value=wallet_amt, inline=False)
    msg.add_field(name=f"{ctx.author}'s Bank:bank:", value=bank_amt, inline=False)
    await ctx.send(embed=msg)



@client.command()
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author

    users = await get_bank_data()

    earnings = random.randrange(1000)

    await ctx.send(f'{ctx.author.mention} Got {earnings} coins!!')

    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json",'w') as f:
            json.dump(users,f)


async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return  False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open("mainbank.json", "r") as f:
      json.dump(users, f)
    return True

async def get_bank_data():
    with open("mainbank.json", "r") as f:
      users = json.load(f)
    return users


@client.command()
async def bag(ctx):
     await open_account(ctx.author)
     user = ctx.author
     users = await get_bank_data()

     try:
         bag = users[str(user.id)]["bag"]
     except:
         bag = []


     em = discord.Embed(title = "Bag")
     for item in bag:
         name = item["item"]
         amount = item["amount"]

         em.add_field(name = name, value = amount)    

     await ctx.send(embed = em)


async def buy_this(user,item_name,amount):
     item_name = item_name.lower()
     name_ = None
     for item in mainshop:
         name = item["name"].lower()
         if name == item_name:
             name_ = name
             price = item["price"]
             break

     if name_ == None:
         return [False,1]

     cost = price*amount

     users = await get_bank_data()

     bal = await update_bank(user)

     if bal[0]<cost:
         return [False,2]


     try:
         index = 0
         t = None
         for thing in users[str(user.id)]["bag"]:
             n = thing["item"]
             if n == item_name:
                 old_amt = thing["amount"]
                 new_amt = old_amt + amount
                 users[str(user.id)]["bag"][index]["amount"] = new_amt
                 t = 1
                 break
             index+=1 
         if t == None:
             obj = {"item":item_name , "amount" : amount}
             users[str(user.id)]["bag"].append(obj)
     except:
         obj = {"item":item_name , "amount" : amount}
         users[str(user.id)]["bag"] = [obj]        

     with open("mainbank.json","w") as f:
         json.dump(users,f)

     await update_bank(user, cost*-1, "wallet")

     return [True,"Worked"]
    


@client.command()
@commands.guild_only()
@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
async def slots(self, ctx, bet: int):
        if 1 > bet:
            return await ctx.send("Give some money! ;w;")
        query = "SELECT * FROM userbal WHERE userid=$1;"
        row = await self.bot.db.fetchrow(query, ctx.author.id)
        if not row:
            return await ctx.send("You don't have an account!")
        losshearts = ["🖤", "💔"]
        doublehearts = ["❤️", "💚", "💛", "🧡", "💜", "💙"]
        triplehearts = ["💗", "💖"]
        jackpothearts = ["💘"]
        hearts = {}
        heartlist = ["❤️", "🖤", "💗", "💚", "💖", "💛", "💔", "🧡", "💜", "💙", "💘"]
        for x in range(1, 10):
            hearts[f"heart{x}"] = random.choice(heartlist)
        msg = await ctx.send(
            f"```\n{hearts['heart1']}{hearts['heart2']}{hearts['heart3']}\n{hearts['heart4']}{hearts['heart5']}{hearts['heart6']}\n{hearts['heart7']}{hearts['heart8']}{hearts['heart9']}\n```"
        )
        if hearts["heart4"] == hearts["heart5"] == hearts["heart6"]:
            if hearts["heart4"] in losshearts:
                multiplier = 0
            if hearts["heart4"] in doublehearts:
                multiplier = 2
            if hearts["heart4"] in triplehearts:
                multiplier = 3
            if hearts["heart4"] in jackpothearts:
                multiplier = 10
        else:
            multiplier = 0
        msg = await ctx.channel.fetch_message(msg.id)
        await msg.edit(
            content=f"{msg.content}\nAnd you got a multiplier of {multiplier}!"
        )
        betresult = int(bet * multiplier)
        if multiplier == 0:
            betresult = int(-bet)
        betresult = row["money"] + betresult
        query = "UPDATE userbal SET money = $1 WHERE userid = $2;"
        altrow = await self.bot.db.fetchrow(query, betresult, ctx.author.id)


@client.command()
async def buy(ctx,item,amount = 1):
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
         if res[1]==1:
             await ctx.send("That Object isn't there!")
             return
         if res[1]==2:
             await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
             return


    await ctx.send(f"You just bought {amount} {item}")


    
@client.command()
async def shop(ctx):
     em = discord.Embed(title = "Shop")

     for item in mainshop:
         name = item["name"]
         price = item["price"]
         desc = item["description"]
         em.add_field(name = name, value = f"${price} | {desc}")

     await ctx.send(embed = em)





mainshop = [{"name":"Watch","price":100,"description":"Time"},
             {"name":"Laptop","price":1000,"description":"Work"},
             {"name":"PC","price":10000,"description":"Gaming"},
             {"name":"Ferrari","price":99999,"description":"Sports Car"}]

@client.command()
async def withdraw(ctx, amount=0):
    users = await get_bank_data()
    user = ctx.author
    if amount > 0:
      users[str(user.id)]['wallet'] += amount
      users[str(user.id)]['bank'] -= amount

      with open("mainbank.json", "w") as f:
        json.dump(users, f)

      await ctx.send(f"You have withdraw {amount} coins!")

    elif amount < 0:
      await ctx.send(f"You can't withdraw a negative amount of coins stupid!")

    elif amount == 0:
      await ctx.send(f"You can't withdraw 0 coins stupid!")


@client.command()
async def dep(ctx, amount=0):
    users = await get_bank_data()
    user = ctx.author
    if amount > 0:
      users[str(user.id)]['wallet'] -= amount
      users[str(user.id)]['bank'] += amount

      with open("mainbank.json", "w") as f:
        json.dump(users, f)

      await ctx.send(f"You have deposited {amount} coins!")

    elif amount < 0:
      await ctx.send(f"You can't deposit a negative amount of coins stupid!")

    elif amount == 0:
      await ctx.send(f"You can't deposit 0 coins stupid!")




@client.command(breif = "stone, paper, scissor game")
async def rps(ctx):
    async with ctx.typing():
        reactions = ['🪨','🧻','✂️']
        player = str(ctx.message.author)
        await ctx.send(f"starting the game stone paper scissor...")
        emd = discord.Embed(title = f"Round 1", description = f"CHOOSE \n\n\t🪨\t:\tfor rock\n\n\t🧻\t:\tfor paper\n\n\t✂️\t:\tfor scissor")
        msg = await ctx.send(embed=emd)
        for i in range(0,3):
            await msg.add_reaction(emoji=reactions[i])

    def check(reaction,user):
        return str(user) == player

    reaction,user = await client.wait_for("reaction_add",timeout = None,check = check)
    async with ctx.typing():
        if(str(user) == player):
            r = random.randint(0,2)
            playerInput = reactions.index(reaction.emoji)
            result = ""
            data = f"I choise {reactions[r]}\t\tYou Chose { reactions[playerInput]}"
            if(r == playerInput):
              result = "Draw"
            elif(r==0 and playerInput==2):
              result = "You lose"
            elif(r==2 and playerInput==0):
              result = "You won"
            elif(r > playerInput):
              result = "You lose"
            else:
              result = "You won"
            eb = discord.Embed(title = result , desciption = data)
            await reaction.message.channel.send(embed= eb)  

@client.command(brief = "fox pics")
async def fox(ctx):
    async with ctx.typing():
        try:
            data = requests.get("https://randomfox.ca/floof")
        except:
              await ctx.send("Network error...")
              pass
        jdata = json.loads(data.text)
        emd = discord.Embed(title='Floof')
        emd.set_image(url = jdata["image"])
        await ctx.send(embed = emd)

@client.command(brief = "cat pics")
async def cat(ctx):
    async with ctx.typing():
        try:
            data = requests.get("https://aws.random.cat/meow")
        except:
              await ctx.send("Network error...")
              pass
        jdata = json.loads(data.text)
        emd = discord.Embed(title='meow')
        emd.set_image(url = jdata["file"])
        await ctx.send(embed = emd)

@client.command(brief = "dog pics")
async def dog(ctx):
    async with ctx.typing():
        try:
            data = requests.get("https://random.dog/woof.json")
        except:
              await ctx.send("Network error...")
              pass
        jdata = json.loads(data.text)
        emd = discord.Embed(title='dog')
        emd.set_image(url = jdata["url"])
        await ctx.send(embed = emd)

@client.command(brief ="Pokemon")
async def pokemon(ctx):
  async with ctx.typing():
      try:
          data = requests.get(f"https://pokeapi.co/api/v2/pokemon/{random.randrange(0,1048)}")
      except:
          await ctx.send("Network error...")
          pass
      jdata = json.loads(data.text)
      emd = discord.Embed(title= 'pokemon', description =f'{jdata["species"]["name"]}')
      emd.set_image(url = jdata["sprites"]["front_default"])
      await ctx.send(embed = emd)


@client.command()
async def reactionrole(ctx, emoji, role: discord.role,*,message):

    emb = discord.Embed(discription=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reaction.json')as json_file: 
      data = json.load(json.file)

      new_react_role = {
        'role_name':role.name,
        'role_id':role.id,
        'emoji':emoji,
        'message_is':msg.id
      }

      data.apend(new_react_role)

    with open('reaction.json','w') as j:
      json.dump(data,j,indent=4)
      
@client.command()
async def button(ctx):
    await ctx.send(type=InteractionType.ChannelMessageWithSource, content="Message Here", components=[Button(style=ButtonStyle.URL, label="Example Invite Button", url="https://dsc.gg/firrd-bot"), Button(style=ButtonStyle.blue, label="click here to invite", custom_id="button")])





@client.event
async def on_ready():
    print(f"{client.user} is Online on Discord")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    reponses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(reponses)}')
@client.command(aliases=['sharyi'])
async def _sharyi(ctx):
    reponses = [
                "Aahat si koi aaye to lagta hai ki tum ho Saya sa   koi lehraye to lagta hai ki tum ho Ab tumhi batao  tum kya kisi bhoot se kam ho?",

                "jailar :- Suna Hai Tum Shayar Ho Kuch Sunao Yaar Qaidi:- Gum-E-Ulfat Mein Jo Zindagi Kati Hai Hamari Jis Din Jamanat Huyi Hamari Us Din Zindagi Khatam Tumhari…."
                "Chandni raat sahil ko diwana bana deti hai… shamma parwane ko jala deti hai.. Ishaq aisi chiiz hai…jo achcho achcho ko roola deti hai…!"
                "Din hua hai to raat bhi hogi,"
                "Ek Pehchan Hazaron Dost Bana Deti Hai..Ek Muskaan Hazaron Ghum Bhula Deti Hai.Ek Muskaan Hazaron Ghum Bhula Deti Hai.Ek Muskaan Hazaron Ghum Bhula Deti Hai.Ek Muskaan Hazaron Ghum Bhula Deti Hai"
                  ]
    await ctx.send(f'\nSharyi: {random.choice(reponses)}')
@client.command()
async def serverinfo(ctx):
    name = str(ctx.guild.name)

    server_name = str(ctx.guild.name)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Server Information",
        description="",
        color=discord.Color.random()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Server Name", value=server_name, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Channels: ", value=len(
        ctx.message.guild.channels), inline=True)
    embed.add_field(name="Country", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name="Requested By: ", value=str(
        ctx.message.author.mention), inline=False)

    await ctx.send(embed=embed)
@client.command()
async def hack(ctx, member : discord.Member):

  random_password = ['36b29c', 'kt764a', '45cvv76', 'fh90;ll', 'gda889', 'kla789', 'kkk89q', 'ff89f52', '95632lrt']

  await ctx.send(f"Hacking Satrted on {member}")
  await ctx.send(f"Hacking Username and Password of {member}")
  await asyncio.sleep(4)
  await ctx.send(f"Hacked!\nUsername - ``{member}\nPassword - **{random.choice(random_password)}**")
  await asyncio.sleep(4)
  await ctx.send("Hacking Completed 20%")
  await asyncio.sleep(3)
  await ctx.send("Hacking Completed 30%")
  await asyncio.sleep(3)
  await ctx.send("Hacking Completed 50%")
  await asyncio.sleep(3)
  await ctx.send("Hacking Epic Games and Steam Account")
  await asyncio.sleep(2)
  await ctx.send("Hacking Epic Games and Steam Account Completed Successfully")
  await asyncio.sleep(3)
  await ctx.send("Hacking Completed 80%")
  await asyncio.sleep(3)
  await ctx.send("Hacking Completed 90%")
  await asyncio.sleep(4)
  await ctx.send(f"A **Dangerous Hacking** Completed on **{member}**\nDon't mind this was a really **Fake Hack**")
@client.command(name="whois")
async def whois(ctx, user: discord.Member = None):

    if user == None:
        user = ctx.author

    rlist = []
    for role in user.roles:
        if role.name != "VERIFY ROLE":
            rlist.append(role.mention)

    b = ", ".join(rlist)

    embed = discord.Embed(colour=user.color, timestamp=datetime.now())

    embed.set_author(name=f"User Info - {user}"),
    embed.set_thumbnail(url=user.avatar_url),

    embed.add_field(name='ID:', value=user.id, inline=False)
    embed.add_field(name='Name:', value=user.display_name, inline=False)

    embed.add_field(name='Created at:', value=user.created_at, inline=False)
    embed.add_field(name='Joined at:', value=user.joined_at, inline=False)

    embed.add_field(name='Bot?', value=user.bot, inline=False)

    embed.add_field(name=f'Roles:({len(rlist)})',
                    value=''.join([b]), inline=False)
    embed.add_field(name='Top Role:',
                    value=user.top_role.mention, inline=False)

    await ctx.send(embed=embed)



queue=[]
status = '18 Naked Cowboys'




@client.command(name='hello',help='This command returns a random the welcome message!')
async def hello(ctx):
    responses = ['***grumble*** Why you wake me up?!','Penis']
    await ctx.send(choice(responses))

    youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)
        
@client.command(name='join', help='This command makes the bot join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("You are not connected to a voice channel")
        return
    
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()

@client.command(name='queue', help='This command adds a song to the queue')
async def queue_(ctx, url):
    global queue

    queue.append(url)
    await ctx.send(f'`{url}` added to queue!')

@client.command(name='remove', help='This command removes an item from the list')
async def remove(ctx, number):
    global queue

    try:
        del(queue[int(number)])
        await ctx.send(f'Your queue is now `{queue}!`')
    
    except:
        await ctx.send('Your queue is either **empty** or the index is **out of range**')
        
@client.command(name='play', help='This command plays songs')
async def play(ctx, *, search_url):
    global queue
    queue.append(search_url)
    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        player = await YTDLSource.from_url(queue[0], loop=client.loop)
        voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)

    await ctx.send('**Now playing:** {}'.format(player.title))
    del(queue[0])

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.pause()

@client.command(name='resume', help='This command resumes the song!')
async def resume(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.resume()

@client.command(name='view', help='This command shows the queue')
async def view(ctx):
    await ctx.send(f'Your queue is now `{queue}!`')

@client.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@client.command(name='stop', help='This command stops the song!')
async def stop(ctx):
    server = ctx.message.guild
    voice_channel = server.voice_client

    voice_channel.stop()


keep_alive()
client.run('OTE0MDE4MjQxMTEyODQyMjQw.YaG70g.LJtDz-L1-CaqjPwQihIhUec3Ue4')