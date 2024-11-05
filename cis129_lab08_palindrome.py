
def is_Palindrome(test):
    #set the input string to a list
    Test=list(test.lower())
    #reverse test list through cutting the list then rebuilding it backwards
    revTest=Test[::-1]
    sum=0
    #iterate tthrough the lists
    for letter in range(len(Test)):
        #compair the letters of each list
        if(Test[letter]==revTest[letter]):
            sum+=1
        #if sum ==length then all letters match thus it is a palindrome
    if(sum==len(Test)):
        return True
    else:
        return False
#prod user if the function returns true then print yes if it returns false then the input is not
if(is_Palindrome(input('enter palindrome: '))):
    print('yes')
else:
    print('no')