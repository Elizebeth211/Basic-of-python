#string built-in python
text = "hello world"
print(text.upper())      # Output: HELLO WORLD
print(text.lower())      # Output: hello world 
print(text.title())      # Output: Hello World 
print(text.capitalize()) # Output: Hello world  

print(text.isupper())


#splits and join
fruit = "Orange, Apple,Banana"
text = fruit.split(",")
print(text)

text1 = (" ").join(fruit)
print(text1)

text = (" ").join(fruit)
print(text)


#maketrans and tanslate
s1 = "abcd"
s2 = "1234"
s3 = "Python sample sting abcd"
table = str.maketrans(s1, s2)
result = s3.translate(table)
print(result)



# index, find and rfind
text = "Python is fun and fun"
print(text.index("is"))  # Output: 7 
print(text.find("are"))   # Output: 7
print(text.rfind("fun"))  # Output: 18 

#removing space using strip()
s = "*******This is a string*****"
text = s.strip("T")
print(text)

#to put string at the center
s = "Python"
s1 = s.center(20, "*")
print(s1)

#Put string to left hand side
s = "Python"
s1 = s.ljust(20, "*")
print(s1)


#replace a string
s = "Python, Java, Html"
s1 = s.replace ("Html","HTML")
print(s1)











