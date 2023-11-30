# Asking the user if they need to ship a package and responding accordingly.
userReply = input("Do you need to ship a package? (Enter yes or no)")

# Checking the user's response and providing an appropriate message.
if userReply == "yes":
    print("We can help you ship that package!")
else:
    print("Please come back when you need to ship a package. Thank you.")

# Asking the user what service they would like: buy stamps, buy an envelope, or make a copy.
userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")

# Checking the user's response and providing relevant information.
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    # If the user wants to make a copy, asking how many copies they would like.
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    # If the user's response doesn't match any of the options, thanking them and ending the interaction.
    print("Thank you, please come again.")

