from discord.ext import commands
import discord

class commands(commands.Cog):


# commands
#client.remove_command("help")


## There was a space between @ and client on the next line
  @commands.command()
  async def commands(self,ctx):
    """shows commands"""
    author = ctx.message.author
    embed = discord.Embed(
      colour = discord.Colour.red()
    )
    # title embed here saying Commands
    embed.set_author(name='Commands')
    embed.add_field(name= '.ping', value= 'Sends back pong , have fun laying table tennis uwu!', inline=False)
    embed.add_field(name= '.Godie', value= 'to let ur anger out ;)', inline=False)
    embed.add_field(name= '.avatar @mention', value= 'shows the avatar of the person you have mentioned', inline=False)
    embed.add_field(name= '.topic shrimp', value= 'gives you a random question to start ur conversation or just answer!', inline=False)
    embed.add_field(name= '.kick', value= """this kicks members from your server, you can type a reason next to .kick @mention [reason].'

    Warning: this command only works if Shrimp_bot has permissions to kick and ban and you yourself do as well! """,
     inline=False)
    embed.add_field(name= '.ban', value= """this bans members from your server, you can type a reason next to .ban @mention [reason].
    
    Warning: this command only works if Shrimp_bot has permissions to kick and ban and you yourself do as well! """, inline=False)
    embed.add_field(name= '.commands', value= 'shows this command', inline=False)
    embed.add_field(name= '.mathsfun', value= """this plays a maths game (you can use [!help] once playing for help with the game) """,
     inline=False)
        
    embed.add_field(name= '.fruit', value= """this plays a fruit game (you can use [!help] once playing for help with the game) """,
     inline=False)
    embed.add_field(name= '.help', value= """this shows you all the extensions that have loaded in  """,
     inline=False)

    await ctx.send(embed=embed)
  #@commands.command()
  # def extensions(self,ctx):
  #   """shows extensions you can load"""
  #   embed = discord.Embed(
  #     colour = discord.Colour.red()
  #   )
  #   # title embed here saying Commands
  #   embed.set_author(name='Extensiions')
  #   embed.add_field(name= '.ping', value= 'Sends back pong , have fun laying table tennis uwu!', inline=False)
    
  #   await ctx.send(embed=embed)
    
def setup(client):
  client.add_cog(commands(client))