import math

#calcutes volume of sphere using radius
def find_volume_sphere(radius):
    volume_sphere=(4/3)*math.pi*radius**3
    return volume_sphere
#calcuates volume of cube  
def find_volume_cube(side):
    volume_cube=side**3
    return volume_cube
  
#input radius  
radius=input("Enter the gum ball radius (in.) => ")
print(radius)
radius=float(radius)
#input sales
sales=int(input("Enter the weekly sales => "))
print(str(sales)+"\n")


fill=math.ceil(sales*1.25)
side=math.ceil(fill**(1/3))
edge_length=side*2*radius
extra=side**3-fill
volume_cube=find_volume_cube(edge_length)
volume_sphere=find_volume_sphere(radius)
wasted_target=volume_cube-volume_sphere*fill
wasted_fill=volume_cube-volume_sphere*(side**3)




print("The machine needs to hold "+str(side)+" gum balls along each edge.")
print("Total edge length is {0:.2f}".format(edge_length)+" inches.")
print("Target sales were "+str(fill)+", but the machine will hold "+str(extra)+ " extra gum balls.")
print("Wasted space is {0:.2f}".format(wasted_target)+ " cubic inches with the target number of gum balls,"+"\n"+"or {0:.2f}".format(wasted_fill) +" cubic inches if you fill up the machine.")
