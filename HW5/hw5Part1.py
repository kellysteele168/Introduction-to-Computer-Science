'''
This program uses two function to print five random moves for the trainer and five random probabilities. It then creates a list of trues and falses and randomly selectes an item in said list five times.
Kelly Steele 3/8/2018
'''

import random

def move_trainer(): #chooses a random direction to move the trainer and random probability
    directions=['N','E','S','W']
    direction_choice= random.choice(directions)
    value=random.random()
    print("Directions: {}\nSelected {}, value {:.2f}".format(directions,direction_choice,value))
   
def throw_pokeball(num_false, num_true): #creates lists of trues and falses, and randomly selects an item
    boolean=[]
    for i in range(num_false):#add amount of falses to list
        boolean.append(False)
    for i in range(num_true): #add amount of trues to list
        boolean.append(True)
    boolean_choice=random.choice(boolean)# randomly select true or false from the list
    print("Booleans: {}\nSelected {}".format(boolean,boolean_choice))#prints the list and the random selection
    
    
#asks user for inputs
grid_size=int(input("Enter the integer grid size => "))
print(grid_size)
num_false=int(input("Enter the integer number of Falses => "))
print(num_false)
num_true=int(input("Enter the integer number of Trues => "))
print(num_true)

#sets seed based on grid size
seed_value=10*grid_size+grid_size
random.seed(seed_value)
print("Setting seed to {}".format(seed_value))

#uses for loop to run move_trainer function five times
for i in range(5):
    move_trainer()
    
#uses for loop to run throw_pokemon function five times
for i in range(5):
    throw_pokeball(num_false,num_true)

