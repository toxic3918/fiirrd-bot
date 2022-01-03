import discord
from discord.ext import commands
from datetime import datetime
import random
import discord
from discord.ext import commands
from datetime import datetime
import time
import asyncio
from PIL import Image
from io import BytesIO
import os
import discord
from discord import user
from discord.ext import commands
from datetime import datetime
import time
import random
import json
import os




class FunCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def luckynumber(self, ctx):
        luckynumber = random.randint(0, 100)

        embed = discord.Embed(title="What is your Lucky Number?", description=f"Your **Lucky Number** is **{luckynumber}**\nDon't forget to check your **Lucky Number** again", timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command(aliases=['cr'])
    async def coolrate(self, ctx):
        coolrate = random.randint(0, 100)

        embed = discord.Embed(title="What is your Cool Rate?", description=f"Your **Cool Rate** is {coolrate}**%\nDon't forget to check Your**Cool Rate** again!")







    @commands.command()
    async def wanted(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open('wanted.jpg')
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((257, 257))

        wanted.paste(pfp, (98, 200))

        wanted.save("profile.png")

        await ctx.send(file = discord.File("profile.png"))

def setup(client):
    client.add_cog(FunCommands(client))