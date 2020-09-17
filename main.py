import os
from game_bot import BotFactory, keep_alive

keep_alive()
bot_token = os.getenv("TOKEN")
bot = BotFactory('cog_extensions', ('mini_games', 'admin', 'game_cogs'))
bot.run(bot_token)

#while for admin is in arcade
  #we wanna use that for .help command so assign to up state cognate and disord commands extension (commands.py)
