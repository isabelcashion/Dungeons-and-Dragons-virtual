import random
import discord
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

fruit_game_flow = {
'start':          [
                    ('connect_to', 'show_fruitbowl'),
                  ],
'show_fruitbowl': [
                    ('connect_to', 'fruit_display_timer'),
                  ],
'fruit_display_timer': [
                    ('is_timer_active', 'fruit_display_timer'),
                    ('connect_to', 'check_guess'),
                  ],
'check_guess':    [
                    ('has_game_finished', 'show_score'),
                    ('connect_to', 'guess_again'),
                  ],
'guess_again':    [
                    ('connect_to', 'check_guess'),
                  ],
'show_score':     [   
                    ('connect_to', 'end'),
                  ],
}

fruit_clues = {
  'apple': 'Gravity was discovered with one',
  'banana': 'Monkeys peel them upside down', 
  'cherries': 'Small and red with pips', 
  'peach': 'James had a giant one', 
  'watermelon': 'As big as a football',
  'grapes': "Don't wine if you can't guess", 
  'pear': "Partridge lives there", 
  'pineapple': 'You might have one on pizza',
  'kiwi':  'Fruit from down under', 
  'strawberry': "You'll find one at wimbledon",
}

all_fruit = fruit_clues.keys()

fruit_custom_help = {'clue': 'fruit_clue'}

class FruitGame(object):

  @commands.group(invoke_without_command=True)
  @start_game(game_flow = fruit_game_flow, custom_help = fruit_custom_help)
  def fruit(self,message, state=None):
    """Remember what's in the fruit bowl"""
    state.current_state = 'start'
    response = f"""
              Welcome to the fruit bowl {message.author.name}!
              Look at what's in it, and you have 10 seconds to
              remember and guess as many as you can

              """
    state.fruit = random.sample(all_fruit, 5)
    state.score = 0
    state.number_of_goes = 1
    state.number_of_goes_allowed = 6
    state.fruit_guessed = []
    return response
    

  def show_fruitbowl(self, message, state):
    response = '  '.join([':'+f+':' for f in state.fruit])
    state.start_timer(10)
    state.player_guessed_early = 0
    state.start_guessing = False
    return self.disappearing_response(response, 10)
  
  @wait_for_player_response
  def fruit_display_timer(self, message, state):
    response = None
    if state.has_timer_expired():
      state.start_guessing = True
      response = self.check_guess(message, state)
      response += "\nGuess again"
    elif state.player_guessed_early > 0:
      response = f"wait ..... it's not disappearing yet ...."
    state.player_guessed_early += 1

    return response

  def is_timer_active(self, message, state):
    if not state.start_guessing:
      return True
    return False
  
  def check_guess(self, message, state):
    guess = message.content
    if guess in state.fruit and guess not in state.fruit_guessed:
      response = f":{guess}: Correct!!"
      state.score += 2
      state.fruit_guessed.append(guess)
    elif guess in state.fruit and guess in state.fruit_guessed:
      response = f"You already guessed :{guess}:"
    else:
      response = f"Nope. {guess} is not in my bowl"
    
    state.number_of_goes += 1
    return response
  
  def has_game_finished(self, message, state):
    if state.number_of_goes > state.number_of_goes_allowed:
      return True
    if len(state.fruit) == len(state.fruit_guessed):
      return True
    return False
  
  @wait_for_player_response
  def guess_again(self, message, state):
    return "Guess another one"
  
  def show_score(self, message, state):
    response = "\n\nGame Over\n\n"
    all_fruit = '  '.join([':'+f+':' for f in state.fruit])
    fruit_not_guessed = '  '.join([':'+f+':' for f in self.unguessed_fruit(state)])
    fruit_guessed_correctly = '  '.join([':'+f+':' for f in state.fruit_guessed])
    if len(state.fruit) == len(state.fruit_guessed):
      response += "Congratulations!!! You remembered all the fruit\n"
      response += all_fruit
    elif len(state.fruit_guessed)==0:
      response += f"You didn't remember a single thing!  Here's my bowl:\n"
      response += all_fruit
    else:
      response += f"You remembered {len(state.fruit_guessed)} correctly!  {fruit_guessed_correctly}\nHere's the rest of my bowl:\n"
      response += fruit_not_guessed
    
    response += f"\nYour score is {state.score}"

    if state.score != 2* len(state.fruit_guessed):
      response += "\n(you had some points deducted because you asked for a clue)"
    
    return response

  def unguessed_fruit(self, state):
    return ([f for f in state.fruit if f not in state.fruit_guessed])

  def fruit_clue(self, message, state):
    """Gives a hint about what the fruit might be"""
    state.score += -1
    return fruit_clues[random.choice(self.unguessed_fruit(state))]

  
  