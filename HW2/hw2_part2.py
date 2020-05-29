'''


#takes day length in seconds and converts it to hours, minutes, and seconds
def day_length(seconds):
    minutes=(seconds//60)
    seconds=seconds%60
    hours=(minutes//60)
    minutes=minutes%60
    return hours,minutes,seconds
#takes day length in hours, minutes and seconds and converts them into seconds
def time_to_seconds(hours, minutes, seconds):
    total_seconds=hours*60*60+minutes*60+seconds
    return total_seconds
#calculates years until the current day length in seconds becomes a certain day length in seconds
def calculated_years(sec_new_day,sec_current_day, sec_change_years):
    years_to_pass=((sec_new_day-sec_current_day)//sec_change_years)+2018
    return years_to_pass

#current day length
current_length=time_to_seconds(23,56,4)
print("The current length of a day is "+str(current_length)+" seconds.")

#day length input
day_x=int(input("Enter the desired day length in seconds => "))
print(str(day_x)+"\n")

#second per year
sec_per_year=6*60*60/900000000

#conversions
hours, minutes, seconds=day_length(day_x)
years_to_day_x=calculated_years(day_x,current_length,sec_per_year)


print(str(day_x)+ " seconds is a day length of "+str(hours)+" hours "+str(minutes)+" minutes and "+str(seconds)+" seconds.")
print("A day change rate of 6 hours every 900000000 years, ")
print("represents {:.6f}".format(sec_per_year),"seconds per year.")
print("A day length of "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds,"+"\n"+"Would be in year {:d}".format(years_to_day_x))
'''
#takes day length in seconds and converts it to hours, minutes, and seconds
def day_length(seconds):
    minutes=(seconds//60)
    seconds=seconds%60
    hours=(minutes//60)
    minutes=minutes%60
    return hours,minutes,seconds
#takes day length in hours, minutes and seconds and converts them into seconds
def time_to_seconds(hours, minutes, seconds):
    total_seconds=hours*60*60+minutes*60+seconds
    return total_seconds
#calculates years until the current day length in seconds becomes a certain day length in seconds
def calculated_years(sec_new_day,sec_current_day, sec_change_years):
    sec_change_years*=900000000
    years_to_pass=(sec_new_day-sec_current_day)/+2018
    years_to_pass = years_to_pass//900000000
    return years_to_pass

#current day length
current_length=time_to_seconds(23,56,4)
print("The current length of a day is "+str(current_length)+" seconds.")

#day length input
day_x=int(input("Enter the desired day length in seconds => "))
print(str(day_x)+"\n")

#second per year
sec_per_year=6*60*60/900000000

#conversions
hours, minutes, seconds=day_length(day_x)
years_to_day_x=calculated_years(day_x,current_length,sec_per_year)


print(str(day_x)+ " seconds is a day length of "+str(hours)+" hours "+str(minutes)+" minutes and "+str(seconds)+" seconds.")
print("A day change rate of 6 hours every 900000000 years, ")
print("represents {:.6f}".format(sec_per_year),"seconds per year.")
print("A day length of "+str(hours)+" hours, "+str(minutes)+" minutes and "+str(seconds)+" seconds,"+"\n"+"Would be in year "+str(round(years_to_day_x)))
