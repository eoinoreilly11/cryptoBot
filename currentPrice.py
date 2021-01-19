import requests
import time
import discord
from discord.ext import commands
import re

client = commands.Bot(command_prefix =  '!')

token = 'BOT_TOKEN'

@client.event
async def on_ready():
    print("Bot 2 Ready")


@client.command(pass_context=True)
async def bit(ctx):

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
    content = requests.get(url).text
    data = str(re.findall(r"[-+]?\d*\.\d+|\d+", content))
    length = len(data)
    bitc = data[2:length-2]

    embed = discord.Embed(
        title = 'BITCOIN = €' + bitc,
        color=discord.Color.gold()
        )

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ether(ctx):

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
    content = requests.get(url).text
    data = str(re.findall(r"[-+]?\d*\.\d+|\d+", content))
    length = len(data)
    eth = data[2:length-2]

    embed = discord.Embed(
        title = 'ETHEREUM = €' + eth,
        color = 0x7593FF
        )

    await ctx.send(embed=embed)

@client.command
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('sound'):
        await message.channel.send('no boder')

client.run(token)
