import random
from discord.ext import commands
from game_bot import start_game, wait_for_player_response

maths_game_flow = {
'start':                [
                          ('connect_to', 'ask_maths_question')
                        ],
'ask_maths_question':   [
                          ('connect_to', 'check_maths_answer')
                        ],
'check_maths_answer':   [
                          ('is_maths_game_over', 'maths_score' ),
                          ('otherwise', 'ask_maths_question'),
                        ],
'maths_score':          [
                          ('connect_to', 'end')
                        ],
}

maths_custom_help = {'clue': 'maths_clue'}

class MathsGame(object):

  @commands.group(invoke_without_command=True)
  @start_game(game_flow = maths_game_flow, custom_help = maths_custom_help)
  def mathsfun(self,message, state=None):
    """Maths quiz"""
    state.current_state = 'start'

    if state.new_game == True:
      response = f"""
                  Welcome to some maths questions {message.author.name}!
                  I'll ask you five questions and give your score at the end
                  """
      state.question = 0
    else:
      response = f"""
                  Welcome back {message.author.name}!
                  Your score is {state.score} and this is question {state.question}
                  """
      state.question = state.question - 1
    
    return response

  @wait_for_player_response
  def ask_maths_question(self, message, state):
    state.number1 = random.randint(1,50)
    state.number2 = random.randint(1,50)
    state.question = state.question + 1
    response = f"What is {state.number1} plus {state.number2}?"
    return response

  def check_maths_answer(self, message, state):
    answer = str(state.number1 + state.number2)
    if message.content == answer:
      response = "Correct"
      state.score = state.score + 1
    else:
      response = f"Wrong.  It's {answer}."
    return response
  
  def is_maths_game_over(self, message, state):
    if state.question == 5:
      return True
    else:
      return False
  
  def maths_score(self, message, state):
    response = f"Game over.  You scored {state.score}" 
    return response

  def maths_clue(self, message, state):
    """Gives a range for the answer"""
    answer = state.number1 + state.number2
    neg = random.randint(1,5)
    pos = random.randint(2,7)
    response = f"Answer is between {answer-neg} and {answer+pos}"
    return response  
    