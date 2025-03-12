#If we have two set we can perform union intersection difference operation
#S1 = {10, 20, 30, 40, 50, 60}
#S2 = {50, 60, 70, 80, 90}

#It will return all the element but should be unique
#S3 = S1.union(S2)
#print(S3)# Output: {70, 40, 10, 80, 50, 20, 90, 60, 30}

#Intersection will give the value that is common to both the set
#S3 = S1.intersection(S2)
#print(S3) # Output:{50, 60}

#difference will return only the element that is present in set one and not set 2
#S3 = S1.difference(S2)
#print(S3) # Output: {40, 10, 20, 30}

#The semmetric_difference will return the value that is uniques to both the set
#S3 = S1.symmetric_difference(S2)
#print(S3) # Output: {70, 40, 10, 80, 20, 90, 30}

#print(S1)
#S1.update(S2)
#print(S1) # Output:{70, 40, 10, 80, 50, 20, 90, 60, 30}

#S1.intersection_update(S2)
#print(S1)# Output:{70, 80, 50, 90, 60}

#S1.symmetric_difference_update(S2)
#print(S1)

#S1.difference_update(S2)
#print(S1)# Output:{20, 40, 10, 30}


#Set1 = {10, 20, 30, 40, 50, 60}
#Set2 = {40, 50, 60, 70, 80, 90}
#print(Set2.issubset(Set1)) # Output: True
#print(Set1.issuperset(Set2))



#L1 = [10, 20, 30, 40, 50, 60]
#L2 = [40, 50, 60, 70, 80, 90]

#print(type(L2))
#S1 = set(L1)
#S2 = set(L2)

#S3 = S1.union(S2)
#print(S3)# Output:{70, 40, 10, 80, 50, 20, 90, 60, 30}

#L3 = list(S3)
#print(L3)# Output:[70, 40, 10, 80, 50, 20, 90, 60, 30]


#L3.sort()
#print(L3)# Output:[10, 20, 30, 40, 50, 60, 70, 80, 90]

S = {10, 20, 30, 40, 50}
#r = S.pop()
#print(S,r)# Output:{20, 40, 10, 30} 50

#S.remove(40)
#print(S) # Output:{50, 20, 10, 30}

#S.discard(1000)
#print(S)# Output:{50, 20, 40, 10, 30}

S.clear()
print(S)# Output:set()




















