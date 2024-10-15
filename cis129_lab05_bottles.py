#Declan Juliano
#lab 5
#No doc


#I like the challenge that programming offers, so I refrained from using the word doc.

#Define variables
totalBottles = 0
returnAmount = 0.10
totalPayout = 0
week = 7
keepGoing = "y"
#keep program running untill user enters N
while(keepGoing=='y'):
    #prompt the accumulated bottles collected for each day in a week
    for day in range(week):
        totalBottles += int(input(f'Enter number of bottles for day #{day+1}: '))
    #display the info with dollers rounded to 2 decimals 
    print('')
    print('The total number of bottles collected is',totalBottles)
    totalPayout=totalBottles*returnAmount
    print(f'The total paid out is ${totalPayout:.2f}')
    print('')
    #prompt user to continue or no
    keepGoing = str(input('Do you want to enter in another week of bottles? Y(es) or N(o) ').lower())
    #if user says no then break
    if(keepGoing == 'n'):
        break
    #reset values
    totalBottles = 0
    totalPayout = 0
    

