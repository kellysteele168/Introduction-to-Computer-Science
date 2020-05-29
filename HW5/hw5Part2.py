'''
This program moves the trainer until he reached the edge of the board. It determines whether or not the trainer sees a pokemon and whether or not he catches it.
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


#asks user for various inputs
size=int(input("Enter the integer grid size => "))
print(size)
p=(input("Enter a probability (0.0 - 1.0) => "))
print(p)
p=float(p)


location=(size//2,size//2)#starting location
move=(0,location)#starting move includes location and probability

throw=(3,1) #initial throw has 3 falses and 1 true

#tracks turns, pokemon seen, and pokemon captured
turn=0
see=0
captured=0


#set seed
seed_value=10*size+size
random.seed(seed_value)

# while loop continues to move trainer until the edge of the grid is reached
while move[1][0]!=0 and move[1][0]!=size-1 and move[1][1]!=0 and move[1][1]!=size-1:
    move=move_trainer(move) #trainer is moved based on function
    turn+=1 #turn is increased to track
    if move[0]<p: #if the random value is greater than the user probability
        catch=throw_pokeball(throw) #throw function run
        print("Saw a pokemon at turn {}, location {}".format(turn,move[1])) #prints that pokemon was seen
        see+=1 #tracks seen pokemon
        if catch=='True': #if function results in true the pokemon is captured
            captured+=1 #tracks captured
            throw=(throw[0],throw[1]+1) #trues are increased
            print("Caught it!") 
        else: #pokemon is not caughet
            print("Missed ...")
            
print("Trainer left the field at turn {}, location {}.".format(turn,move[1]))
print("{} pokemon were seen, {} of which were captured.".format(see,captured))
      
