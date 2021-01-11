import discord, os, aiohttp, random, requests
from discord.ext import commands

from utils import http

class pictures(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cat(self, ctx):
        """ Posts a random cat """
        catr = requests.get('https://some-random-api.ml/img/cat')
        catf = str(catr.json()['link'])
        embed = discord.Embed(title=":cat: Random Cat", color=discord.Color.default())
        embed.set_image(url=catf)
        embed.set_footer(text=f"{ctx.author}")
        await ctx.send(embed=embed) 

    @commands.command()
    async def dog(self, ctx):
        """ Posts a random dog """
        dogr = requests.get('https://some-random-api.ml/img/dog')
        dogf = str(dogr.json()['link'])
        embed = discord.Embed(title=":dog: Random Dog", color=discord.Color.default())
        embed.set_image(url=dogf)
        embed.set_footer(text=f"{ctx.author}")
        await ctx.send(embed=embed)

    @commands.command(aliases=["bird"])
    async def birb(self, ctx):
        """ Posts a random birb """
        birdr = requests.get('https://some-random-api.ml/img/birb')
        birdf = str(birdr.json()['link'])
        embed = discord.Embed(title=":bird: Random Bird", color=discord.Color.default())
        embed.set_image(url=birdf)
        embed.set_footer(text=f"{ctx.author}")
        await ctx.send(embed=embed)

    @commands.command()
    async def panda(self, ctx):
      pandar = requests.get(random.choice(['https://some-random-api.ml/img/panda', 'https://some-random-api.ml/img/red_panda']))
      pandaf = str(pandar.json()['link'])
      embed = discord.Embed(title=":panda_face: Random Panda", color=discord.Color.default())
      embed.set_image(url=pandaf)
      embed.set_footer(text=f"{ctx.author}")
      await ctx.send(embed=embed)

    @commands.command()
    async def lizard(self, ctx):
      await self.randomimageapi(ctx, 'https://nekos.life/api/lizard', 'url')
  
    @commands.command()
    async def fox(self, ctx):
      foxr = requests.get('https://randomfox.ca/floof/')
      foxf = str(foxr.json()['image'])
      await ctx.send(foxf)

def setup(bot):
    bot.add_cog(pictures(bot))