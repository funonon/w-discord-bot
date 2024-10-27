import discord
from discord.ext import commands
import os
from keep_alive import keep_alive  # 追加

# Botの設定
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# サーバーの起動
keep_alive()  # 追加

# Discordのボットトークンを使って起動
bot.run(os.getenv("DISCORD_TOKEN"))
