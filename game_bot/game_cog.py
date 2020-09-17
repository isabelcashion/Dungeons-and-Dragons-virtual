from textwrap import dedent
import discord
from discord.ext import commands

from . import wait_for_player_response

class GameCog(commands.Cog):

  game_command_prefix = ''

  built_in_game_help = {
          'help': 'help',
          'pause': 'pause', 
          'quit': 'quit',
  }
  custom_game_help = {}

  def __init__(self, client):
    self.client = client
    self.users = self.client._users
    self.game_flow = {}
  
  @commands.Cog.listener()
  async def on_message(self, message):
    
    state = self.users.get_active_game(message.author.id)
    
    if state is None:
      return
    
    # In game help commands processed first
    help_commands = self.__help_commands()
    if message.content in help_commands:
      response = getattr(self, help_commands[message.content])(message, state)
      await self.send_response(message.channel,response)
      return
    
    # if it's not a bot command, treat the message as part of the
    # gameflow
    if not message.content.startswith('.'):
      state.current_turn += 1
      await self.execute_game_flow(message, state)
      
  async def execute_game_flow(self, message, state):
      loop_count = 0
      while True:
        # Make sure we don't loop forever
        loop_count +=1
        if loop_count>50:
          raise RunTimeError('Logic is not exiting - check flow')
          break

        # The next state is a method name on this object
        response = self.do_next_game_action(message, state)
        
        # Stop executing loop when the response from the
        # next game action is a tuple of
        # the form (True/False, message).  Send the message if
        # true but break anyway.
        # Two ways a flow can end:
        #    either a function is decorated with @wait_for_player_response
        #    or, an end state is specified (end() defined below)
        if isinstance(response, tuple) and len(response)==2:
          if response[0]:
            await self.send_response(message.channel,response[1])
          break
        
        # Otherwise just send the response and stay in loop
        await self.send_response(message.channel,response)

  @staticmethod
  async def send_response(channel,response):
    if response in [None, True, False]: return
    if isinstance(response, discord.Embed):
      await channel.send(embed=response)
    elif isinstance(response, dict):
      await channel.send(**response)
    else:
      await channel.send(dedent(response))

  @staticmethod
  def disappearing_response(content, delete_after):
    if isinstance(content, discord.Embed):
      response = {'embed': content}
    else:
      response = {'content': dedent(content)}
    response['delete_after'] = delete_after

    return response

  @staticmethod
  def make_embed(title='', description='', colour=0x3615c4,
                 author=None, icon=None, thumbnail=None, footer=None,
                 fields=None):

    embed=discord.Embed(title=title, description=description, color=colour)

    author_params = {}
    if author is not None:
      author_params['name'] = author
    if icon is not None:
      author_params['icon_url'] = icon
    if len(author_params)>0:
      embed.set_author(**author_params)

    if thumbnail is not None:
      embed.set_thumbnail(url=icon)
    
    if fields is not None:
      for f in fields:
        embed.add_field(**f)
    
    if footer is not None:
      embed.set_footer(text=footer)
    
    return embed

  def __help_commands(self):
    builtin = {self.game_command_prefix+c:self.built_in_game_help[c] \
                   for c in self.built_in_game_help.keys()}
    builtin.update({self.game_command_prefix+c:self.custom_game_help[c] \
                   for c in self.custom_game_help.keys()})
    return builtin

  # Builtin game commands
  def help(self, message, state):
    """Shows this help message"""
    response = f'In game help for {state.game}:\n\n'
    
    commands = self.__help_commands()
    width = max([len(c) for c in commands.keys()]) +2
    fmt = "{{cmd:{width}}}{{help}}\n".format(width=width)
    for cmd, func in commands.items():
      response += fmt.format(cmd=cmd,help=getattr(self,func).__doc__)

    response = "```" + response + "```"
    return response

  def quit(self, message, state):
    """Stop playing"""
    self.custom_game_help = {}
    self.users.remove_game(state.user, state.game)
    return f'{message.author.name} no longer playing {state.game}'

  def pause(self, message, state):
    """Pause playing"""
    state.active = False
    self.custom_game_help = {}
    return f'{message.author.name} has paused the {state.game}.  Type .{state.game} to resume'

  def connect_to(self, message, state):
    return True

  def otherwise(self, message, state):
    return True


  def do_next_game_action(self, message, state):
    response = None
    for exit_logic, next_state in self.game_flow[state.game][state.current_state]:
      move_on = getattr(self, exit_logic)(message, state)
      if move_on:
        response = getattr(self, next_state)(message, state)
        state.current_state = next_state
        break
    return response

  @wait_for_player_response
  def demo_q1(self, message, state):
    return (f'{message.author.name} is playing {state.game} and is on turn {state.current_turn}')

  def end(self, message, state):
    return((False, self.quit(message, state)))
  

  @commands.group(invoke_without_command=True)
  async def my_games(self,ctx):
    """Shows any games in progress"""
    games = self.users.get_all_games(ctx.message.author.id)

    if games is None or games == []:
      await ctx.send(f'No games in progress for {ctx.message.author.name}')
      return
    
    active = [g.game for g in games if g.active]
    inactive = [g.game for g in games if not g.active]
    
    active = [g.game for g in games if g.active]
    inactive = ','.join([g.game for g in games if not g.active])

    active = [g.game for g in games if g.active]
    inactive = ', '.join([g.game for g in games if not g.active])
    response = f'Paused Games for {ctx.message.author.name}: {inactive}'
    if len(active)==1:
      if response != '': response += ' and '
      response += f'game {active[0]} is currently active'
    await ctx.send(response)