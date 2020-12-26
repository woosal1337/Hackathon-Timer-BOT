import random
from discord.ext import commands, tasks
import time
from time import gmtime, strftime, localtime, timezone
from datetime import datetime
import pytz

f = open("token.0", "r")
token = f.read()
f.close()

bot = commands.Bot(command_prefix="#")

channel = bot.get_channel(746850985510699092)


@bot.event
async def on_ready():
    channel = bot.get_channel(746850985510699092)
    country_time_zone = pytz.timezone('Turkey')

    previousHour = ""

    while True:
        country_time = datetime.now(country_time_zone)
        currentHour = country_time.strftime("%H:%M:%S").split(":")[0]
        if previousHour != currentHour:
            await channel.send("Hackathon'un bitmesine son {0} saat :hourglass: :hourglass_flowing_sand:".format(20 - int(currentHour)))

            previousHour = currentHour


@bot.event
async def on_message(message):
    pass


bot.run(token)
