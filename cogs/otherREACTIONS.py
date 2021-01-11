import discord
from discord.ext import commands

class otherreactions(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    message_id = payload.message_id
    
    if message_id == 785239688897101830:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

      if payload.emoji.name == '📢':
        role = discord.utils.get(guild.roles, name="Announcements")
      elif payload.emoji.name == '🎁':
        role = discord.utils.get(guild.roles, name="Giveaway")
      elif payload.emoji.name == '🗳️':
        role = discord.utils.get(guild.roles, name="Polls")
      elif payload.emoji.name == '🎮':
        role = discord.utils.get(guild.roles, name="Gaming")
      elif payload.emoji.name == '💯':
        role = discord.utils.get(guild.roles, name="Fact Of The Day")
      elif payload.emoji.name == '💭':
        role = discord.utils.get(guild.roles, name="Quote Of The Day")
      elif payload.emoji.name == '🎵':
        role = discord.utils.get(guild.roles, name="Song vs Song")
      elif payload.emoji.name == '🎥':
        role = discord.utils.get(guild.roles, name="Movie")
      elif payload.emoji.name == '❤️':
        role = discord.utils.get(guild.roles, name="Vent")
      elif payload.emoji.name == '🤍':
        role = discord.utils.get(guild.roles, name="Motivation")

      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
      if member is not None:
        await member.add_roles(role)

  @commands.Cog.listener()
  async def on_raw_reaction_remove(self, payload):
    message_id = payload.message_id
      
    if message_id == 785239688897101830:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

      if payload.emoji.name == '📢':
        role = discord.utils.get(guild.roles, name="Announcements")
      elif payload.emoji.name == '🎁':
        role = discord.utils.get(guild.roles, name="Giveaway")
      elif payload.emoji.name == '🗳️':
        role = discord.utils.get(guild.roles, name="Polls")
      elif payload.emoji.name == '🎮':
        role = discord.utils.get(guild.roles, name="Gaming")
      elif payload.emoji.name == '💯':
        role = discord.utils.get(guild.roles, name="Fact Of The Day")
      elif payload.emoji.name == '💭':
        role = discord.utils.get(guild.roles, name="Quote Of The Day")
      elif payload.emoji.name == '🎵':
        role = discord.utils.get(guild.roles, name="Song vs Song")
      elif payload.emoji.name == '🎥':
        role = discord.utils.get(guild.roles, name="Movie")
      elif payload.emoji.name == '❤️':
        role = discord.utils.get(guild.roles, name="Vent")
      elif payload.emoji.name == '🤍':
        role = discord.utils.get(guild.roles, name="Motivation")

      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
      if member is not None:
        await member.remove_roles(role)

def setup(bot):
    bot.add_cog(otherreactions(bot))