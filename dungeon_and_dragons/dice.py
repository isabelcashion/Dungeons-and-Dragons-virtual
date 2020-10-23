import random

class dice(object):
  def __init__(self, num_sides, colour='red'):
    self.num_sides = num_sides
    self.colour = colour

  # how many dice will be rolled

    

  def roll(self):
    
    thrown_number = random.randint(1,self.num_sides) 
    
    return thrown_number


# create three instances of class dice

# one is called d4 and it has four sides initialised
d4 = dice(4, 'yellow')

# one is called d8 and it has eight sides initialised
d8 = dice(8, 'blue')

d12 = dice(12, 'green')

#check



print(f'object d4 of class dice has {d4.num_sides} sides and the colour is {d4.colour}')
print(f'object d8 of class dice has {d8.num_sides} sides and the colour is {d8.colour}')

amount_of_dice = int(input("How many dice do you want to roll? Please type here"))

d4_running_total = 0
for t in range(1,amount_of_dice + 1):
  roll = d4.roll()
  d4_running_total = d4_running_total + roll 
  print(f'Roll number {t} of dice d4 and get {roll}.  The running total of all dice rolled so far is {d4_running_total}')

print('d4 total is {d4_running_total}')

for t in range(1,7):
  print(f'I roll dice d8 and get {d8.roll()}')


"""


print( thrown_number + amount_of_dice)

"""



