from datetime import datetime
import time
import discord
import asyncio
from discord.ext import commands
import os
import psutil

bot = commands.Bot(command_prefix='!')

async def background_task():
        await bot.wait_until_ready()
        while True:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="CPU: " + str(psutil.cpu_percent(interval=0.5)) + "% RAM:" + str(psutil.virtual_memory().percent) + "%"))
            await asyncio.sleep(10) #every 10 seconds 

@bot.event
async def on_ready():
        print("Now watching your CPU & ram usage...")

bot.loop.create_task(background_task())

bot.run('BOTTOKEN')
