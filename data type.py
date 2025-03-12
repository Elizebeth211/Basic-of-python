x = 10      # An integer variable
name = "John"  # A string variable
is_python_fun = True  # A boolean variable
print (x)
print (name)
print (is_python_fun)

age = 25
print(type(age))  # Output: <class 'int'>

weight = 20.99
print(type(weight)) # Output: <class 'float'>

message = "Hello, World!"
print(type(message))  # Output: <class 'str'>

is_it_raining = True
print(type(is_it_raining))  # Output: <class 'bool'>

#list
l=[10,20,30,40,50]
print((l))
print(id(l))
l.append(60)
print((l))
print(id(l))
print(type(l))

#tuple
l = (10,20,30,30,40,50)
print(l)
print(type(l))
for index,value in enumerate(l):
    print(index,value)
for t in enumerate (l):
    print(t)
for t in enumerate (l):
    print(t[0])

#Dictionary
# Dictionary of student details
student = {
    "name": "Isabel",
    "age": 5,
    "grade": "A"
}
print(student)  # Output: {'name': 'Isabel', 'age': 25, 'grade': 'A'}
print(type(student))  # Output: <class 'dict'>

student['grade']= 'B'
print(student)  # Output: {'name': 'Isabel', 'age': 25, 'grade': 'B'}
print(student["name"]) # Output: Isabel
print(student.get("Rollno."))# Output: None
print(student.get("Rollno.",'Rollno. doesnot exist'))# Output: Rollno. doesnot exist
print(student.setdefault("Rollno.")) # Output: None
print(student) # Output:{'name': 'Isabel', 'age': 5, 'grade': 'B', 'Rollno.': None}
print(student.keys()) # Output: dict_keys(['name', 'age', 'grade', 'Rollno.'])
print(student.values()) # Output: dict_values(['Isabel', 5, 'B', None])
print(student.items())# Output: dict_items([('name', 'Isabel'), ('age', 5), ('grade', 'B'), ('Rollno.', None)])

#set
s = {10,20,30,30,40,50}
print(type(s))
print(s)# Output:{50, 20, 40, 10, 30}
s.add(60)
print (s) # Output:{50, 20, 40, 10, 60, 30}

#complex
z = 3 + 4j  # Complex number (3 is the real part, 4j is the imaginary part)
print(z)  # Output: (3+4j)
print(type(z))  # Output: <class 'complex'>

#Convert one data type to another
x = float(10)  # Converts int to float
print(x)  # Output: 10.0
print(type(x))

y = str (7)  # Converts string to float
print(y)  # Output: 3.14
print(type(y))

#Convert one data type to another
l = [10,20,30]
t = tuple(l)
print(t)
