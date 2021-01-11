import discord
from discord.ext import commands

class yrreaction(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Years
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      message_id = payload.message_id
      
      if message_id == 784530715530231818:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        if payload.emoji.name == '5️⃣':
          role = discord.utils.get(guild.roles, name="2015")
        elif payload.emoji.name == '6️⃣':
          role = discord.utils.get(guild.roles, name="2016")
        elif payload.emoji.name == '7️⃣':
          role = discord.utils.get(guild.roles, name="2017")
        elif payload.emoji.name == '8️⃣':
          role = discord.utils.get(guild.roles, name="2018")
        elif payload.emoji.name == '9️⃣':
          role = discord.utils.get(guild.roles, name="2019")
        elif payload.emoji.name == '0️⃣':
          role = discord.utils.get(guild.roles, name="2020")

        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
        if member is not None:
          await member.add_roles(role)

    #Years
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
      message_id = payload.message_id
      
      if message_id == 784530715530231818:
        guild_id = payload.guild_id
        guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)

        if payload.emoji.name == '5️⃣':
          role = discord.utils.get(guild.roles, name="2015")
        elif payload.emoji.name == '6️⃣':
          role = discord.utils.get(guild.roles, name="2016")
        elif payload.emoji.name == '7️⃣':
          role = discord.utils.get(guild.roles, name="2017")
        elif payload.emoji.name == '8️⃣':
          role = discord.utils.get(guild.roles, name="2018")
        elif payload.emoji.name == '9️⃣':
          role = discord.utils.get(guild.roles, name="2019")
        elif payload.emoji.name == '0️⃣':
          role = discord.utils.get(guild.roles, name="2020")

        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)    
        if member is not None:
          await member.remove_roles(role)
      
def setup(bot):
    bot.add_cog(yrreaction(bot))