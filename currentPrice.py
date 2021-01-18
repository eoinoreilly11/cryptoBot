import requests
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  '!')

token = 'BOT_TOKEN'

@client.event
async def on_ready():
    print("Bot 2 Ready")


@client.command(pass_context=True)
async def bit(ctx):

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
    content = requests.get(url).text

    embed = discord.Embed(
        title = 'BITCOIN = €' + content[18:23],
        color=discord.Color.gold()
        )

    await ctx.send(embed=embed)

@client.command(pass_context=True)
async def ether(ctx):

    url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
    content = requests.get(url).text

    embed = discord.Embed(
        title = 'ETHEREUM = €' + content[19:23],
        color = 0x7593FF
        )

    await ctx.send(embed=embed)

client.run(token)
    
