# Write the code that replaces the first character of a string given to you or received from the user without changing the first character, with a "?" sign.



x=input("enter a word")

x_new=x.replace(x[0],"?")[1:]
print(x_new)
print (x[0] + x_new)