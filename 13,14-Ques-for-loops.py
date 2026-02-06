# 13 :- Write a Python program to find the sum of digits of a given number using a for loop.

n = input("Enter a number: ")
t = 0

for i in n:
    t += int(i)
    
print(t)

# 14 :- Write a Python program to calculate.

n = int(input("Enter a number: "))
t = 0

for i in range(1, n + 1):
a = i * i
t += a

print(t)
