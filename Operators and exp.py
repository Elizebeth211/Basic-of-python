#arithmatic operator
a = 4
b = 3

print(a + b)   # Addition -> 13
print(a - b)   # Subtraction -> 7
print(a * b)   # Multiplication -> 30
print(a / b)   # Division -> 3.3333
print(a // b)  # Floor Division -> 3 (removes decimals)
print(a % b)   # Modulus (remainder) -> 1
print(a ** b)  # Exponentiation (10^3) -> 1000

#comparison operator

print(a == b)   # False (10 is not equal to 3)
print(a != b)   # True (10 is not equal to 3)
print(a > b)    # True (10 is greater than 3)
print(a < b)    # False (10 is not less than 3)
print(a >= 10)  # True (10 is equal to 10)
print(b <= 3)   # True (5 is equal to 5)


#Identity operator
print(a is b)
print(a is not b)

#Assignment operators
x = 10  
x += 5   # Same as x = x + 5
print(x)  # Output: 15

#Bitwise operators
# 3 = 011
# 4 = 100

print(a & b)  # AND -> 0
print(a | b)  # OR -> 7
print(a ^ b)  # XOR -> 7
print(~a)     # NOT -> -5
print(a << 1) # Left Shift (Multiply by 2) -> 8
print(a >> 1) # Right Shift (Divide by 2) -> 2


#Logical operators
A = True
B = False

print(A and B)  # False (Both must be True)
print(A or B)   # True (At least one is True)
print(not A)    # False (Reverses value)

#Membership operators

text = "Apple"
print("A" in text)  # True














