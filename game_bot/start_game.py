from decorator import decorator

game_flow = {
    'start': [
              ('connect_to', 'demo_q1'),
              ],
    'demo_q1': [
              ('connect_to', 'demo_q1'),
              ],
  }

# @game_start decorator
@decorator
async def start_game(f, 
                     initial_state='start', 
                     game_flow=game_flow, 
                     custom_help = {},
                     *args, **kwargs):
  self = args[0]
  ctx = args[1]
  message = ctx.message
  self.custom_game_help = custom_help
  self.game_flow[f.__name__] = game_flow
  state, paused = self.users.start_game(ctx.message.author.id, f.__name__, initial_state)
  if len(paused)>0:
    await ctx.send(f'The following games for {ctx.message.author} have been paused: {paused}')
  
  if state.new_game:
      await ctx.send(f'{f.__name__} started with {ctx.message.author}')
  else:
    await ctx.send(f'{f.__name__} restarted with {ctx.message.author}')
  
  # run the initial welcome or resume logic
  kwargs['state'] = state
  response = f(self,message, state)
  
  await self.send_response(message.channel, response)
  # do the first action in the list
  state.new_game = False
  await self.execute_game_flow(ctx.message, state)


@decorator
def wait_for_player_response(f, *args, **kwargs):
  response = (True, f(*args, **kwargs))
  return(response)