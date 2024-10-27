import os
from discord.ext import commands
from flask import Flask
import threading

# Flaskアプリケーションを定義して、Render上で動かす
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is alive!"  # RenderのURLにアクセスするとこのメッセージが表示されます

# Flaskサーバーを別スレッドで実行する関数
def run():
    app.run(host='0.0.0.0', port=8080)

# Discordのボットの設定
intents = discord.Intents.default()  # 必要なインテントを設定
intents.message_content = True  # メッセージ内容のインテントを有効化

bot = commands.Bot(command_prefix="!", intents=intents)  # コマンドプレフィックスを"!"に設定

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')  # ログイン完了時に表示されるメッセージ
    await bot.change_presence(activity=discord.Game(name="Bot is online!"))  # ボットのステータスを表示

# サンプルのコマンド
@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I'm your bot!")  # !helloと入力すると返信

@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! Latency is {round(bot.latency * 1000)}ms')  # !pingと入力すると応答

# Flaskサーバーを開始
t = threading.Thread(target=run)
t.start()

# ボットを実行
bot.run(os.getenv('DISCORD_TOKEN'))  # 環境変数からトークンを取得してボットを起動
