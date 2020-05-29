word=input("Word => ")
print(word)
columns=input("#columns => ")
print(columns)

rows=input("#rows => ")
print(rows)

print("Your word is: "+ str(word)+"\n")

print("(a)")
printrowa=("*** "*int(columns)+"\n")
print(printrowa*int(rows))

print("(b)")
columnb=int(columns)//int(2)
rowb=int(rows)//int(2)
print((int(columns)*"*** "+"\n")*(int(rowb)-1)+(int(columns)*"*** "))
print(int(columnb)*"*** "+"CS1 "+int(columnb)*"*** ")
print((int(columns)*"*** "+"\n")*(int(rowb)-1)+(int(columns)*"*** "))

print("\n"+"(c)")
columnc=(int(columns)-3)
print(int(columnb)*"*** "+" ^  "+int(columnb)*"*** ")
print(((int(columns)-3)//2)*"*** "+" /  ***  \  "+((int(columns)-3)//2)*"*** ")
 
print((((int(columns)-3)//2)*"*** "+" |  ***  |  "+((int(columns)-3)//2)*"*** "+"\n")*int(rowsc)+((int(columns)-3)//2)*"*** "+" |  CS1  |  "+((int(columns)-3)//2)*"*** "+"\n"+(((int(columns)-3)//2)*"*** "+" |  ***  |  "+((int(columns)-3)//2)*"*** "+"\n")*int(rowsc)+((int(columns)-3)//2)*"*** "+" \  ***  /  "+((int(columns)-3)//2)*"*** ")
print(int(columnb)*"*** "+" v  "+int(columnb)*"*** ")
