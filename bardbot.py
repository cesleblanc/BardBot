import discord, requests
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True  # The correct way to enable message content intent


bot = commands.Bot(command_prefix='!', intents=intents)

def find_rhymes(word):
  print('Looking for rhymes...')
  url = f"https://api.datamuse.com/words?rel_rhy={word}"
  response = requests.get(url)
  if response.status_code == 200:
    rhymes = [result['word'] for result in response.json()]
    return rhymes
  else:
    return []

@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name}')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

@bot.command()
async def rhyme(ctx, word: str):
  # Logic to find rhymes for the provided word
  rhymes = find_rhymes(word)

bot.run('SECRET_TOKEN')