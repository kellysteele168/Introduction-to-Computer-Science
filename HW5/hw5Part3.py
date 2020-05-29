'''
The program moves the trainer for a given amount of simulations to determine various statistics. Additionally, it tracks a grid of caught and missed pokemon.
Kelly Steele 3/8/2018
'''

import random
def move_trainer(move): # function moves trainer 
    directions=['N','E','S','W']
    direction_choice= random.choice(directions)#choose random direction
    value=random.random()#random probability
    
    #change location based on direction chosen
    if direction_choice=='N':
        loc=(move[1][0]-1,move[1][1]) 
    elif direction_choice=='S':
        loc=(move[1][0]+1,move[1][1]) 
    elif direction_choice=='E':
        loc=(move[1][0],move[1][1]+1) 
    else:
        loc=(move[1][0],move[1][1]-1)
        
    return (value,loc) #returns the random value and the new location
   
def throw_pokeball(throw): #determins whether or not a pokemon is caught based on the number of trues and falses
    boolean=[]
    #list of trues and falses are generated
    for i in range(throw[0]):
        boolean.append('False')
    for i in range(throw[1]):
        boolean.append('True')    
    choice=random.choice(boolean) #random item chosen
    return choice #decision returned

def run_one_simulation(grid): #moves trainer, sees pokemon, misses pokemon, and catches pokemon for one simulation
    throw=(3,1) #sets trues and falses
    turn=0 #tracks turn for simulation
    move=[0,(size//2,size//2)] #sets starting place
    while (move[1][0])!=0 and int(move[1][0])!=size-1 and int(move[1][1])!=0 and int(move[1][1])!=size-1: #continues actions until trainer reaches edge
        move=move_trainer(move) #runs move_trainer function
        turn+=1 #tracks turns
        if move[0]<p: #if random probability is less than user input for loop is entered
            catch=throw_pokeball(throw) #rungs throw_pokemon function
            if catch=='True':
                grid[move[1][0]][move[1][1]]+=1 #increases net for that place if pokemon is caught
                throw=(throw[0],throw[1]+1) #increases trues if pokemon is caught
            else:
                grid[move[1][0]] [move[1][1]]-=1  #decreases net for that place if pokemon is missed
    return turn,grid        

#input statements
size=int(input("Enter the integer grid size => "))
print(size)
p=(input("Enter a probability (0.0 - 1.0) => "))
print(p)
p=float(p)
simulations=int(input("Enter the number of simulations to run => "))
print(simulations)
print('')

#random seed 
seed_value=10*size+size
random.seed(seed_value)

#creates grid where columns=size and rows=size
grid=[]
for i in range(size):
    grid.append([0]*size)


turn_list=[] #keeps track of the turn amount in each simulation


while simulations>0: #run run_one_simulation function while simulations is greater than 0
    turn,grid=run_one_simulation(grid)
    turn_list.append(turn) #appends amount of turns to list to be used for print statements
    simulations-=1
    

turn_average=sum(turn_list)/len(turn_list) #calculates the average turns using the turn list  

#finds max and min over all simulations
max_turn=max(turn_list)
min_turn=min(turn_list)

#finds specific simulation for max and min turns
max_index=turn_list.index(max_turn)
min_index=turn_list.index(min_turn)

#creates a list of values from grid to determine the best and worst net
values_in_grid=[]
for i in grid:
    for j in i:
        values_in_grid.append(j)       
best_net=max(values_in_grid)
worst_net=min(values_in_grid)

#formats grid for printing
for i in grid:
    list=[]
    for j in i:
        x=('{:5d}'.format(j))
        list.append(x)
    print(*list,sep='')



#print statements
print("Average number of turns in a simulation was {:.2f}".format(turn_average))
print("Maximum number of turns was {:d} in simulation {:d}".format(max_turn,max_index+1))
print("Minimum number of turns was {:d} in simulation {:d}".format(min_turn,min_index+1))
print("Best net missed pokemon versus caught pokemon is {:d}".format(best_net))
print("Worst net missed pokemon versus caught pokemon is {:d}".format(worst_net))
