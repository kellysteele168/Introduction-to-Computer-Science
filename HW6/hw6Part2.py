'''
This program searches for beasts from an inputed title and compares them with beasts from other movies.
Kelly Steele 3/29/2018
'''

import textwrap #import textwrap to break up lines

lower_title='go' #used to start while loop

while lower_title != 'stop': #ends when users inputs stop 
    title=input("Enter a title (stop to end) => ") #user inputs title or portion of title
    print(title)    
    lower_title=title.lower() #changes case to compare
    file=open('titles.txt') #opening file to find other titles
    similar_set=set() #set stores titles with similar beasts
    all_beasts=set() #set stores all beasts found in other titles
    movie='Not Found' #used to track if elif statement should be entered
    found=False
    if lower_title!='stop':
        for x in file.readlines(): #reading movies in file to check if input title exists
            try_movie=x.strip().split('|')
            if lower_title in try_movie[0].lower() and found==False:
                movie=try_movie
                title_beasts_set=set((movie[1:])) #creates set of beasts in from inputed title
                found=True
        if movie=='Not Found':
            print('\nThis title is not found!')

        elif movie!='Not Found':
            file=open('titles.txt')
            for y in file.readlines(): #reads each line to compare beasts
                other=y.strip().split('|')
                other_beasts=set((other[1:]))
                if other[0]!=movie[0]: 
                    shared_set=other_beasts.intersection(title_beasts_set) #creates shared set
                    all_beasts=all_beasts.union(other_beasts)#adds new beasts to all beast set
                    if len(shared_set)>0:
                        similar_set.add(other[0]) #if commmon beasts adds to shared set
        
      
            unique_set=title_beasts_set.difference(all_beasts) #finds beasts unique to input title
            
            #converting sets to sorted strings
            title_beasts_list=list(title_beasts_set)
            title_beasts_list.sort()
            title_beasts_string=', '.join(title_beasts_list)
            
            similar_list=list(similar_set)
            similar_list.sort()
            similar_string=', '.join(similar_list)
            
            unique_list=list(unique_set)
            unique_list.sort()
            unique_string=', '.join(unique_list)            
            
            #formating lines
            par1=('Found the following title: {}'.format(movie[0]))
            par2=('Beasts in this title: {}'.format(title_beasts_string))
            par3=('Other titles containing beasts in common: {}'.format(similar_string))
            par4=('Beasts appearing only in this title: {}'.format(unique_string))
            
            #using textwrap to create paragraphs
            line2=textwrap.wrap(par2)
            line3=textwrap.wrap(par3)
            line4=textwrap.wrap(par4)
            
            #printing lines
            print('')
            print(par1)
            for line in line2:
                print(line)
            print('')
            for line in line3:
                print(line)
            print('')
            for line in line4:
                print(line)
            print('')
            
            

