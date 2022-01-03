import discord
from discord.ext import commands


class ChatCommands(commands.Cog):
    def __init__(self, client):
        self.client = client



@commands.command()
async def ping(self, ctx):
    await ctx.reply("Pong!")


    @commands.command()
    async def hello(self, ctx):
        await ctx.reply(f"Hi {ctx.author.mention}! How are you?")


    @commands.commands()
    async def hi(self, ctx):
        await ctx.reply(f"Hello {ctx.author.mention}! How are yu doing?")


    @commands.command()
    async def fine(self, ctx):
        pass


    @commands.command()
    async def bad(self, ctx):
        pass

    @commands.command()
    async def invite(self, ctx):

        embed = discord.Embed(title="Invite The Bot", description="Invite by clicking here  -->  [Click To Invite](https://discord.com/api/oauth2/authorize?client_id=914018241112842240&permissions=8&scope=bot)", timestamp=datetime.utcnow(), color=discord.Color.purple())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ChatCommands(client))