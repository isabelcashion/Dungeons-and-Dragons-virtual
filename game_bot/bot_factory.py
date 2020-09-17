from discord.ext import commands

from .user_state import UserState

class BotFactory(object):
  def __init__(self, ext_dir=None, init_ext=None):
    self.ext_dir = ext_dir
    self.init_ext = init_ext
    self.create_bot()
    self.load_initial_extensions()
  
  def create_bot(self):
    bot = commands.Bot(command_prefix='.')

    @bot.event
    async def on_ready():
      print('Logged on as {0}!'.format(bot.user))

    @bot.event
    async def on_message(message):
      if message.author == bot.user:
        return
      print(f'{message.author}: {message.content} ')
      await bot.process_commands(message)

  
    @bot.command()
    async def load(ctx, ext):
      """Load custom extension"""
      bot.load_extension(self.extension_path(ext))
    
    @bot.command()
    async def unload(ctx, ext):
      """Unload custom extension"""
      bot.unload_extension(self.extension_path(ext))

    @bot.command()
    async def reload(ctx, ext):
      """Reload custom extension"""
      bot.reload_extension(self.extension_path(ext))

    # Store user state for games
    bot._users = UserState()

    self.bot = bot
  
  def load_initial_extensions(self):
    for ext in self.init_ext:
      self.bot.load_extension(self.extension_path(ext))

  def extension_path(self, ext):
    return f'{self.ext_dir}.{ext}'
  
  def run(self, *args, **kwargs):
    return self.bot.run(*args, **kwargs)

  