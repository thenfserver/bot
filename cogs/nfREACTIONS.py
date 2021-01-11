import discord
from discord.ext import commands

class nfreactions(commands.Cog):
  def __init__(self, client):
    self.client = client

  #NF Notications 
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    message_id = payload.message_id
      
    if message_id == 784530728502296617:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

      if payload.emoji.name == '📢':
        role = discord.utils.get(guild.roles, name="Feed")
      elif payload.emoji.name == '🐦':
        role = discord.utils.get(guild.roles, name="Twitter")
      elif payload.emoji.name == '💿':
        role = discord.utils.get(guild.roles, name="Youtube")

      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
      if member is not None:
        await member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    message_id = payload.message_id
      
    if message_id == 784530728502296617:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

      if payload.emoji.name == '📢':
        role = discord.utils.get(guild.roles, name="Feed")
      elif payload.emoji.name == '🐦':
        role = discord.utils.get(guild.roles, name="Twitter")
      elif payload.emoji.name == '💿':
        role = discord.utils.get(guild.roles, name="Youtube")

      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
      if member is not None:
        await member.remove_roles(role)

def setup(bot):
  bot.add_cog(nfreactions(bot))