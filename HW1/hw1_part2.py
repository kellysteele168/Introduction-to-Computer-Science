firstword=input("First => ")
print(firstword)
secondword=input("Second => ")
print(secondword)

phrase=firstword+"_"+secondword
length=len(phrase)
print("Example variable names")
lowercase=phrase.lower()
print("Lower case: "+ str(lowercase) +" "+ str(length))
upper=phrase.upper()
print("For constants: "+ str(upper)+" "+ str(length))

camel=firstword.title()+secondword.title()
camellength=len(camel)
print("Camel case: "+ camel+ " "+ str(camellength))

sysvar="_"+str(firstword.lower())+"_"+str(secondword.lower())
sysvarlength=len(sysvar)
print("System variables: "+ str(sysvar) + " "+str(sysvarlength))

sillyvar=str(firstword)+"_"+str(secondword)
silly1=sillyvar.replace("l","_")
silly2=silly1.replace("o","_")
silly3=silly2.replace("L","_")
silly4=silly3.replace("O","_")
print("Silly variable: "+ str(silly4)+" ")

