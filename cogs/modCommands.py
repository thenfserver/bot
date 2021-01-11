import discord, random
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

from utils import bench_data

class mod(commands.Cog):
    mod_role = None

    def __init__(self, client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def ranmember(self, ctx, guild = discord.Guild):
      guild = ctx.author.guild
      await ctx.send(f"{(random.choice(guild.members)).mention}")


    @commands.command()
    @has_permissions(manage_messages=True)
    async def respond(self, ctx, member: discord.Member=None, *, context):
      embed = discord.Embed(title="Message Received", description=context, color=discord.Color.red())
      embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
      embed.set_footer(text=f"{ctx.author} | {ctx.author.id}")
      await member.send(embed=embed)
      embed=discord.Embed(title="Message Sent", description=context, color=discord.Color.green())
      embed.set_author(name=f"Sent to {member}", icon_url=member.avatar_url)
      embed.set_footer(text=f"Sent by {ctx.author} | {ctx.author.id}")
      await ctx.send(embed=embed)
      
    @commands.command()
    @has_permissions(manage_messages=True)
    async def fakeleave(self, ctx, member: discord.Member):
      fo = open("utils/lists/leaves.txt")
      LeaveMessage = fo.readlines()
      await ctx.send(f"**{member}** {random.choice(LeaveMessage)}")
      await ctx.message.delete()

    @commands.command()
    @has_permissions(manage_messages=True)
    async def svs(self, ctx):
      fo = open("utils/lists/songs.txt", "r")
      song = fo.readlines()
      embed = discord.Embed(title="Song vs Song", description=f"{(random.choice(song))} - 🗝️ \n{(random.choice(song))} - 🛒", color=0x36393e)
      msg = await ctx.send("<@&728677564943695943>", embed=embed)
      reactions = ['🗝️', '🛒']
      for emoji in reactions[:len(reactions)]:
          await msg.add_reaction(emoji)
      await ctx.message.delete()
      embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!svs` in {ctx.channel.mention}")
      embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
      channel = self.client.get_channel(736051087412559954)
      await channel.send(embed=embed)

    @commands.command()
    @has_permissions(manage_messages=True)
    async def qotd(self, ctx):
      fo = open("utils/lists/quotes.txt", "r")
      quote = fo.readlines()
      embed = discord.Embed(title="Quote of the Day", description=f"{(random.choice(quote))}",color=0x36393e)
      await ctx.send("<@&727892627399245906>", embed=embed)
      await ctx.message.delete()
      embed = discord.Embed(color=discord.Color.blue(), description=f"Used `nf!qotd` in {ctx.channel.mention}")
      embed.set_author(name=f"{ctx.author}", icon_url=ctx.author.avatar_url)
      channel = self.client.get_channel(736051087412559954)
      await channel.send(embed=embed)

    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=f"No reason given."):
        if not member:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!kick - NFrealbot")
            embed.add_field(name="Description:", value="Kicks the specifed user.", inline=False)
            embed.add_field(name="Usage:", value="nf!kick {member} (reason)", inline=False)
            embed.add_field(name="Example:", value="nf!kick bread#7620 3 warnings \nnf!kick 374771579164426240 3 warnings\nnf!kick @bread 3 warnings")
            await ctx.send(embed=embed)
            return
        else:
            await member.kick(reason=reason)
            await ctx.send(f"Kicked {member} for {reason}")

            channel = self.client.get_channel(736051087412559954)
            await channel.send(f":boot: **{member}** (`{member.id}`) was kicked by **{ctx.author}** (`{ctx.author.id}`) for `{reason}`.")

    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=f"No reason given."):
        if not member:
            embed = discord.Embed(color=discord.Color.default())
            embed.set_author(name="nf!ban - NFrealbot")
            embed.add_field(name="Description:", value="Bans the specifed user.", inline=False)
            embed.add_field(name="Usage:", value="nf!ban {member} (reason)", inline=False)
            embed.add_field(name="Example:", value="nf!ban bread#7620 3 warnings \nnf!ban 374771579164426240 3 warnings\nnf!ban @bread 3 warnings")
            await ctx.send(embed=embed)
            return
        else:
            await member.ban(reason=reason)
            await ctx.send(f"banned {member} for {reason}.")
            channel = self.client.get_channel(736051087412559954)
            await channel.send(f":rotating_light: **{member}** (`{member.id}`) was banned by **{ctx.author}** (`{ctx.author.id})` for `{reason}`")

    @commands.command(aliases=['purge', 'prune'])
    @has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        member = ctx.author
        await ctx.message.delete()
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"Deleted {amount} messages requested by {member} ({member.id})")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def mute(self, ctx, member: discord.Member):
        muterole = discord.utils.get(member.guild.roles, name="Muted")
        await member.add_roles(muterole)
        await ctx.send(f"Muted {member.mention}!")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: discord.Member):
        muterole = discord.utils.get(member.guild.roles, name="Muted")
        await member.remove_roles(muterole)
        await ctx.send(f"Unmuted {member.mention}!")

    @commands.command()
    @has_permissions(manage_roles=True)
    async def role(self, ctx, mode, member: discord.Member = None, *, role: discord.Role = None):
      if mode == "add":
        await member.add_roles(role)
        await ctx.send(f"Gave {member.name}#{member.discriminator} `{role}`.")
      elif mode == "remove":
        await member.remove_roles(role)
        await ctx.send(f"Removed {member.name}#{member.discriminator} `{role}`.")

    @commands.command()
    @has_permissions(manage_messages=True)
    async def change(self, ctx, mode=None, benchedUser: discord.Member=None, *, reason="No reason specifed."):
      benchrole = discord.utils.get(benchedUser.guild.roles, name="Socially Popular")
      benchchannel = self.client.get_channel(774116269733576724)
      if mode == None:
        embed = discord.Embed(description="Description: \n  Sends the specifed user to the bench.\nUsage: nf!change {add or remove} (user) [reason]")
      if mode == "add":
        await benchedUser.add_roles(benchrole)
        await ctx.send(f"Added {benchedUser} to <#774116269733576724>.")
        await benchchannel.send(f"Hello, {benchedUser.mention}. \n\nYou have been sent to the bench by a staff member of this server. This basically means you can't chat with anyone in this server until you get removed. To get removed from this channel, tell us why we shouldn't mute/kick/ban you.\n\nThe reason you were sent to the bench: `{reason}`")
        bench_data.add(benchedUser)

        try:
          bench_data.add(benchedUser)
        except:
          pass
      elif mode == "remove":
        await benchedUser.remove_roles(benchrole)
        bench_data.remove(benchedUser)
        await ctx.send(f"Removed {benchedUser} from <#774116269733576724>.")

def setup(bot):
    bot.add_cog(mod(bot))