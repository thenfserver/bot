import discord, time, random
from discord.ext import commands
from datetime import datetime as d
from collections import deque
 
class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
      start = d.timestamp(d.now())
      embed = discord.Embed(description=f"Latency: `{round(self.client.latency * 1000, 3)}`ms", color=0x36393e)
      await ctx.send(embed=embed)

      """await ctx.send(":ping_pong: Wew, I made it over the ~waves~. `{}ms` is my heartbeat (latency) :heart:.".format(round(self.client.latency * 1000, 3)))"""


    @commands.command()
    async def help(self, ctx, mode=None):
        if mode == None:
          embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at)
          embed.set_author(name=f"Help - NFrealbot \nPrefix: nf!")
          embed.add_field(name="Infomation (nf!help infomation)", value= "`nf!help` `nf!ping` `nf!suggestion` `nf!serverinfo` `nf!userinfo` `nf!roleinfo` `nf!botinfo` `nf!membercount` `nf!avatar`", inline=False)
          embed.add_field(name="Staff (nf!help staff)", value= "`nf!staff` `nf!ban` `nf!kick` `nf!kick` `nf!svs` `nf!qotd` `nf!raid` `nf!mute` `nf!unmute`", inline=False)
          embed.add_field(name="NF (nf!help nf)", value="`nf!song` `nf!quote` `nf!album` `nf!social`", inline=False)
          embed.add_field(name="Fun (nf!help fun)", value="`nf!rps` `nf!8ball` `nf!coinflip` `nf!randomnumber` `nf!gayrate` `nf!simprate` `nf!epicgamerrate`", inline=False)
          embed.add_field(name="Photos {nf!help photos}", value="`nf!dog` `nf!cat` `nf!birb` `nf!panada` `nf!fox`")
          await ctx.send(embed=embed)
        elif mode == "infomation":
            embed = discord.Embed(
                color=discord.Color.green(), timestamp=ctx.message.created_at)
            embed.set_author(name=f"Help - NFrealbot \nPrefix: nf!")
            embed.add_field(
                name="Infomation", value="Infomation commands.", inline=False)
            embed.add_field(
                name="> nf!help",
                value="`Sends the help command.`",
                inline=True)
            embed.add_field(
                name="> nf!ping",
                value="`Sends the latency of the bot.`",
                inline=True)
            embed.add_field(
                name="> nf!suggestion",
                value="`Suggest something. (nf!suggestion server {suggestion})`",
                inline=True)
            embed.add_field(
                name="> nf!serverinfo",
                value="`Sends infomation about the serer.`",
                inline=True)
            embed.add_field(
                name="> nf!userinfo",
                value="`Sends infomation about the specifed user.`",
                inline=True)
            embed.add_field(
                name="> nf!roleinfo",
                value="`Sends infomation about the specifed role.`")
            embed.add_field(
                name="> nf!botinfo",
                value="`Sends infomation about NFrealbot.`")
            embed.add_field(
                name="> nf!membercount",
                value="`Sends the member count of the server.`",
                inline=True)
            embed.add_field(
                name="> nf!avatar",
                value="`Sends the avatar of the specifed user.`")
            await ctx.send(embed=embed)
        elif mode == "staff":
            embed = discord.Embed(color=discord.Color.green(), timestamp=ctx.message.created_at)
            embed.set_author(name=f"Help - NFrealbot \nPrefix: nf!")
            embed.add_field(name="Staff", value="Staff commands.", inline=False)
            embed.add_field(name="> nf!ban", value="`Bans the specifed user.`", inline=True)
            embed.add_field(name="> nf!kick", value="`Kicks the specifed user.`", inline=True)
            embed.add_field(name="> nf!svs", value="`Sends the song vs song.`")
            embed.add_field(name="> nf!qotd", value="`Sends the quote of the day.`")
            embed.add_field(name="> nf!change", value="Run the command for useage." )
            await ctx.send(embed=embed)
        elif mode == "nf":
            embed = discord.Embed(
                color=discord.Color.green(), timestamp=ctx.message.created_at)
            embed.set_author(name=f"Help - NFrealbot \nPrefix: nf!")
            embed.add_field(name="NF", value="NF commands.", inline=False)
            embed.add_field(
                name="> nf!song",
                value="`Send a random song made by NF.`",
                inline=True)
            embed.add_field(
                name="> nf!quote",
                value="`Send a random quote said by NF.`",
                inline=True)
            embed.add_field(
                name="> nf!album",
                value="`Sends a random album made by NF.`",
                inline=True)
            embed.add_field(
                name="> nf!social",
                value="`Sends all of NF's socials.`",
                inline=True)
            await ctx.send(embed=embed)
        elif mode == "fun":
            embed = discord.Embed(
                color=discord.Color.green(), timestamp=ctx.message.created_at)
            embed.set_author(name=f"Help - NFrealbot")
            embed.add_field(name="Fun", value="Fun commands.", inline=False)
            embed.add_field(
                name="> nf!rps", value="`Rock, paper, scissors.`", inline=True)
            embed.add_field(
                name="> nf!8ball", value="`Magic 8ball.`", inline=True)
            embed.add_field(
                name="> nf!coinflip", value="`Flips a coin.`", inline=True)
            embed.add_field(
                name="> nf!randomnumber",
                value="`Picks a random number 1-100`")
            await ctx.send(embed=embed)

    @commands.command()
    async def suggestion(self, ctx, mode=None, *, content: str=None):
      if mode == None:
        embed = discord.Embed(title="Suggestion", description="`nf!suggestion server {suggestion}` \n`nf!suggestion bot {suggestion}`", color=discord.Color.green())
        await ctx.send(embed=embed)
      elif mode == "server":
        if content == None:
          embed = discord.Embed(title="Server Suggestion", description="nf!suggestion server {suggestion}", color=0x36393e)
          await ctx.send(embed=embed)
        else:  
          embed = discord.Embed(title="Server Suggestion", description=content, color=discord.Color.green(), timestamp=ctx.message.created_at)
          embed.set_footer(text=f"Suggested by {ctx.author.name} ({ctx.author.id}) | Suggested ")
          channel = self.client.get_channel(709150055881375776)
          msg = await channel.send(embed=embed)
          reactions = ['<:upvote:774364895122292777>', '<:downvote:774364895096995840>']
          for emoji in reactions[:len(reactions)]:
              await msg.add_reaction(emoji)
          await ctx.message.delete()
      elif mode == "bot":
        embed = discord.Embed(title="Bot Suggestion", description=content, color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_footer(text=f"Suggested by {ctx.author.name} ({ctx.author.id}) | Suggested ")
        channel = self.client.get_channel(709150055881375776)
        msg = await channel.send(embed=embed)
        reactions = ['<:upvote:774364895122292777>', '<:downvote:774364895096995840>']
        for emoji in reactions[:len(reactions)]:
            await msg.add_reaction(emoji)
        await ctx.message.delete()

    @commands.command()
    async def serverinfo(self, ctx, guild: discord.Guild = None):
        guild = ctx.author.guild
        embed = discord.Embed(color=guild.owner.color, timestamp=guild.created_at)
        embed.set_author(name=f"{guild.name}", icon_url=guild.icon_url)
        embed.set_footer(text=f"ID: {guild.id} | Server Created")
        embed.add_field(name="Owner", value=guild.owner)
        embed.add_field(name="Region", value=guild.region)
        embed.add_field(name="Channel Catergories", value=len(guild.categories))
        embed.add_field(name="Text Channels", value=len(guild.text_channels))
        embed.add_field(name="Voice Channels", value=len(guild.voice_channels))
        embed.add_field(name="Members", value=len(guild.members))
        embed.add_field(name="Roles", value=len(guild.roles))
        await ctx.send(embed=embed)
        await ctx.send((random.choice(guild.members)))

    @commands.command()
    async def userinfo(self, ctx, *, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles[1:]]
        roles = deque(roles)
        roles.rotate(len(member.roles))
        roles = list(roles)  

        embed = discord.Embed(description=f"**<:Emojadfadsf:785015239523172383> User Infomation**\nID: {member.id}\nProfile: {member.mention}\nCreated: {member.created_at}\n\n<:Emojadfadsf:785015239523172383> **Member Infomation**\nJoined: {member.joined_at}\nRoles: [{len(member.roles)-1}] {''.join([role.mention for role in roles])} ", color=discord.Color.green())
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=f"{member.name}", icon_url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def roleinfo(self, ctx, *, role: discord.Role):
        embed = discord.Embed(color=role.color, timestamp=ctx.message.created_at)
        embed.set_author(name=f"{role.name}")
        embed.set_footer(text=f"ID: {role.id}")
        embed.add_field(name=f"Mention", value=role.mention)
        embed.add_field(name=f"Hoisted?", value=role.hoist)
        embed.add_field(name=f"Position", value=role.position)
        embed.add_field(name=f"Members w/ role", value=len(role.members))
        embed.add_field(name="Created at", value=role.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        await ctx.send(embed=embed)

    @commands.command()
    async def membercount(self, ctx, guild: discord.Guild = None):
        guild = ctx.author.guild
        embed = discord.Embed(color=guild.owner.color, timestamp=ctx.message.created_at)
        embed.set_footer(text="Member count at")
        embed.set_author(name=f"{guild.name}'s Member Count - NFrealbot", icon_url=guild.icon_url)
        embed.add_field(name="All Members", value=len(guild.members))
        embed.add_field(name="Humans", value=len(list(filter(lambda m: not m.bot, ctx.guild.members))))
        embed.add_field(name="Bots", value=len(list(filter(lambda m: m.bot, ctx.guild.members))))
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        embed = discord.Embed(title=f"{member.name}'s avatar", color=member.color, timestamp=ctx.message.created_at)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def credits(self, ctx):
      embed = discord.Embed(title=f"Credits", color=0x36393e, timestamp=ctx.message.created_at)
      embed.add_field(name="Developer", value="<@374771579164426240>")
      embed.add_field(name="Avatar Artist", value="<@541104541274210345>")
      await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(info(bot))