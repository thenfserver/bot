import discord, os, time, random, datetime, asyncio, platform
from discord.ext import commands

from utils import keep_alive

start_time = time.time()

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix =["nf!", "NF!", "Nf!", "nF!", "nf! ", "NF! ", "Nf! ", "nF! "], case_insensitive=True, intents=intents)
token = os.environ['TOKEN']
client.remove_command('help')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

@client.event
async def on_ready():
  print(f"Succesfully signed in as {client.user.name} ({client.user.id}).")

  channel = client.get_channel(743246479594094693)
  embed = discord.Embed(description=f"{client.user.name} has booted on {time.ctime()}.",color=discord.Color.green())
  await channel.send(embed=embed)

async def ch_pr():
  await client.wait_until_ready()

  statuses = ["Chasing | nf!help", "DM for ModMail | nf!help"]

  while not client.is_closed():

    status = random.choice(statuses)
    await client.change_presence(activity=discord.Game(name=status))

    await asyncio.sleep(30)
    
client.loop.create_task(ch_pr())

@client.command()
async def info(ctx):
  """ The bot's info. """
  current_time = time.time()
  difference = int(round(current_time - start_time))
  text = str(datetime.timedelta(seconds=difference))
  embed = discord.Embed(color=discord.Color.green())
  embed.set_author(name=f"{client.user.name}'s Info")
  embed.set_footer(text=f"Ping {round(client.latency * 1000)}ms | Uptime {text} | Version 2020.20.09")
  embed.add_field(name="Developer", value=f"bread#7620", inline=True)
  embed.add_field(name="Language", value=f"Python {platform.python_version()}")
  embed.add_field(name="Libary", value=f"discord.py {discord.__version__}", inline=True)        
  embed.add_field(name="Users", value=f"`{len(set(client.get_all_members()))}`", inline=True)
  embed.add_field(name="Github", value=f"[Click Here](https://github.com/IronCodez/nfrealbot/)")
  embed.add_field(name="Status", value="[Click Here](https://stats.uptimerobot.com/L5ZkxcPQNB)")
  await ctx.send(embed=embed)

@client.command()
async def uptime(ctx):
    current_time = time.time()
    difference = int(round(current_time - start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(color=discord.Color.green(), description=text)
    await ctx.send(embed=embed)

keep_alive.keep_alive()
client.run(token, bot=True, reconnect=True)