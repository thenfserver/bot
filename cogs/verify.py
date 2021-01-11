import discord
from discord.ext import commands

class verify(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      message_id = payload.message_id
      
      if message_id == 786043482770767902:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        if payload.emoji.name == '✅':
          role1 = discord.utils.get(guild.roles, name="Verified")
          role2 = discord.utils.get(guild.roles, name="Let You Down fan")

        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
        if member is not None:
          await member.add_roles(role1)
          await member.add_roles(role2)

    @commands.command()
    @commands.is_owner()
    async def verify(self, ctx):
      msg = await ctx.send("To cut down on raids on this server you must now verify before you can chat in this server, before you click the ✅ make sure to read the rules in <#706977106831343636>.")
      reactions = ["✅"]
      for emoji in reactions[:len(reactions)]:
          await msg.add_reaction(emoji)

def setup(bot):
    bot.add_cog(verify(bot))