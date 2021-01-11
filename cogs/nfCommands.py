import discord, random
from discord.ext import commands

class nf(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def album(self, ctx):
    fo = open("utils/lists/albums.txt")
    album = fo.readlines()
    embed = discord.Embed(title="Random Album", description=f"{random.choice(album)}", color=0x36393e)
    await ctx.send(embed=embed)

  @commands.command()
  async def quote(self, ctx):
    fo = open("utils/lists/quotes.txt", "r")
    quote = fo.readlines()
    embed = discord.Embed(title="Random Quote", description=f"{random.choice(quote)}",color=0x36393e)
    await ctx.send(embed=embed)

  @commands.command()
  async def song(self, ctx):
    fo = open("utils/lists/songs.txt", "r")
    song = fo.readlines()
    embed = discord.Embed(title="Random Song", description=f"{random.choice(song)}",color=0x36393e)
    await ctx.send(embed=embed)

  @commands.command()
  async def social(self, ctx):
    embed = discord.Embed(color=discord.Color.default())
    embed.set_author(name="Social - NFrealmusic")
    embed.add_field(name="Stream NF", value="[Spotify](https://open.spotify.com/artist/6fOMl44jA4Sp5b9PpYCkzz)\n[Soundcloud](https://soundcloud.com/nfrealmusic)\n[Amazon Music](https://music.amazon.com/artists/B00FPGTO3I)\n[Google Play](https://play.google.com/store/music/artist?id=A3mml7nahg44vbtycguv5zwlbay&hl=en_US)\n[Apple Music](http://music.apple.com/us/artist/898094630)\n[Youtube Music](https://music.youtube.com/channel/UCjiGsk3ePl9fajUfgNVFGBA)\n[Pandora](https://www.pandora.com/artist/nf/AR2hppzZrfxvXK4)\n[iHeartRADIO](https://www.iheart.com/artist/nf-958998/)")
    embed.add_field(name="NF's Social", value="[Twitter](https://twitter.com/nfrealmusic)\n[Instagram](https://instagram.com/nfrealmusic)\n[Youtube](https://www.youtube.com/channel/UCoRR6OLuIZ2-5VxtnQIaN2w)")
    await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(nf(bot))