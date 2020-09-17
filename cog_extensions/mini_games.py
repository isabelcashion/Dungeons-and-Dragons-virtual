
from discord.ext import commands
import discord

class mini_games(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command()
  async def ping(self,ctx):
      await ctx.send('Pong!')



  @commands.command()
  async def Godie(self,ctx):
      await ctx.send('oki ):')


  @commands.command()
  async def avatar(self,ctx, member: discord.Member):
    """ @mention shows the avatar of the person you have mentioned"""
    show_avatar = discord.Embed(
      colour = discord.Color.purple()
    )
    show_avatar.set_image(url='{}'.format(member.avatar_url))
    await ctx.send(embed=show_avatar)
    # if no mention 
    #await ctx.send (embed=show_avatar of current member)

def setup(client):
  client.add_cog(mini_games(client))