# Write the code that replaces the first character of a string given to you or received from the user without changing the first character, with a "?" sign.

text=input("Enter the word")
new_text=text[0]

for i in range(1,len(text)):
    if text[i]==text[0]:
        new_text+="?"
    else:
        new_text+=text[i]
print(new_text)