'''
This program uses a variety of inputs to make various actions with Pikachu.
Kelly Steele 2/22/18
'''
#function for moving pikachu
def move(x,y,direction):
    if direction=='E':
        if x>=20:
            x=x+20
        else:
            x=0
    elif direction=='S':
        if y<=130:
            y=y+20
        else:
            y=150
    elif direction=='W':
        if x<=130:
            x=x-20
        else:
            x=150
    else:
        if y>=20:
            y=y-20
        else:
            y=0
    return x, y
#define variables
x=75
y=75
i=10
energy=10
command_list=[]

#while loops asks for inputs and determines actions
while i>0:
    
    #ask for input
    print("Pikachu at ({:d}, {:d}) with power {:d}".format(x,y,energy))
    command=input("What does Pikachu do ('N', 'S', 'E', 'W', 'Attack', 'Rest')? ")
    print(command)
    command_list.append(command)
    input_command=command.title()
    
    #used to move pikachu
    if input_command=='N' or input_command=='S' or input_command=='E' or input_command=='W':
        if energy>=1:
            x,y=move(x,y,input_command)
            energy=energy-1
        else:
            print("Pikachu is too tired!")
            
    #used to rest pikachu 
    elif input_command=='Rest':
        energy=energy+10
        
    #used to attack with pikachu
    elif input_command=='Attack':
        if energy<5:
            print("Pffft, It's a dud ...")
            energy=0
        else:
            print("Bzzzt, Pikachu zaps its foe!")
            energy=energy-5
            
    #used to lower energy for inputs other than possible actions
    else:
        if energy>0:
            energy=energy-1
        else:
            energy=0
            print("Pikachu is too tired!")
    i=i-1

#prints final statements
print("Pikachu at ({:d}, {:d}) with power {:d}\n".format(x,y,energy))
sorted_list=sorted(command_list)
print("All commands entered:")
print(command_list)
print("All commands sorted:")
print(sorted_list)