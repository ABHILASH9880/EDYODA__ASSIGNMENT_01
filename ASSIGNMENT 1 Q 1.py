n = int(input("enter number of Fibonacci series"))
a = 0
b = 1 
s = 0

for x in range (n) :
    print(s,end=" ")
    s = a+b
    b = a
    a = s