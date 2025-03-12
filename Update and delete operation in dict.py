L1 = [1,2,3,4,5]
L2 = [6,7,8,9,10]
d = dict(zip(L1,L2))
print(d) # Output: {1: 6, 2: 7, 3: 8, 4: 9, 5: 10}


L1 = [1,2,3,4,5]
d = dict.fromkeys(L1)
print(d)# Output: {1: None, 2: None, 3: None, 4: None, 5: None}

D1 = {1:1,2:4,3:9}
D2 = {4:16,5:25,6:36}
D1.update(D2)
print(D1) # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}

r = D1.pop(2)
print(D1) # Output:{1: 1, 3: 9, 4: 16, 5: 25, 6: 36}
print(D1,r) # Output:{1: 1, 3: 9, 4: 16, 5: 25, 6: 36} 4

r = D1.popitem()
print(D1,r)# Output: {1: 1, 3: 9, 4: 16, 5: 25} (6, 36)

D1.clear()
print(D1)# Output:{}

del D1
print(D1)
