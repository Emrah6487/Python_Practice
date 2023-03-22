# Write the code that replaces the first character of a string given to you or received from the user without changing the first character, with a "?" sign.

x=input("Please enter the word")

y=x[0]

for i in range(1,len(x)):
    if x[i] == x[0]:
        y+="?"
    else:
        y+=x[i]
print(y)
        


