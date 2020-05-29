'''
This program sees if change can be made for a given price and given selection of coins. If possible the change is found.
Kelly Steele 2/22/18
'''
#import functions
import hw3_util

#inputing the file
file=(input("Enter the coin file name => "))
print(file)
coins= hw3_util.read_change(file)

#input the item cost
cost=int(input("Enter the item cost in cents (0-100) => "))
print(cost)

#define variables and lists
change_cents=100-cost
change_modify=change_cents
return_change=[]

#counting amounts of avaiable coins
halfdollars=coins.count(50)
quarters=coins.count(25)
dimes=coins.count(10)
nickles=coins.count(5)
pennies=coins.count(1)

#each sees if there is avaible change within each coin type to append
if halfdollars>0:
    if change_modify>50:
        x=change_modify//50
        if x<=halfdollars:
            change_modify=change_modify%50
            return_change+=([50]*x)
        else:
            change_modify=change_modify-halfdollars*50
            return_change+=([50]*halfdollars)
  
if quarters>0:
    if change_modify>25:
        x=change_modify//25
        if x<=quarters:
            change_modify=change_modify%25
            return_change+=([25]*x)
        else:
            change_modify=change_modify-quarters*25
            return_change+=([25]*quarters)
            
if dimes>0:
    if change_modify>10:
        x=change_modify//10
        if x<=dimes:
            change_modify=change_modify%10
            return_change+=([10]*x)
        else:
            change_modify=change_modify-dimes*10
            return_change+=([10]*dimes)
           
        
if nickles>0:
    if change_modify>5:
        x=change_modify//5
        if x<=nickles:
            change_modify=change_modify%5
            return_change+=([5]*x)
        else:
            change_modify=change_modify-nickles*5
            return_change+=([5]*nickles)
            
if pennies>0:
    if change_modify>1:
        x=change_modify//1
        if x<=pennies:
            change_modify=change_modify%1
            return_change+=([1]*x)
        else:
            change_modify=change_modify-pennies*1
            return_change+=([5]*nickles)
            
#prints statement if there is proper change            
if change_modify==0:
    halfdollaz=return_change.count(50)
    quarterz=return_change.count(25)
    dimez=return_change.count(10)
    nicklez=return_change.count(5)
    penniez=return_change.count(1)
    print("\nI have the following coins:")
    print(coins)
    print("Change from $1.00 is {:d} cents".format(change_cents))
    print("{:d} Half Dollars, {:d} Quarters, {:d} Dimes, {:d} Nickels, {:d} Pennies".format(halfdollaz,quarterz,dimez,nicklez,penniez))
    
#prints statement if there is not proper change   
else:
    print("\nI have the following coins:")
    print(coins)
    print("Change from $1.00 is {:d} cents".format(change_cents))
    print("I cannot make change with my current coins.")
    print("I need an additional {:d} cents.".format(change_modify))