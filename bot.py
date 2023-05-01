import os
import discord
from discord.ext import commands
from pygpt4all.models.gpt4all import GPT4All
from dotenv import load_dotenv

load_dotenv()
discord_token = os.getenv("DISCORD_TOKEN")

description = '''An example bot to showcase pygpt4all'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

model = GPT4All('ggml-gpt4all-l13b-snoozy.bin')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ai(ctx, *, question: str):
    """Ask the ai a question."""
    ans = ""
    # Note: Every 10 seconds, you will get a WARNN level logging message
    # that will look like this:
    #   {gateway.py:186} WARNING - Shard ID None heartbeat blocked for more than xxx seconds.
    for token in model.generate(question, temp=0.28, n_predict=4096):
        ans += token
    await ctx.send("ai:{}\n".format(ans))

bot.run(discord_token)
