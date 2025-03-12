#for loop

s = [10, 20, 30, 40, 50] #iterating over a list
for value in s:
    print(value)


for i in range(1, 6):  # Iterating using range from 1 to 5
    print(i)

    
for char in "Python": #iterating over a string
    print(char)

colors = ("red", "green", "blue") #iterating over a tuple
for color in colors:
    print(color)

#break and continue function in for loop
l = [10, 20, 30, 40, 50]
key = 30

for value in l:
    if value == key:
        print("Element found")
        break  # Stops the loop when key is found
    else:
        continue  # Moves to the next iteration
else:
    print("Element not found")  # Runs only if loop completes without `break`


fruits = ["apple", "banana", "cherries"]
for index, fruit in enumerate(fruits):
    print (index, fruit)
#Output
#0 apple
#1 banana
#2 cherries

x = 10

if x > 5:
    pass  # Placeholder (Does nothing but avoids an error)
else:
    print("x is small")

#while loop
x = 1
while x <= 5:
    print(x)
    x += 1  # Increment x



