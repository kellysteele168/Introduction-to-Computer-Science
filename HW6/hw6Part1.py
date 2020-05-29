'''
This program takes a list of words and first checks if a word is in a dictionary. If not, various functions are applied in order to attempt to make a word in the dictionary.
Kelly Steele 3/29/2018
'''

def found(word): #checks to see if a given word is already in the dictionary
    f=False #used to return if word is not found
    if (i in dictionary_list)==True:
        f=True
    return f
def drop(word): #checks to see if droping a letter results in a word that is in the dictionary
    found=False
    d=[False,''] #returned if word is not found
    length=len(word)
    for i in range(0,length): #iterates through each letter
        new=word
        drop_word=new[:i]+new[(i+1):] #breaks word at i 
        if (drop_word in dictionary_list)==True: #checks if dictionary
            d=[True, drop_word]
            break #breaks to return first word found
    return d
def swap(word): #checks to see if swaping two adjacent letters results in a word in the dicitonary
    s=[False,''] #used to return if a word is not found
    for i in range(1,len(word)): #iterates through all letters except zero and swaps with preceding letter
        new=word
        if i==1: #creating new words
            swap_word=new[i]+new[i-1]+new[i+1:]
        else:
            swap_word=new[0:i-1]+new[i]+new[i-1]+new[i+1:]
        if (swap_word in dictionary_list)==True: #checks if in dictionary
            s=[True,swap_word]
            break #breaks to return first swapped letter
    return s
    
def replace(word): #replaced each letter in the word to see if that results in a word in the dictionary
    r=[False,''] #set to false to return if not found
    letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'y', 'z' ] #used to pick letters to swap   
    for i in range(0,len(word)): #iterates through each letter in a wrod
        for j in letters: #iterates through each letter in letter list
            replace_word=word[:i]+j+word[i+1:]  #breaks and replaced old letters with new letters
            if (replace_word in dictionary_list)==True: #checks if in dicitonary
                r=[True,replace_word]
                break #breaks to return first word found
    return r

dictionary_file=input("Dictionary file => ") #inputing, opening, and reading dictionary file
print(dictionary_file)
dictionary_open=open(dictionary_file)
dictionary_read=dictionary_open.readlines()
dictionary_list=set()
for i in dictionary_read:
    i=i[:-1]
    dictionary_list.add(i)


input_file=input("Input file => ") #inputing, opening, and reading list of words
print(input_file)
input_open=open(input_file)
input_read=input_open.readlines()
input_list=[]
for i in input_read:
    i=i[:-1]
    input_list.append(i)
 
    
for i in input_list:#checking each word with each functions
    f=found(i)
    d=drop(i)
    s=swap(i)
    r=replace(i)
    #printing first results for each word
    if f==True:
        print("{:15s} -> {:15s} :FOUND".format(i,i))
    elif d[0]==True:
        print("{:15s} -> {:15s} :DROP".format(i,d[1]))
    elif s[0]==True:
        print("{:15s} -> {:15s} :SWAP".format(i,s[1]))
    elif r[0]==True:
        print("{:15s} -> {:15s} :REPLACE".format(i,r[1]))
    else:
        print("{:15s} -> {:15s} :NO MATCH".format(i,i))