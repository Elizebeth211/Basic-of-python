#Working with math and random modules
L = [10, 20, 30, 40, 50]
#print(sum(L)) #Output:150


#print(max(L)) #Output:50

#num = 20.4
#print(round(num))

#print(dir(__builtins__)) # see entire list of builtin

#help(__builtins__) #Description of builtin

import math
#L = [0.1] * 10
#print(L)#Output:[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
#print(sum(L))

#Addition of floating point numbers
#print(math.fsum(L))#Output: 1.0

num = 15.5559
#print(math.floor(num), math.ceil(num))#Output:15 16

#print(math.sqrt(25)) # Output: 5.0
#print(math.factorial(5))# Output:120

num1 = 45.5556
print(math.modf(num1))# Output:(0.5555999999999983, 45.0)
d, i = math.modf(num1)
print(i)
print(math.pow(10,2))# Output:100.0
print(math.log(10,2))# Output:3.3219280948873626
print(math.log10(2))
print(math.log2(10))


print(math.sin(0))# Output:0.0

print(math.sin(30))# Output:-0.9880316240928618
print(math.sin(math.radians(30)))# Output:0.49999999999999994




import random
print(random.random())


L = [1, 2, 3, 4, 5]
print(random.choice(L)) 


print(random.randint(10, 100))

print(random.randrange(10, 100))


print(random.uniform(10, 20))


















