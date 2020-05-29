'''
This program defines a word as alternating if the length is at least 8, vowels and consonants alternate thorughout the word, and the vowels appear in non-decreasing alphabetical order.
Kelly Steele 2/28/18
'''

#is_alternating function determines if a word is alternating or not, and prints the corresponding statement
def is_alternating(word_real):
    word=word_real.lower()
    if len(word)>=8:
        if alternating(word)==True:
            if vowel(word)==True:
                x=True
                print("The word '{}' is alternating\n".format(word_real))
            else:
                print("The word '{}' is not alternating\n".format(word_real))
                x=False
        else:
            print("The word '{}' is not alternating\n".format(word_real))
            x=False
    else:
        print("The word '{}' is not alternating\n".format(word_real))
        x=False

#alternating function determines if leters alternate vowels and consonants
def alternating(word):
    count=0
    x=True
    consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
    vowels=['a','e','i','o','u']
    if word[0] in consonants:
        for i in word:
            placement=word.index(i)
            if (placement%2)!=0:
                if i in vowels:
                    count+=1
                else:
                    x=False
            if (placement%2)==0:
                if i in consonants:
                    count+=1
                else:
                    x=False
    elif word[0] in vowels:
        for i in word:
            placement=word.index(i)
            if (placement%2)!=0:
                if i in consonants:
                    count+=1
                else:
                    x=False
            if (placement%2)==0:
                if i in vowels:
                    count+=1
                else:
                    x=False
    else:
        x=False
    return x

#vowel function determines if the vowels appear in ascending/descending order
def vowel(word):
    x=True
    vowels=['a','e','i','o','u']
    word_vowels=[]
    for i in word:
        if i in vowels:
            word_vowels.append(i)
    count=len(word_vowels)-1
    if count>0:
        for i in word_vowels:
            current_letter=i
            current_place=word_vowels.index(i)
            vowel_loop=word_vowels[current_place:]
            for i in vowel_loop:
                if i<current_letter:
                    x=False
    return(x)
#while the loop remains true and the user inputs something. A combinations of all three functions determine if the word is alternating
loop=True
while loop==True:
    word=input("Enter a word: ")
    print(word)
    if len(word)>0:
        is_alternating(word)
    else:
        loop=False
