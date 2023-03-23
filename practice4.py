#write even and odds numbers 1-50
odds=[]
even=[]
for i in range(1,51):
    if i % 2 == 0:
        even.append(i)
    else:
        odds.append(i)
print(odds)
print(even)
#other method

x=[i for i in range(51,101) if i%2==0]
y=[i for i in range(51,101) if i%2==1]
print(x)
print(y)

#other method

print(f"even number:{[i for i in range (1,11) if i %2==0]}")
print(f"odds number:{[i for i in range (1,11) if i %2==1]}")
        

