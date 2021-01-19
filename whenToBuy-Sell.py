import requests
import time
import discord
from discord.ext import commands
import re

client = commands.Bot(command_prefix =  '!')

token = 'BOT_TOKEN'

@client.event
async def on_ready():
    print("Bot Ready")


@client.command(pass_context=True)
async def on(ctx):
    winnerB1 = winnerB2 = winnerE1 = winnerE2 = 0

    while 1:

        url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
        content = requests.get(url).text
        data = str(re.findall(r"[-+]?\d*\.\d+|\d+", content))
        length = len(data)
        bit = data[2:length-2]

        if float(bit) < 29500 and winnerB1 == 0:
            embed = discord.Embed(
                title = 'BITCOIN = €' + bit,
                description = 'BUY NOW BUY NOW!!!!',
                color=discord.Color.gold()
            )
            await ctx.send(embed=embed)
            time.sleep(1)
            await ctx.send(embed=embed)
            time.sleep(1)
            await ctx.send(embed=embed)
            winnerB = 1
        elif float(bit) > 34000 and winnerB2 == 0:
            embed = discord.Embed(
                title = 'BITCOIN = €' + bit,
                description = 'SELL NOW SELL NOW!!!!',
                color=discord.Color.gold()
            )
            await ctx.send(embed=embed)
            winnerB2 = 1
        else:
            print('BITCOIN = €' + content[18:23])
            
        
        url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
        content = requests.get(url).text
        data = str(re.findall(r"[-+]?\d*\.\d+|\d+", content))
        length = len(data)
        ether = data[2:length-2]

        if float(ether) < 1000 and winnerE1 == 0:
            embed = discord.Embed(
                title = 'ETHEREUM = €' + ether,
                description = 'BUY NOW BUY NOW!!!!',
                color= 0x7593FF
            )
            await ctx.send(embed=embed)
            time.sleep(1)
            await ctx.send(embed=embed)
            time.sleep(1)
            await ctx.send(embed=embed)
            winnerE = 1
        elif float(ether) > 1200 and winnerE2 == 0:
            embed = discord.Embed(
                title = 'ETHEREUM = €' + ether,
                description = 'SELL NOW SELL NOW!!!!',
                color=discord.Color.gold()
            )
            await ctx.send(embed=embed)
            winnerE2 = 1
        else:
            print('ETHEREUM = €' + ether + '\n')

        if winnerB1 == 1 and winnerE1 == 1 and winnerB2 == 1 and winnerE2 == 1:
            break

        time.sleep(180)

client.run(token)


