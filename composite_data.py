# Importing necessary tools for working with CSV files and making copies of objects.
import csv
import copy

# Defining a template for a car, with placeholders for details.
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Displaying the initial structure of our car template.
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Creating an empty list to store information about various cars.
myInventoryList = []

# Opening a file containing details about different cars, each separated by commas.
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    lineCount = 0  # A counter to keep track of the line we're examining.
    
    # Iterating through each line in the file.
    for row in csvReader:
        if lineCount == 0:
            # Displaying the column names on the first line.
            print(f'Column names are: {", ".join(row)}')
            lineCount += 1
        else:
            # Displaying details of each car in a readable format.
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            
            # Creating a new car object based on our template and filling in the details.
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            
            # Adding the new car to our list.
            myInventoryList.append(currentVehicle)
            lineCount += 1
    
    # Indicating the number of lines processed.
    print(f'Processed {lineCount} lines.')

# Creating a redundant copy of our car template; this line could be optimized.
currentVehicle = copy.deepcopy(myVehicle)

# Displaying detailed information about each car in our list.
for myCarProperties in myInventoryList:
    # Displaying each property and its value, separated by dashes.
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
        print("-----")
