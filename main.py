import discord
from discord.ext import commands

# 1. 設定機器人的意圖 (Intents)
intents = discord.Intents.default()
intents.message_content = True

# 2. 初始化機器人，設定指令前綴為 '>' (修正了您截圖中斷掉的第7行)
bot = commands.Bot(command_prefix='>', intents=intents)

# 3. 當輸入 >ping 時，機器人會回應 pong
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# 4. 啟動機器人 (請將下方文字替換成您剛剛重置的「新 Token」)
bot.run('MTU1NjE3OTMwMzIwMzM0ODUwMQ.GxwP2s.6tnrPAse-UMAqDr87ofoDz7Qxkf5RgJRngqdyI')
