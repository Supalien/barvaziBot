import discord
from discord.ext import commands
import asyncio
import sys

INVITE_LINK = 'https://discordapp.com/api/oauth2/authorize?client_id=688789378000224328&permissions=8&scope=bot'
VIDEO_LINK = 'https://discordapp.com/channels/'
bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('---------')
    print('Versions')
    print(sys.version[:5])
    print(discord.__version__)
    print('---------')
    print('Commands')
    print(*[c.name for c in bot.commands])
    print('---------')

@bot.command(aliases=['ss', 'share', 'screen_share', 'screen', 'videoshare', 'video'])
async def screenshare(ctx):
    if ctx.author.voice == None:
            await ctx.send('בבקשה הצטרף/י לשיחת קול')
            return
    url = f'https://discordapp.com/channels/{ctx.guild.id}/{ctx.author.voice.channel.id}'
    emb = discord.Embed(description=f'[לחצו כאן כדי להצטרף לשיחת הוידאו]({url})')
    await ctx.send(embed=emb)


with open('token.txt') as f:
    token = f.read()
    bot.run(token.strip())
