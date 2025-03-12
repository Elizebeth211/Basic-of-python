# update a list
l = [10, 20,30, 40,50]
l[2] = 400
print(l)

#pop the value from the list
r = l.pop()
print(l,r)

#Remove an element from the list
l.remove (20)
print (l) #Output: [10, 30, 40, 50]

l.clear()
print (l)

#sort
numbers = [5, 2, 9, 1, 7]
numbers.sort() 
print(numbers)
numbers.sort(reverse=True)  # Sorts in descending order
print(numbers)
numbers.reverse()
print(numbers)



#sorted
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sorted(numbers)  # Creates a new sorted list
print(sorted_numbers)  # Output: [1, 2, 5, 7, 9]
print(numbers)  # Original list remains unchanged


#check index
l = [10 ,20, 30, 40, 50]
print (l.index(30))


#Check occurence using count()
l = [10 ,20, 30, 40, 40, 40,]
print (l.index(40))
