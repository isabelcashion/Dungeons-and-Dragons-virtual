from discord.ext import commands
import discord

class admin(commands.Cog):
  
  def __init__(self, client):
    self.client = client


  # @commands.event
  # async def on_member_join(self,member):
  #     print(f'{member} has joined the server')



  # @commands.event
  # async def on_member_remove(self,member):
  #     print(f'{member} has left the server')


  @commands.command(pass_context=True)
  async def join(self,ctx):
      channel = ctx.message.author.voice.voice_channel
      await commands.join_voice_channel(channel)

  @commands.command(pass_context = True)
  async def leave(self,ctx):
    """this makes shrimp_bot leave the voice channel"""
    server = ctx.message.server
    voice_client = commands.voice_client_in(server)
    await voice_client.disconnect()

  # @commands.command(pass_context =True)
  # async def purge(self,ctx,amount=10):
  #     """bulk delete 10 messages from above"""
  #     channel = ctx.message.channel
  #     messages = []
  #     await for message in self.client.logs_from(channel, limit=amount):
  #         messages.append(message)
  #     await client.delete_messages(messages)




  #kick and ban user

  @commands.command()
  async def kick(self,ctx, member : discord.Member, *, reason = None):
    """kicks your member... WARNING: you can only use this command if you have given shrimp_bot admin and you have admin yourself"""
    await member.kick(reason=reason)

  @commands.command()
  async def ban(self,ctx, member : discord.Member, *, reason = None):
    """bans your member... WARNING: you can only use this command if you have given shrimp_bot admin and you have admin yourself"""
    await member.ban(reason=reason)

def setup(client):
  client.add_cog(admin(client))