import discord
from discord.ext import commands
import os

# Intents設定（メンバー関連の情報にアクセスする場合は適切なIntentsを有効にする必要があります）
intents = discord.Intents.default()
intents.message_content = True

# Botの接続設定
bot = commands.Bot(command_prefix="!", intents=intents)  # プレフィックスを任意で設定

# Botの起動時メッセージ
@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

# シンプルなpingコマンド
@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Discordのボットトークンを環境変数から取得して起動
bot.run(os.getenv("DISCORD_TOKEN"))
