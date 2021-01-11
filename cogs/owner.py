import discord, os
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions


class owner(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def eval(self, ctx, *, expr):
        try:
            result = eval(expr)
            embed = discord.Embed(color=discord.Color.green())
        except Exception as error:
            embed = discord.Embed(color=discord.Color.red())
            result = str(error)

        embed.add_field(name="Input:", value=f":inbox_tray: ```{expr}```", inline = False)
        embed.add_field(name="Output:", value=f":outbox_tray: ```{result}```", inline = False)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, extension):
      self.client.reload_extension(f'cogs.{extension}')
      await ctx.send(f"Reloaded the cog `{extension}`.")

    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, extension):
      self.client.load_extension(f'cogs.{extension}')
      await ctx.send(f"Loaded the cog `{extension}`.")    

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, extension):
      self.client.unload_extension(f'cogs.{extension}')
      await ctx.send(f"Unloaded the cog `{extension}`.")
          
    @commands.command()
    @commands.is_owner()
    async def stop(self, ctx):
        """ Stops the bot. """
        await ctx.send(f'Stopping {self.client.user.name}...')
        await self.client.change_presence(activity=discord.Game(type=0, name='Stopping...'), status=discord.Status.dnd)
        await self.client.logout()

    @commands.command()
    @has_permissions(administrator=True)
    async def say(self, ctx, *, message):
      await ctx.send(message)
      await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def dm(self, ctx, member: discord.Member=None, *, context):
      await member.send(context)
      await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def years(self, ctx):
      embed = discord.Embed(description=":five:: 2015 or before \n:six:: 2016\n:seven:: 2017\n:eight:: 2018\n:nine:: 2019\n:zero:: 2020", color=discord.Color.default())
      msg = await ctx.send("What year did you discover NF?", embed=embed)
      reactions = ["5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "0️⃣"]
      for emoji in reactions[:len(reactions)]:
          await msg.add_reaction(emoji)

    @commands.command()
    @commands.is_owner()
    async def nfnoti(self, ctx):
      embed = discord.Embed(description=":loudspeaker:: All of NF's Feed\n:bird:: NF's Twitter\n:cd:: NF's YouTube\n", color=discord.Color.default())
      msg = await ctx.send("React below to get notifications when NF posts.", embed=embed)
      reactions = ["📢","🐦", "💿"]
      for emoji in reactions[:len(reactions)]:
        await msg.add_reaction(emoji)

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx):
      embed = discord.Embed(description=":loudspeaker:: Announcements\n:gift:: Giveaway (Must be level 20+ to gain access)\n:ballot_box:: Polls\n:video_game:: Gaming\n:100:: Fact Of The Day\n:thought_balloon:: Quote Of The Day\n:musical_note:: Song Vs. Song\n:movie_camera:: Movie Night\n❤️: Vent\n🤍: Motivational Mondays", color=discord.Color.default())
      msg = await ctx.send("React below to get Roles!", embed=embed)
      reactions = ["📢", "🎁", "🗳️", "🎮", "💯", "💭", "🎵", "🎥", "❤️", "🤍"]
      for emoji in reactions[:len(reactions)]:
          await msg.add_reaction(emoji)
      
def setup(bot):
    bot.add_cog(owner(bot))