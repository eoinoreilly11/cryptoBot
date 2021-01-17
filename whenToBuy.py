import requests
import time
import discord
from discord.ext import commands

client = commands.Bot(command_prefix =  '!')

token = 'BOT_TOKEN'

@client.event
async def on_ready():
    print("Bot Ready")


@client.command(pass_context=True)
async def on(ctx):
    winnerB = 0
    winnerE = 0
    while 1:

        if winnerB == 0:
            url = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=eur'
            content = requests.get(url).text

            if int(content[18:23]) < 28000:
                embed = discord.Embed(
                    title = 'BITCOIN = €' + content[18:23],
                    description = 'BUY NOW BUY NOW!!!!',
                    color=discord.Color.gold()
                )
                await ctx.send(embed=embed)
                time.sleep(1)
                await ctx.send(embed=embed)
                time.sleep(1)
                await ctx.send(embed=embed)
                winnerB = 1
            else:
                print('BITCOIN = €' + content[18:23])
            
        if winnerE == 0:
            url = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=eur'
            content = requests.get(url).text

            if int(content[19:23]) < 900:
                embed = discord.Embed(
                    title = 'ETHEREUM = €' + content[19:23],
                    description = 'BUY NOW BUY NOW!!!!',
                    color= 0x7593FF
                )
                await ctx.send(embed=embed)
                time.sleep(1)
                await ctx.send(embed=embed)
                time.sleep(1)
                await ctx.send(embed=embed)
                winnerE = 1
            else:
                print('ETHEREUM = €' + content[19:23] + '\n')

        if winnerB == 1 and winnerE == 1:
            break
        time.sleep(180)

client.run(token)


