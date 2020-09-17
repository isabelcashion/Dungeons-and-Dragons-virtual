class Survey(object):
    survey_questions = ['What is your name?',
                       'What is your age?',
                       'Where do you live?',]
    def __init__(self):
        self.question_number = 0
        self.survey_in_progress = False
        self.user = None

    def next_question(self):
        question_to_ask = self.survey_questions[self.question_number]
        self.question_number = self.question_number + 1
        if self.question_number > 2:
            self.question_number = 0
            self.survey_in_progress = False
        return question_to_ask

    def start_survey(self, user_who_started_survey):
        if not self.survey_in_progress:
            self.user = user_who_started_survey
            self.survey_in_progress = True
            print(f'{user_who_started_survey} started a survey')
    
bot_survey_memory = Survey()    

@client.command()
async def survey(ctx):
    #bot_survey_memory.start_survey(ctx.message.author)
    #await ctx.send(bot_survey_memory.next_question())
    #await ctx.send('Use the command: .answer to send back your answer.')
    
    # Create the embed
    # survey_embed = discord.Embed(title="Profile", 
    #                              description="This is the details you have provided in the survey", 
    #                              color=0x3615c4)
    # add user's name and avatar
    # import shelve
    # db = shelve.open('test_store.db')
    # record = db[ctx.message.author]
                                  #  r, icon_url="https://cdn.statically.io/gh/connectedblue/pylearn/0d90038e/images/hangman.png")

    # survey_embed.add_field(name="Age", value="14", inline=False)

    
    # survey_embed.add_field(name="Location", value="Shrimp town", inline=True)
    
    # # send the embed back to the user
    #await ctx.send(embed=survey_embed)
    
    
    db = shelve.open('test_store.db')
    
    user = str(ctx.message.author)
    record = db[user]
    age = record['Age']

    await ctx.send(f"Hello {user} you are {age} years old")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f'message from {message.author} who said {message.content} ')
    # process message to see if the author has a survey running

    
    if bot_survey_memory.user is not None and bot_survey_memory.user == message.author:
        await message.channel.send(f'Your answer is: {message.content}')
        await message.channel.send(bot_survey_memory.next_question())
    await client.process_commands(message)