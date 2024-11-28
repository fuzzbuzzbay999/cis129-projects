#Declan Juliano
#lab011 data storage and file handling
#******** these are 2 very specific examples of storing data, first 2 are for reading and writing a text file. 
#the last is for creating a csv doc, with the data in tupple rows.





#*************TXT WRITE******************
#generates a txt file with a grade then the student number, alowing for non-sequential reads

def TXTw():
    print("Enter the grade for the student, -99 to quit")
    total=0
    value=0
    count = 1
    with open('grades.txt',mode='w')as file:
        #write file with grades
        while(True):
            try:
                
                #if setting value to the int() of the input passed without error, then proceed
                value= int(input(f'Entering data for student #{count} '))
                
                if(value ==-99):
                    break
                elif(value<0):
                    raise ValueError('Grades cant be negative!!!!')
                #write the value to the file in the format (grade,student number)
                file.write(f'{value} {count}\n')
                #increase student number
                count+=1
                
            except Exception as error:
                #if the above code threw an error then warn and try again
                print(f'Thats not right, {error}')


#*************TXT READ******************
#reads and displays the data in the txt file made in the code above
def TXTr():
    total=0
    with open('grades.txt',mode='r') as grades:
           print('student \t grade earned')
           print('*****************************')
           
           grade=0
           for line in grades:
               #unpack lines[grade count] into grade and the count variables
               grade,count = line.split()
               #print the student number  and grade
               print(f'student #{count} \t got {grade:>8}')
               #calculate toal
               total+=(float(grade))
           #print the data
           print(f'The total is {total}')
           print(f'The student count is {count}')
           print(f'The class average {int(total)/int(count):.3f}')
    

#*************CSV WRITE******************
#takes the first and last name, and stores 3 exam grades in a csv file
import csv
import sys
def CSVw():
    with open('grades.csv',mode='w',newline='') as grades:
        #variables
        #we will use format for setting the length of each row of the csv document 
        Format=['(String) Fist Name:','(String) Last Name:','(Integer) Exam 1 grade:','(Integer) Exam 2 grade:','(Integer) Exam 3 grade:']
        #types format data should be
        FormatType=['str','str','int','int','int']
        #list to commit to the current csv line
        dataToSave=[]
        #current index
        index = 0
        #initiates the writer
        writer=csv.writer(grades)

        print('Enter the info as promted, enter -99 in any field to exit')
        while(True):
            #if index => the length of format(length of csv rows) 
            if(index>=len(Format)):
                #reset index
                index=0
                #write the line
                #ONLY WRITES THE LINE IF 5 VALUES HAD BEEN SUCESSFULLY ENTERED!!!
                writer.writerow(dataToSave)
                #reset the dataToSave
                dataToSave=[]
            #get the value
            value=input(Format[index]+' ')
            #test sential and flush the writer.
            if(value=='-99'):
                sys.exit()

            #test if the value type alligns with the format type
            if(FormatType[index]=='int'):
                try:
                    #if the value should be int TRY to make it an int
                    value=int(value)
                    if(value<0):
                        raise ValueError('Grades cant be negative!!!!')
                    #if so, append the value to the dataToSave list
                    dataToSave.append(value)
                except Exception as error:
                    #if not, decrease the index and print the error
                    print('Something went wrong:',error)
                    index-=1
            else:
                #if valye is not supposed to be an Int then  append it to the dataToSave
                dataToSave.append(value)
            #increase the index
            index+=1
            #back to the top

def main():
    while(True):
        print('\nThis menu helps run through two various methods of storing and reading data')
        print('1: Enter a list of grades for an assignment')
        print('2: Read the grade file and display metrics')
        print('3: Enter and store 3 exam grades in a CSV file')
        print('4: Exit')
        print('Enter the integer to select the option you want below.')
        option=input('|')
        if(option == '1'): 
            TXTw()
        elif(option=='2'):
            TXTr()
        elif(option=='3'):
            CSVw()
        elif(option=='4'):
            print('exiing...')
            sys.exit()
        else:
            print('Thats not an option silly, try again')
main()    

''' 
*****************************************
failed attempt at the csv using for loops
I am too tired to make it work
*****************************************

import csv
import sys
with open('grades.csv',mode='w',newline='') as grades:
    #variables
    Format=['Fist:','Last:','exam1grade:','exam2grade:','exam3grade:']
    FormatType=['str','str','int','int','int']
    writer=csv.writer(grades)
    print('enter the info as promted, enter -99 in any feild to exit')
    while(True):
            dataToSave=[]
            #if setting value to the int() of the input passed without error, then proceed
            for index in range(len(Format)):
                value= input(Format[index]+':')
                print(type(value))
                if(FormatType[index]=='int'):
                    try:
                        value=int(value)
                    except Exception as error:
                        print(error)
            #if sentinal value entered exit without error
                if(value=='-99'):
                    sys.exit()
                dataToSave.append(value)
            print(dataToSave)
            writer.writerow(dataToSave)
'''
