# Author Declan Julinao
# makes a reciept

#define vars
coffeePrice = 5
muffinPrice = 4
sconePrice = 10
teaPrice = 5
tax = 6
#initiate plurals as empty strings
coffeePlural = ''
muffinPlural = ''
sconePlural = ''
teaPlural = ''

#prod user about amount of stuff bought
print("***************************************")
print('My Coffee and Muffin Shop')
coffeeNum =input("Number of coffees bought?: \n")
muffinNum =input("Number of muffins bought?: \n")
sconeNum = input("Number of scones bought?: \n")
teaNum = input("Number of teas bought?: \n")
print("***************************************\n")
print("***************************************")
#create the reciept
print("My Coffee and Muffin Shop Receipt")
#maths
coffeeAmount=round(float(int(coffeeNum)*int(coffeePrice)))
muffinAmount=round(float(int(muffinNum)*int(muffinPrice)))
sconeAmount=round(float(int(sconeNum)*int(sconePrice)))
teaAmount=round(float(int(teaNum)*int(teaPrice)))

foodAmount=coffeeAmount+muffinAmount+sconeAmount+teaAmount
taxAmount=(tax/100)*foodAmount
totalAmount = foodAmount+taxAmount

#decides if the line items are plural
if int(coffeeNum)>1:
    coffeePlural='s'
if int(muffinNum)>1:
    muffinPlural='s'
if int(sconeNum)>1:
    sconePlural='s'
if int(teaNum)>1:
    teaPlural='s'

#print the numbers with zero space between string concatenations
print(coffeeNum, " Coffee",coffeePlural," at $",coffeePrice," each: $ ",float(coffeeAmount),'0', sep='')
print(muffinNum," Muffin",muffinPlural," at $",muffinPrice," each: $ ",float(muffinAmount),'0', sep='')
print(sconeNum," Scone",sconePlural," at $",sconePrice," each: $ ",float(sconeAmount),'0', sep='')
print(teaNum," Tea",teaPlural," at $",teaPrice," each: $ ",float(teaAmount),'0', sep='')
#print tax
print(tax,"% tax: $ ",round(taxAmount,2), sep='')
print("---------")
print("Total: $",totalAmount)
print("***************************************")
print("Thanks for visiting see you again soon!!")
print("***************************************")
