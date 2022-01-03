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











@client.event
async def on_member_join(member):
    embed = discord.Embed(title="Welcome to the server", description=f"Welcome! {member.mention} to the server, Enjoy your stay here!", timestamp=datetime.utcnow(), color=discord.Color.random())

    await member.send(embed=embed)