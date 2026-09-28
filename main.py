import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='>', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx. send('pong')

# 請記得把 'token' 換成您在 Discord Developer Portal 申請的機器人 Token
bot.run('MTU1NDAyODc0MjA4NTQ0MzY1NA.G4hkFr.SUj7TsoUPCPp_CkvXv9ONoPkP5Qb6H0PHGDfTU') 
