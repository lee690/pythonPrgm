"""
Exploring the basic data tupes that are used to store numeric values
"""

print("Python has three numeric types: int, float, and complex")

'''
Creating a variable
A variable is like a labeled box that stores information. You can change the contents of the box, but the label stays the same. Here, the variable name is myValue, but will store different data types in that labeled box.
'''

#assigned an integer type of data to this variable
myValue=1
print(myValue) 
#checks the data type
print(type(myValue)) 
#remember integer is whole numbers
print(str(myValue) + " is of the data type " + str(type(myValue)))


#assigned a float type of data to this variable
myValue=3.14
print(myValue)
print(type(myValue))
#string built in function combines numbers and text
print(str(myValue) + " is of the data type " + str(type(myValue)))


#complex data type
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))


#boolean data type
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))