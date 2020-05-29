'''
This program determines the name at a given rank and year. It then finds the percent of names in the year for the name, as well as the percent in the year before and year after.
Kelly Steele 2/22/18
'''

#import name data
import math
import read_names
read_names.read_from_file("top_names_1880_to_2014.txt")

#finds percentanges and total counts for names
def find_percent(year,rank):
    i_f=249
    total_count_female=0
    while i_f>-1:
        total_count_female=total_count_female+female_counts[i_f]
        i_f=i_f-1
    name_count_female=female_counts[input_ranking]
    percent_female=name_count_female/total_count_female*100
    i_m=249
    total_count_male=0
    while i_m>-1:
        total_count_male=total_count_male+male_counts[i_m]
        i_m=i_m-1
    name_count_male=male_counts[input_ranking] 
    percent_male=name_count_male/total_count_male*100
    return name_count_female, total_count_female, percent_female, name_count_male, total_count_male, percent_male
def stars(percent):
    stars=math.trunc(percent/.1)
    return stars
def year_after_percent(current_year,name,gender):
    year_after=current_year+1
    names,counts=read_names.top_in_year(year_after,gender)
    if (name in names)==True:
        index_name=(names.index(name))
        sum_count=sum(counts)
        count_name=counts[index_name]
        percent=count_name/sum_count
        percent=percent*100
    else:
        percent=0
    return percent, year_after
def year_before_percent(current_year,name,gender):
    year_before=current_year-1
    names,counts=read_names.top_in_year(year_before,gender)
    if (name in names)==True:
        index_name=(names.index(name))
        sum_count=sum(counts)
        count_name=counts[index_name]
        percent=count_name/sum_count
        percent=percent*100
    else:
        percent=0
    return percent, year_before

#input year and rank
base_year=int(input("Enter a year (1881-2013) => "))
print(base_year)
rank=int(input("Enter a rank (1-250) => "))
print(rank)

#checking to see if year and rank are in range
if (base_year<1881) or (base_year>2013) or (rank<1) or (rank>250):
    print(str(base_year)+" is not in the range 1881-2013 or "+str(rank)+" is not in the range 1-250")
else:
    #creates the correct ranking ot use for the data
    input_ranking=rank-1
    
    #reads base_year for names and counts
    (female_names,female_counts) = read_names.top_in_year(base_year, 'f') 
    (male_names,male_counts) = read_names.top_in_year(base_year, 'M')
    the_female_name=female_names[input_ranking]
    the_male_name=male_names[input_ranking]
    
    #main rank 
    main_cf,main_tf,main_pf,main_cm,main_tm,main_pm=find_percent(base_year,input_ranking)
    main_stars_female=stars(main_pf)
    main_stars_male=stars(main_pm)
    
    
    #find percent for before and after year
    before_pf,year_before=year_before_percent(base_year,the_female_name,'f')
    after_pf,year_after=year_after_percent(base_year,the_female_name,'f')
    before_pm,year_before=year_before_percent(base_year,the_male_name,'m')
    after_pm,year_after=year_after_percent(base_year,the_male_name,'m')   
    
    before_stars_female=stars(before_pf)
    after_stars_female=stars(after_pf)
    before_stars_male=stars(before_pm)
    after_stars_male=stars(after_pm)
    
    print("The rank "+str(rank)+" most popular female name in "+str(base_year)+" is "+the_female_name)
    print("\t"+str(main_cf)+" out of "+ str(main_tf)+" or {:.2f}%".format(main_pf))
    print("Histogram for "+female_names[input_ranking])
    print(str(year_before)+":\t"+(before_stars_female)*"*"+"\t"+"({:.2f}%)".format(before_pf))
    print(str(base_year)+":\t"+(main_stars_female)*"*"+"\t"+"({:.2f}%)".format(main_pf))
    print(str(year_after)+":\t"+(after_stars_female)*"*"+"\t"+"({:.2f}%)".format(after_pf))
    
    print("\nThe rank "+str(rank)+" most popular male name in "+str(base_year)+" is "+the_male_name)
    print("\t"+str(main_cm)+" out of "+ str(main_tm)+" or {:.2f}%".format(main_pm))
    print("Histogram for "+male_names[input_ranking])
    print(str(year_before)+":\t"+(before_stars_male)*"*"+"\t"+"({:.2f}%)".format(before_pm))
    print(str(base_year)+":\t"+(main_stars_male)*"*"+"\t"+"({:.2f}%)".format(main_pm))
    print(str(year_after)+":\t"+(after_stars_male)*"*"+"\t"+"({:.2f}%)".format(after_pm))
