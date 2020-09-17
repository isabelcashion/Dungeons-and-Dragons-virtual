from datetime import datetime, timedelta

class GameState(object):
  def __init__(self, user, game, initial_state):
    self.user = user
    self.game = game
    self.active = False
    self.current_state = initial_state
    self.current_turn = 0
    self.score = 0
    self.new_game = True
    self._expiry_time = None

  def start_timer(self, time_in_seconds):
    self._expiry_time = datetime.now() + timedelta(seconds=time_in_seconds)

  def has_timer_expired(self):
    if self._expiry_time is None:
      raise ValueError('Timer not set')
    if datetime.now() < self._expiry_time:
      return False
    else:
      self._expiry_time = None
      return True