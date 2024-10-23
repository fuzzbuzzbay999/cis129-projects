"""
Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
"""
import math
dogPack = 10
bunPack = 8
dogsLeft = 0
bunsLeft = 0

def dogDistribution(numPeople,numDogs):
    #total hotdogs
    totalDogsNBuns = int(numPeople)*int(numDogs)
    #total packs of dogs
    numDogPacks=math.ceil(totalDogsNBuns/dogPack)
    #total packs of buns
    numBunPacks = math.ceil(totalDogsNBuns/bunPack)
    #how many dogs are left
    dogsLeft=(numDogPacks*dogPack)-totalDogsNBuns
    #how many buns are left
    bunsLeft=(numBunPacks*bunPack)-totalDogsNBuns
    #return a "list"
    return(totalDogsNBuns,numDogPacks,numBunPacks,dogsLeft,bunsLeft)

#interprets the list(tuple)
def interpreter(list):

    #saves list to data for easier to understand
    data=list

    #print out result with the indexes in data
    print('Minimum packages of hot dogs needed: ',data[1])
    print('Minimum packages of hot dog buns needed: ',data[2])
    print('Hot dogs left over: ',data[3])
    print('Hot dog buns left over: ',data[4])

#prod user for data, print the results from the nested function calls starting wih the dogDistriution, then the interpreter.
interpreter(dogDistribution(input("Enter the number of people attending the cookout: "),input("Enter the number of hot dogs for each person: ")))
