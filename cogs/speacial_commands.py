import discord
from discord.ext import commands
from datetime import datetime
from PIL import Image
from io import BytesIO
import discord
from discord import client
from discord.ext import commands
from datetime import datetime
import time


class SpecialCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command()
    async def afk(self, ctx, *, afk_arg="No **AFK** message was given!"):
        
        embed = discord.Embed(title="", description=f"{ctx.author.mention} has gone **AFK**\nAFK Message: **{afk_arg}**", color=ctx.author.color)
        await ctx.send(embed=embed)

    
    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def addrole(self, ctx, member: discord.Member, role: discord.Role):
        await member.add_roles(role)

        embed = discord.Embed(title=f"{member} You have been Given a **Role**!", description=f"hey {member.mention}, You have given a role called: **{role.name}**", timestamp=datetime.now(), color=ctx.author.color)

        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def removerole(self, ctx, member: discord.Member, role: discord.Role):
        await member.remove_roles(role)

        embed = discord.Embed(title=f"{member} You have been Given a **Role**!", description=f"hey {member.mention}, Your role has been removed called: **{role.name}**", timestamp=datetime.now(), color=ctx.author.color)

        await ctx.send(embed=embed)

    @commands.command()
    async def announcement(self, ctx, *, announcement):
        await ctx.send(f"{announcement}")


    @commands.command(aliases=['mc'])
    async def membercount(self, ctx):
        embed = discord.Embed(title="Members", description=f"{ctx.guild.member_count}", timestamp=datetime.utcnow(), color=discord.Color.blue())
        await ctx.send(embed=embed)

    @commands.command()
    async def rip(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open('rip.jpg')
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((179, 125))

        wanted.paste(pfp, (228, 206))

        wanted.save("profile.jpg")

        await ctx.send(file = discord.File("profile.jpg"))


    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        if user == None:
            user = ctx.author

        wanted = Image.open('slap.jpg')
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)

        pfp = pfp.resize((179, 125))

        wanted.paste(pfp, (228, 206))

        wanted.save("slaplol.png")

        await ctx.send(file = discord.File("slaplol.png"))


    @commands.command()
    async def say(self, ctx, *, say="No **say** command was told!"):
        await ctx.send(f"{say}")
        await ctx.message.delete()


    @commands.command()
    async def poll(self, ctx):
        thumbsup = "👍"
        thumbsdown = "👎"

        embed = discord.Embed(title="Poll Time!", description="👍 You like it - 👎 You don't like it", timestamp=datetime.utcnow(), color=ctx.author.color)

        reaction = await ctx.send(embed=embed)

        await reaction.add_reaction(emoji=thumbsup)
        await reaction.add_reaction(emoji=thumbsdown)










    
    @commands.command()
    async def add(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Calculation (Addition)", description=num1+num2, timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command()
    async def sub(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Calculation (Substraction)", description=num1-num2, timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command()
    async def mul(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Calculation (Multiplication)", description=num1*num2, timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)


    @commands.command()
    async def div(self, ctx, num1: int, num2: int):
        embed = discord.Embed(title="Calculation (Division)", description=num1/num2, timestamp=datetime.utcnow(), color=ctx.author.color)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):

        embed = discord.Embed(title="Invite The Bot", description="Invite by clicking here  -->  [Click To Invite](https://discord.com/api/oauth2/authorize?client_id=914018241112842240&permissions=8&scope=bot)", timestamp=datetime.utcnow(), color=discord.Color.purple())
        await ctx.send(embed=embed)


    @commands.command()
    async def pollwrite(self, ctx, *, poll="No **poll** was given!"):
        thumbsup = "👍"
        thumbsdown = "👎"

        embed = discord.Embed(title="Poll Time!", description=f"{poll}", timestamp=datetime.utcnow(), color=ctx.author.color)

        reaction = await ctx.send(embed=embed)

        await reaction.add_reaction(emoji=thumbsup)
        await reaction.add_reaction(emoji=thumbsdown)


    # view futures maintenance
        @commands.command()
        async def earlymaintenance(self, ctx):
            await ctx.send("The maintenance is now going on!")


def setup(client):
    client.add_cog(SpecialCommands(client))