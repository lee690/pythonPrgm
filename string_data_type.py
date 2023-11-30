"""Introducing the string data type
A text file containing a logical sequence of commands is a script.
"""


#creating a var
myString = "This is a string."
#printing the variable
print(myString)

#This code outputs the data-type of the variable
print(type(myString))

#To convert the return value of type into a string, use the str() built-in function:
print(myString + " is of the data type " + str(type(myString)))


"""
Working with string concatenation
String concatenation is the process of combining two strings into one string. You have actually been doing string concatenation since lab 1, but you didnt call this process by that term. The plus sign (+) is used to concatenate strings. When the plus sign (+) is used with strings, it behaves differently than when you use it for numbers. In lab 1, you used the plus sign (+) to add numbers. Now, you will use the plus sign (+) to combine, or concatenate, strings.
"""

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

"""
Working with input strings
In coding, information that a user enters is known as input. You will use a built-in function named 
input() to get information from the user. The input() function will pause the code until a user enters a string and presses ENTER. Return to the Python script:
 """
name = input("What is your name?")
print(name)


""" 
Formatting output strings
When your script wants to communicate information back to the user, it is called output. You have been using the print() function to write output to the shell. You will create a survey and output the information that it collects back to the user.
"""
color = input("What is your favorite color?")
animal = input("What is your favorite animal?")
#Using the format function, you can format in what order you want to print options 
print("{}, you like a {} {}!".format(name,color,animal))