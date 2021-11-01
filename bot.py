import os
from discord.ext import commands
import discord
from dotenv import load_dotenv
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
import asyncio

load_dotenv('DISCORD_TOKEN.env')#loads client secret from the .env file in the same directory
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='^') #change it to whatever you want
bot.remove_command("help")

@bot.event
async def on_ready():
    activity = discord.Game(name="A game", type=3) #you can change from playing to watching, etc 
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    
@bot.command()
@commands.has_permissions(ban_members=True)#bans members if admin role is true
async def ban(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.ban(reason=reason)
        ban = discord.Embed(title=f":boom: Banned {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}",color=0xB026FF)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member, *, reason="No reason provided"):
        await user.kick(reason=reason)
        ban = discord.Embed(title=f":boot: Kicked {user.name}!", description=f"Reason: {reason}\nBy: {ctx.author.mention}",color=0xB026FF)
        await ctx.message.delete()
        await ctx.channel.send(embed=ban)
        await user.send(embed=ban)

@bot.command()## get mentioned users avatar
async def av(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

@bot.command()##help command
async def help(ctx):
    em = discord.Embed(title="Tutorial Bot command list:", description="", color=0x2f3136)
    em.add_field(name="`^ban {user}`", value="Bans the user.")
    em.add_field(name="`^kick {user}`", value="Kicks user.")
    em.add_field(name="`^av {user}`", value="Gets the mentioned users pfp.")

    em.set_footer(text="GitHub Discord bot made by cyber")
    await ctx.send(embed=em)

bot.run(TOKEN)
