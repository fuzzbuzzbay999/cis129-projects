# Author Declan Julinao
# makes a reciept

#define vars
coffeePrice = 5
muffinPrice = 4
tax = 6
#prod user about amount of stuff bought
print("***************************************")
print('My Coffee and Muffin Shop')
coffeeNum =input("Number of coffees bought?: \n")
muffinNum =input("Number of muffins bought?: \n")
print("***************************************\n")
print("***************************************")
#create the reciept
print("My Coffee and Muffin Shop Receipt")
#maths
coffeeAmount=round(float(int(coffeeNum)*int(coffeePrice)))
muffinAmount=round(float(int(muffinNum)*int(muffinPrice)))
foodAmount=coffeeAmount+muffinAmount
taxAmount=(tax/100)*foodAmount
totalAmount = foodAmount+taxAmount
#print the numbers with zero space between string concatenations
print(coffeeNum, " Coffee at $",coffeePrice," each: $ ",float(coffeeAmount),'0', sep='')
print(muffinNum," Muffins at $",muffinPrice," each: $ ",float(muffinAmount),'0', sep='')
print(tax,"% tax: $ ",round(taxAmount,2), sep='')
print("---------")
print("Total: $",totalAmount)
print("***************************************")
