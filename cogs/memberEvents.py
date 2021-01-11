import discord, time, random
from discord.ext import commands

class welcome(commands.Cog):
    def __init__(self, client):
        self.client = client   
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
      LeaveChannel = self.client.get_channel(719710156576915556)
      channel = self.client.get_channel(775144350178082816)
      fo = open("utils/lists/leaves.txt")
      LeaveMessage = fo.readlines()
      await LeaveChannel.send(f"**{member}** {random.choice(LeaveMessage)}")
      await channel.edit(name=f"Outcasts: {len(member.guild.members)}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
      autoRole = discord.utils.get(member.guild.roles, name="Let You Down fan")
      WelcomeChannel = self.client.get_channel(712354983961559042)
      channel = self.client.get_channel(775144350178082816)
      await WelcomeChannel.send(f"Hey {member.mention}, welcome to **NFREALMUSIC** discord server:tada:! Make sure to read the <#706977106831343636>, tell us about yourself and grab some <#711644476627746848>.")
      await channel.edit(name=f"Outcasts: {len(member.guild.members)}")
      await member.add_roles(autoRole)

def setup(bot):
    bot.add_cog(welcome(bot))