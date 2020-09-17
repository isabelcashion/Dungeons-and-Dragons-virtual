import random
import discord
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

hangman_game_flow = {
'start':          [
                    ('connect_to', 'ask_level'),
                  ],
'ask_level': [
                    ('connect_to', 'is_level_valid'),
                  ],
'is_level_valid': [
                    ('is_level_valid', 'game_setup'),
                    ('connect_to', 'wrong_level'),
                  ],
'wrong_level': [
                    ('connect_to', 'ask_level'),
                  ],
'game_setup':    [
                    ('connect_to', 'show_placeholder'),
                  ],
'show_placeholder':    [
                    ('connect_to', 'is_game_finished'),
                  ],

'is_game_finished': [
                    ('is_game_finished', 'show_hangman_score'),
                    ('connect_to', 'show_placeholder'),
                  ],



'show_hangman_score':     [   
                    ('connect_to', 'end'),
                  ],
}




hangman_custom_help = {'clue': 'hangman_clue'}

class HangmanGame(object):

  @commands.group(invoke_without_command=True)
  @start_game(game_flow = hangman_game_flow, custom_help = hangman_custom_help)
  def hangman(self,message, state=None):
    """guess the word game"""
    state.current_state = 'start'
    response = f"""
              Welcome to the Hangman {message.author.name}!
              You can use !help during the game for ingame help and advisement.
              """
    state.score = 0
    state.level= None
    state.current_go = 1
    state.letters_guessed = []
    state.guessed_correctly = False
    return response

  @wait_for_player_response
  def ask_level(self,message, state):
    response = "Which level do you want? 1, 2 or 3? " 

    return response

  def is_level_valid(self,message,state):
    # player has just entered their level
    state.level = message.content
    # make a decision if it's valid
    if state.level in ["1","2","3"]:
      return True
    else:
      return False
    
  def wrong_level(self, message,state):
    return "The level input that you have typed is invalid."

    

  def game_setup(self, message, state):
    if state.level == "1":
      state.number_of_goes_allowed = 7
      state.word_to_guess = "cool"
    else:
      state.number_of_goes_allowed = 10
      state.word_to_guess = "droplet"
    
    state.word_to_guess = list(state.word_to_guess)
    state.placeholder= list("-" *len(state.word_to_guess))

    return f"you have {state.number_of_goes_allowed} guesses"

  @wait_for_player_response
  def show_placeholder(self,message,state):
    response = f""" the word you need to guess is {state.placeholder}
    You currently on go {state.current_go} . 
    Type your letter guess!"""
    state.current_go = state.current_go + 1
    return response

  def is_game_finished(self, message, state):
    # Check each letter against the guess
    # and if correct, update the placeholder
    Guess = message.content
    
    index= 0
    while index<len(state.word_to_guess):
        if Guess == state.word_to_guess[index]:
            state.placeholder[index] = Guess
        index = index+1
    
    if state.word_to_guess == state.placeholder:
      state.guessed_correctly = True
      return True


    if state.current_go > state.number_of_goes_allowed:
      print("current goes is equal to number of goes allowed")
      return True
    else:
      print("current goes is not equal to number of goes allowed")
      return False

  def show_hangman_score(self, message, state):
    if state.guessed_correctly == True:
      return f"You guessed the word: {state.word_to_guess}"
    else:
      return f"You have finished game and didn't manage to guess the whole word here is the word {state.word_to_guess}"
