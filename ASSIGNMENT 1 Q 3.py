list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even=0
odd=0
for i in list :
    if (i%2==0):
        even=even+1
    else:
        odd=odd+1
print("Even number in list",even)
print("Odd numbers in list",odd)