import requests
import bs4 as bs
import time
import discord
from discord.ext import commands
import re

client = commands.Bot(command_prefix =  '!')

token = 'USER_TOKEN'

@client.event
async def on_ready():
    print("ya boy ready")

@client.command(pass_context=True)
async def gimme(ctx):
    while 1:
        url = 'https://bitflyer.com/en-eu/bitcoin-chart'
        content = requests.get(url)
        soup = bs.BeautifulSoup(content.text, 'lxml')
        stock = str(soup.find("div", {"class": "p-currencyInfo__price c-text--number"}).text)

        embed = discord.Embed(
        title = stock,
        color = discord.Color.gold()
        )
        await ctx.send(embed=embed)

        time.sleep(10)

client.run(token)
