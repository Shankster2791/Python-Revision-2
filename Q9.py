#9. Write a function ‘nearly_equal’ to test whether two strings are nearly equal. Two strings ‘a’ and ‘b’ are nearly equal when ‘a’ can be generated by a single mutation on ‘b’.
def nearly_equal(str1,str2):  # sourcery skip: aug-assign, remove-pass-elif
    count=0
    i=j=0
    while(i<len(str1) and j<len(str2)):
        if(str1[i]!=str2[j]):
            count=count+1
            if(len(str1)>len(str2)):
                i=i+1
            elif(len(str1)==len(str2)):
                pass
            else:
                i=i-1
        if(count>1):
            return False
        i=i+1
        j=j+1
    if(count<2):
            return True
  
str1=input("Enter first string::\n")
str2=input("Enter second string::\n")
boolean=nearly_equal(str1,str2)
if(boolean):
    print("Strings are nearly equal.")
else:
    print("Strings are not equal.")
