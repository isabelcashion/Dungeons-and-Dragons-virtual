import discord
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

vanish_game_flow = {
    'start': [
              ('connect_to', 'embed_test'),
              ],
    'embed_test': [
              ('connect_to', 'disappear'),
              ],
    'disappear': [
              ('connect_to', 'end'),
              ],
  }


hangman_image = "https://cdn.statically.io/gh/connectedblue/pylearn/0d90038e/images/hangman.png"
hangman_template = {
  'title': 'Hangman', 
  'description': 'Play hangman with me',
  'colour': 0x3615c4,
  'icon': hangman_image,
  'footer': "(c) 2020",
}


class OtherGames(object):
  
  @commands.group(invoke_without_command=True)
  @start_game(game_flow = vanish_game_flow)
  def vanish(self,message, state=None):
    """A game that just disappears for no reason"""
    return None

  def embed_test(self, message, state):
    embed = self.make_embed(**hangman_template,
                            author=message.author.name,
                            thumbnail=hangman_image,
            fields=[
              {
                  'name': "last letter guessed", 
                  'value': "Y",
                  'inline': False
              },
              {
                  'name': "Word to guess", 
                  'value': "\- D D - - E",
                  'inline': True
              },
              ])

    return self.disappearing_response(embed, 15)

  def disappear(self, message, state):
    return self.disappearing_response("This will disappear soon", 10) 

