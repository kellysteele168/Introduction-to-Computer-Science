'''
This program takes a list of words and first checks if a word is in a dictionary. If not, various functions are applied in order to attempt to make words in a dictionary. The top corrections are printed.
Kelly Steele 4/12/2018
'''

def found(word): #checks to see if a given word is already in the dictionary
    f=False #used to return if word is not found
    if (i in dictionary_list)==True:
        f=True
    return f

def drop(word): #checks to see if droping a letter results in a word that is in the dictionary
    length=len(word)
    for i in range(0,length): #iterates through each letter
        new=word
        drop_word=new[:i]+new[(i+1):] #breaks word at i 
        if ((drop_word in dictionary_list)==True) and ((drop_word in possible_word)==False): #checks if dictionary
            possible_word.append(drop_word) #adds to possible word list
            
def insert(word): #inserts letters throughout the word to make a new word
    for i in range(0,len(word)+1): #for each space including before and after word
        for j in letters: #each letter in alphabet is used
            word_list=list(word) #creates list to alter word
            word_list.insert(i,j) #inserts letter at location
            insert_word=''.join(word_list) #combines list into new word
            if ((insert_word in dictionary_list)==True) and ((insert_word in possible_word)==False): #checks if in dictionary
                possible_word.append(insert_word) #adds to possible word list
 
def swap(word): #checks to see if swaping two adjacent letters results in a word in the dicitonary
    for i in range(1,len(word)): #iterates through all letters except zero and swaps with preceding letter
        new=word
        if i==1: #creating new words
            swap_word=new[i]+new[i-1]+new[i+1:]
        else:
            swap_word=new[0:i-1]+new[i]+new[i-1]+new[i+1:]
        if ((swap_word in dictionary_list)==True) and ((swap_word in possible_word)==False): #checks if in dictionary
            possible_word.append(swap_word)#adds to possible word list
    
def replace(word): #replaced each letter in the word to see if that results in a word in the dictionary 
    for i in range(0,len(word)): #iterates through each letter in a word
        for j in keyboard_dict[word[i]]: #iterates through each letter in letter list
            replace_word=word[:i]+j+word[i+1:]  #breaks and replaced old letters with new letters
            if ((replace_word in dictionary_list)==True) and ((replace_word in possible_word)==False): #checks if in dicitonary
                possible_word.append(replace_word) #adds to possible word list

dictionary_file=input("Dictionary file => ") #inputing, opening, and reading dictionary file
print(dictionary_file)
dictionary_open=open(dictionary_file)
dictionary_read=dictionary_open.readlines()
dictionary_list=dict()
for i in dictionary_read:
    i=i[:-1]
    i=i.split(',')
    dictionary_list[i[0]]=i[1]

input_file=input("Input file => ") #inputing, opening, and reading list of words
print(input_file)
input_open=open(input_file)
input_read=input_open.readlines()
input_list=[]
for i in input_read:
    i=i[:-1]
    input_list.append(i)

keyboard_file=input("Keyboard file => ") #creating dictionary with definitions as possible substitues for a letter
print(keyboard_file)
keyboard_open=open(keyboard_file)
keyboard_read=keyboard_open.readlines()
keyboard_dict=dict()
keyboard_list=[]
for i in keyboard_read:
    i=i[:-1]
    car_list=i.split(' ')
    keyboard_dict[car_list[0]]=set()
    for i in range(0,len(car_list)):
        if i!=0:
            keyboard_dict[car_list[0]].add(car_list[i])
    
 

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
'w', 'y', 'z' ]
    
for i in input_list:#checking each word with each functions
    i=i.strip()
    possible_word=[] #tracks all possible corrections for word
    how_many=0 #used to see how many options for corrections
    f=found(i) #checks if original word is in dictionary
    
    if f==False: #if word is not found, al functions are run to determine other possibilities
        d=drop(i)
        s=swap(i)
        ins=insert(i)
        r=replace(i)
        
    if len(possible_word)==1: #if only one word is found as a correction
        how_many=1 #used for print statements
        most_likely1=possible_word[0]
        
    elif len(possible_word)==2:#if two words are found as corrections
        how_many=2 #used for print statements
        if float(dictionary_list[possible_word[0]])>float(dictionary_list[possible_word[1]]): #checking to see most probable option and second most probable option
            most_likely1=possible_word[0]
            most_likely2=possible_word[1]
        elif float(dictionary_list[possible_word[0]])<float(dictionary_list[possible_word[1]]): #checking for most probable option and second most probable option
            most_likely1=possible_word[1]
            most_likely2=possible_word[0]     
        elif possible_word[0]>possible_word[1]: #if likelyhood same, then alphabetical order checked
            most_likely1=possible_word[0]
            most_likely2=possible_word[1]
        elif possible_word[0]<possible_word[1]:#if likelyhood same, then alphabetical order checked
            most_likely1=possible_word[1]
            most_likely2=possible_word[0]   
            
    elif len(possible_word)>2: #if more than two words are found as correction
        
        how_many=3 #used for print statements
        most_likely_val1=-1 #starting value helps to choose first item regardless of value
        most_likely1='none' #remembers most likely word
        for x in possible_word: #iterates through possible word list 
            if float(dictionary_list[x])>most_likely_val1: #if x prob greater than saved prob
                most_likely1=x #store new word
                most_likely_val1=float(dictionary_list[x]) #store new value
            elif float(dictionary_list[x])==most_likely_val1: #if probabilies equal then order checked
                if most_likely1<x:
                    most_likely1=x
        possible_word.remove(most_likely1) #top word removed
       
        #process repeated for second and third most popular word
        most_likely_val2=-1
        most_likely2='none'
        for x in possible_word:
            if float(dictionary_list[x])>most_likely_val2:
                most_likely2=x
                most_likely_val2=float(dictionary_list[x])
                
            elif float(dictionary_list[x])==most_likely_val2:
                if most_likely2<x:
                    most_likely2=x
        possible_word.remove(most_likely2)            
        most_likely_val3=-1
        most_likely3='none'
        for x in possible_word:
            if float(dictionary_list[x])>most_likely_val3:
                most_likely3=x
                most_likely_val3=float(dictionary_list[x])
            elif float(dictionary_list[x])==most_likely_val3:
                if most_likely3<x:
                    most_likely3=x
        possible_word.remove(most_likely3)
        
        
        
    #printing first results for each word
    if f==True: #if original word found
        print("{:15s} -> {:15s} :FOUND".format(i,i))
    elif how_many==1:#if only one word is found
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely1,1))
    elif how_many==2: #if two words are found
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely1,1))  
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely2,2))
    elif how_many==3: #if three words are chosen to print
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely1,1))  
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely2,2))        
        print("{:15s} -> {:15s} :MATCH {}".format(i,most_likely3,3)) 
    elif len(possible_word)==0: #if no matched are found for the original word
        print("{:15s} -> {:15s} :NO MATCH".format(i,i))
        
