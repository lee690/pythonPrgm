#DEFINING A LIST
# Create the list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))

#Accessing a list by position
# the first list postion is considered 0. Use brackets to tell python which position in th elist you want. 
print(myFruitList[0]) # apple
print(myFruitList[1]) # banana
print(myFruitList[2]) # cherry

# Changing values in a list
myFruitList[2] = "orange"
print(myFruitList)

'''
Introducing the tuple data type
Defining a tuple
The tuple is like a list, but it can’t be changed. A data type that can’t be changed after it’s created is said to be immutable. To define a tuple, you use PARENTHESIS instead of brackets
'''

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Accessing the tuple by position
print(myFinalAnswerTuple[0])
print(myFinalAnswerTuple[1])
print(myFinalAnswerTuple[2])

'''
DICTIONARY data type
A dictionary is a list with named positions (keys). Imagine that your list shows people’s favorite fruit
'''
myFavoriteFruitDictionary = {
      "Akua" : "apple",
      "Saanvi" : "banana",
      "Paulo" : "pineapple"
    }

print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary["Saanvi"])
print(myFavoriteFruitDictionary["Paulo"])