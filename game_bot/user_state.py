from .game_state import GameState

class UserState(object):

  def __init__(self):
    self._users = {}

  def start_game(self,user, game, initial_state):
    if user not in self._users:
      self._users[user] = {game: GameState(user, game, initial_state)}
    elif game not in self._users[user]:
      self._users[user][game] = GameState(user, game, initial_state)
    
    self._users[user][game].active = True
    paused_games = [g for g in self._users[user].keys() if g != game]
    for g in paused_games:
      self._users[user][g].active = False
    
    return self._users[user][game], paused_games

  def get_active_game(self, user):
    if user in self._users.keys(): 
      active_games = [g for g in self._users[user].values() if g.active]
      if len(active_games) > 1:
        raise ValueError("Too many active games")
      if len(active_games) == 1:
        return active_games[0]
    return None

  def get_all_games(self, user):
    if user in self._users.keys(): 
      return [g for g in self._users[user].values()]
    return None
  
  def remove_game(self, user, game):
    try:
      del self._users[user][game]
    except:
      raise KeyError(f'Cannot remove {game} for {user}')



