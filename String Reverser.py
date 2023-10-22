print ('**********The string reverser*********')
string=str(input ('\nEnter your string:\n>>'))
sr=len(string)
rev=''
i=sr-1
print ("\nThe length of string is:\n",sr,"characters")
while i>=0:
   rev=rev + string[i]
   i-=1
print('\nThe Reverse string is:\n',rev)
