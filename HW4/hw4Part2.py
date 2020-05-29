'''
This program uses zip codes to return locations, and locations to return zip codes. It also can calculated the distance between two zip codes.
Kelly Steele 2/28/18
'''
#import data and modules
import hw4_util
import math
zipcodes=hw4_util.read_zip_all()

#this function using a list of all zip codes, and a city and state to find the zip codes of the specific location
def zip_by_location(zip_codes,location):
    city=location[0].title()
    state=location[1].upper()
    zip_for_location=[]
    place=-1
    for i in zipcodes:
        place+=1
        in_list=i.count(city)+i.count(state)
        if in_list==2:
            zip_for_location.append(zip_codes[place])
    return zip_for_location, city,state    

#this function uses a list of all zip codes and a specific zip code to return the location information including geographic coordinates, city, and state
def location_by_zip(zip_codes, code):
    place_in_list=zip_codes.index(code)
    location=zipcodes[place_in_list]
    return location

#this function properly formats the latitude and longitude in terms of degrees, minutes, and seconds
def lat_lon(number):
    number=abs(number)
    degrees=int(number)
    degree_remainder=number-degrees
    minutes=int(degree_remainder*60)
    minutes_remainder=(degree_remainder*60)-minutes
    seconds=minutes_remainder*60
    lat_or_lon=('{:03d}\xb0{:02d}\'{:.2f}"'.format(degrees,minutes,seconds))
    return lat_or_lon

#creates list of all zip codes
zip_codes=[]
for i in zipcodes:
    zip_codes.append(i[0])
#while loop continues to ask for prompts until end is entered
command='empty'
new_line=1
while command != 'end':
    if new_line==0:
        print()
    #asks for  task
    command=input("Command ('loc', 'zip', 'dist', 'end') => ")
    print(command)
    command=command.lower()
    #if loc is entered the user then enters a zip code to return the location information
    if command=='loc':
        zip_lookup=input("Enter a ZIP code to lookup => ")
        print(zip_lookup)
        if zip_lookup in zip_codes:
            location=location_by_zip(zip_codes,zip_lookup)
            city=location[3]
            state=location[4]
            county=location[5]
            if location[1]>0:
                lat_let='N'
            else:
                lat_let='S'
            if location[2]>0:
                lon_let='E'
            else:
                lon_let='W'
            latitude=lat_lon(location[1])
            longitude=lat_lon(location[2])
            print("ZIP code {} is in {}, {}, {} county,\n\tcoordinates: ({}{},{}{})".format(zip_lookup,city,state,county,latitude,lat_let,longitude,lon_let))
        else:
            print("Invalid or unknown ZIP code")   
    #if zip is entered, the city and state are then asked for to determine all zips wiithin the area
    elif command=='zip':
        city_lookup=input("Enter a city name to lookup => ")
        print(city_lookup)
        state_lookup=input("Enter the state name to lookup => ")
        print(state_lookup)
        location=[city_lookup,state_lookup]
        zip_for_location, city, state=zip_by_location(zip_codes,location)
        zip_int=[]
        for i in zip_for_location:
            i=int(i)
            zip_int.append(i)
        if len(zip_for_location)>0:
            print("The following ZIP code(s) found for {}, {}: {}".format(city,state,str(zip_int)[1:-1]))
        else:
            print("No ZIP code found for {}, {}".format(city,state))    
    #if dist is entered the user enters two zip codes and the distance between them is calculated using the longitude and latitude
    elif command=='dist':
        first=input("Enter the first ZIP code => ")
        print(first)
        second=input("Enter the second ZIP code => ")
        print(second)
        if first in zip_codes and second in zip_codes:
            location_1=location_by_zip(zip_codes,first)
            lat_1=location_1[1]
            lon_1=location_1[2]
            location_2=location_by_zip(zip_codes,second)
            lat_2=location_2[1]
            lon_2=location_2[2]
            delta_lat=lat_2-lat_1
            delta_lon=lon_2-lon_1
            r=3959.191
            a=((math.sin(math.radians(delta_lat/2)))**2)+math.cos(math.radians(lat_1))*math.cos(math.radians(lat_2))*((math.sin(math.radians(delta_lon/2)))**2)
            d=2*r*math.asin(a**.5)
            print("The distance between {} and {} is {:.2f} miles".format(first,second,d))
        else:
            print("The distance between {} and {} cannot be determined".format(first,second))
    #if end is entered the loop stops running
    elif command=='end':
        print("\nDone")
    #used if the program does not recognize the command
    else:
        print("Invalid command, ignoring")  
    new_line=0
