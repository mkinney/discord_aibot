# Note: started from the basic_bot.py example

import os
import discord
from discord.ext import commands
from pygpt4all.models.gpt4all_j import GPT4All_J

def new_text_callback(text):
    return text

discord_token = os.environ['DISCORD_TOKEN']

description = '''An example bot to showcase pygpt4all'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

model = GPT4All_J('ggml-gpt4all-j-v1.3-groovy.bin')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
async def ai(ctx, *, question: str):
    """Ask the ai a question."""
    response = model.generate(question, n_predict=55, new_text_callback=new_text_callback)
    # get rid of the question and trailer
    ans = response.replace(question,"")
    ans = ans.replace("<|endoftext|>","")
    await ctx.send("Asked ai:{}\nResponse:{}".format(question, ans))


bot.run(discord_token)
