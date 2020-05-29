#counting happy words
def number_happy(sentence):
    laugh=sentence.count("laugh")
    happiness=sentence.count("happiness")
    love=sentence.count("love")
    excellent=sentence.count("excellent")
    good=sentence.count("good")
    smile=sentence.count("smile")
    positive=int(laugh)+int(happiness)+int(love)+int(excellent)+int(good)+int(smile)
    return positive
#counting sad words
def number_sad(sentence):
    bad=sentence.count("bad")
    sad=sentence.count("sad")
    terrible=sentence.count("terrible")
    horrible=sentence.count("horrible")
    problem=sentence.count("problem")
    hate=sentence.count("hate")
    negative=int(bad)+int(sad)+int(terrible)+int(horrible)+int(problem)+int(hate)
    return negative
    

input_sentence=input("Enter a sentence => ")
print(input_sentence)

#making input lowercase
lower=input_sentence.lower()

#implementing functions
positive=number_happy(lower)
negative=number_sad(lower)

#determine sentiment
if int(positive)>int(negative):
    sentiment="happy"
elif int(negative)>int(positive):
    sentiment="sad"
else:
    sentiment="neutral"


print("Sentiment: "+int(positive)*"+"+int(negative)*"-")
print("This is a "+sentiment+ " sentence.")