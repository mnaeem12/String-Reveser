print ('The string reverser')
string=str(input ('Enter your string:'))
sr=len(string)
rev=''
i=sr-1
print ("The length of string is :",sr)
while i>=0:
   rev=rev + string[i]
   i-=1
print('The Reverse string is:',rev)