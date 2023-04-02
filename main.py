# <required imports>
import discord
from discord.ext import commands
from os import system, name, getlogin, getcwd
from sys import platform

# <user config>
from config import token, administrators

# <discord bot>
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("Bot is ready.")
    bot.tree.sync()
    bot.activity = discord.Activity(type=discord.ActivityType.watching, name=f"over {len(bot.get_guild(1091796815743025324).member_count())} users")

@bot.hybrid_command(name="help")
async def help(ctx):
    help = discord.Embed(

    )
    ctx.send(help)

@bot.hybrid_command(name="hardware")
async def hardware(ctx):
    info = discord.Embed(

    )
    ctx.send(info)

@bot.hybrid_command(name="restart")
async def restart(ctx):
    if ctx.author.id in administrators:
        await ctx.send("RESTARTING SERVER...")
        system(r"screen -S minecraft -X stuff `echo -ne \"stop\r\"`")
        await ctx.send("Server stopped...")
        system(r"screen -S minecraft -X stuff `echo -ne \"java -jar download.jar\r\"`")
        await ctx.send("Server started, wait a few mintues for it to load...")
    else:
        await ctx.send("You are not an administrator.")

# <run bot>
bot.run(token)
