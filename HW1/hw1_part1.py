Radius_of_Sun=int(input("Enter the radius of the Sun (miles) -> "))
print(Radius_of_Sun)
Radius_of_Moon=int(input("Enter the radius of the Moon (miles) -> "))
print(Radius_of_Moon)
MAXDistance_Sun_to_Earth=int(input("Enter the maximum distance to the Sun (miles) -> "))
print(MAXDistance_Sun_to_Earth)
MINDistance_Moon_to_Earth=int(input("Enter the minimum distance to the Moon (miles) -> "))
print(MINDistance_Moon_to_Earth)
Rate_Moon_away_from_Earth=float(input("Enter the rate the Moon is moving away (in/year) -> "))
print(Rate_Moon_away_from_Earth)
Distance_Moon_to_Earth=float(MAXDistance_Sun_to_Earth*(Radius_of_Moon/Radius_of_Sun))
Distance_to_Move=float(Distance_Moon_to_Earth-MINDistance_Moon_to_Earth)
In_Inches=Distance_to_Move*5280*12
Years_to_Move=int(In_Inches/Rate_Moon_away_from_Earth)
print("The Moon will have exactly the same apparent size as the Sun when it is {:.2f}".format((Distance_Moon_to_Earth)) + " miles away.")
print("The Moon will need to recede another {:.2f} ".format((Distance_to_Move)) +" miles")
print("Which will occur in "+ str(Years_to_Move) +" years at the current rate.")