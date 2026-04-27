# i = 1

# while i <=10:
#     print(i)
#     i += 1


# for i in range(1,11):
#     print(i)

# i = 1
# for i in range(0, 5):
#     print(i)
# else:
#     print("Done!!!!")    

# n = int(input("Enter a number: "))

# sum = 0

# for i in range(1, n+1):
#     sum += i
# print("the sum is:", sum)

# n = int(input("Enter a number: "))

# for i in range(1,11):
#     pro = n * i
#     print(n, "X", i, "=",pro)
# input_number = 6
# for i in range(1,input_number + 1):
#     print(f"Current Number is : {i} and the cube is {i**3}")

n = 123
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)