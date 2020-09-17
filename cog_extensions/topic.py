from discord.ext import commands
import discord
import random 

class topic(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command()
  async def topic(self,ctx,*,question):
    """.topic shrimp brings back a question"""
    question = ['What is lying in your fridge at the moment?',
                'Would you prefer fries or ceaser salad right now?',
                'How often do you eat salad as a full meal?',
                'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                'What would you do to quickly get someone’s attention?',
                'I am a person who thinks a lot, what about you?',
                'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                'What would you do to quickly get someone’s attention?',
                'I am a person who thinks a lot, what about you?',
                'If you had 30 secs of everyone’s attention, what is the one thing you will say?',
                'What would you do to quickly get someone’s attention?',
                'I am a person who thinks a lot, what about you?',
                'What is your wildest fantasy?',
                'Do you ever hit nostalgia and if yes, how do you feel?',
                'Which is the one superpower you wish you had?',
                'Did you always want to be in the profession you are in?',
                'Which is the biggest fear of your life?',
                'Is there anything you would try that you never tried before?',
                'Have you ever planned a conspiracy to stalk someone?',
                'Would you rather chose to be alone and alive or with a group of people and die?',
                'Have you ever been chased by police?',
                'Why are you acting weird for the past few days?',
                'I heard you have a big secret to tell your partner, is that true?',
                'What will you prefer? To be buried or cremated?',
                'Which one do you want to know- When will you die or how will you die?',
                'What is the weather like?',
                'Watch Star Wars or Star Trek? Harry Potter or The Lord of the Rings? Use whichever movies you find most relevant.',
                'Read on a Kindle or paperback book? This question is a starter for many possible conversations on reading, favorite books, technology, libraries, bookstores and more!',
                'Go to a play or musical?',
                'Go to the theater or a movie?',
                'Wear jeans or chinos?',
                'Have a Margarita or Pina Colada?',
                'Drink a glass of Guinness or Fat Tire?',
                'Drink coffee or beer?',
                'Crash with friends or stay in a hotel?',
                'Visit Europe or Mexico?',
                'Vacation in Hawaii or Alaska, and why?',
                'Choose a free trip or money? This may tell you whether the person values experiences over dollars.',
                'Stay in a hotel or an Airbnb home?',
                'Go skiing or snowboading?',
                'Travel by plane, train, or automobile?',
                'Enjoy a houseboat or speed boat?',
                'Go climbing or zip lining?',
                'Hike or bike?',
                'Go to a comedy club or dance club?',
                'Have a night out or evening in?',
                'Watch TV or read a book?',
                'Go canoeing or waterskiing?',
                'Camp in an RV or stay in a tent?',
                'Use Facebook or Twitter?',
                'Use iPhone or Android phone?'
                'Win the lottery or find your perfect job?',
                'Swim in a pool or the ocean? Salt water and waves crashing on the beach or temperature controlled, lovely water all year round.',
                'Travel by sailboat or cruise ship?',
                'Watch sports or play sports?',
                'Play dodgeball or kickball?',]           
    await ctx.send(f'Question: {random.choice(question)}')

def setup(client):
  client.add_cog(topic(client))