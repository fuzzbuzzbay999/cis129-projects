#Declan Juliano
#lab07 theater seating.
#******** I chose a very different dirrection, through the use of lists, adding more sections is a lot easier, 
# just add the respective details to the 3 lists and the program handles the rest
"""
A dramatic theater has three seating sections, and it charges the following prices for tickets in 
each section: section A seats cost $20 each, section B seats cost $15 each, and section C seats cost $10 each. 
The theater has 300 seats in section A, 500 seats in section B, and 200 seats in section C. Design a program 
that asks for the number of tickets sold in each section and then displays the amount of income generated from 
ticket sales. The program should validate the numbers that are entered for each section.
"""
#to add more sections just append on another section name
sections=['A','B','C']
#to add more sections just append the number of seats for the new section
seats=[300,500,200]
#to add more sections just append the price for a seat in the new section.
prices=[20,15,10]

#consants
#soldseats is set to the length of sections so no need to change
#holds the amount of seatssold per section
soldSeats=[-99]*len(sections)
#amount of money
profit=0
#amount of seats sold
seatsSold=0
#tells the program an invalid number was entered
TRIGGER= False

#class for colors in the console
class color:
   PURPLE = '\033[95m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

#function to retreve data, if the value is invalid it will throw an error and set TRIGGER to True
def getData(index):
    print('')
    print(f'Entering data for section {sections[index]}, total seats in this section {seats[index]}')
    #error catcher
    #if the user inputs a numeric value, update the seats sold, if not a value error is thrown
    try:
        soldSeats[index]= int(input('How many seats were sold? :'))
        #if the user inputs a number larger then the avaliable seats throw value error stating input is too large
        if(soldSeats[index]>seats[index]):
            raise ValueError(color.PURPLE+f'thats not possible, the amount sold {soldSeats[index]} is greater than the availible {seats[index]}'+color.END)
        #if the user inputs a number less than 0 thow value error stating non positive
        if(soldSeats[index]<0):
            raise ValueError(color.PURPLE+'non-positive number'+color.END)
        return False
    #catches the errors and prints out the reason
    except Exception as err:
        print(color.RED+'oops error'+color.END ,err,color.RED+' try again'+color.END)
        return True

#***** actual program ******
#welcome
print(color.UNDERLINE+color.YELLOW+f'Welcome to the Silly Theater Profit Calculator.\nJust follow the instructions and you\'ll be all good:)'+color.END)
#iterates through each index in the sections ('a','b','c'...) and updates the respective indecies in soldSeats, through the getData() function 
for index in range(len(sections)):
    #set TRIGGER to getData return. | False for valid input an true for inalid
    TRIGGER = getData(index)
    #catch invalid input, ex selling more seats then whats available or selling negative seats.
    while(TRIGGER):
        #update trigger with the new value 
        TRIGGER = getData(index)
    print(f'{soldSeats[index]} sold in section {sections[index]}, giving ${soldSeats[index]*prices[index]:.2f} in profit')

print('')

#calculate profit, multiply number sold seats by price of the seats in the section
#prints the respective seat count in the current indexed section with its respective revinue
for index in range(len(sections)):
    profit +=soldSeats[index]*prices[index]
    seatsSold += soldSeats[index]
    print(f'{soldSeats[index]} sold in section {sections[index]}, giving ${soldSeats[index]*prices[index]:.2f}')
#prints the total
print('')
print(f'The total profit is ${profit:.2f} with {seatsSold} seats sold')


