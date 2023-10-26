print ('**********The string reverser*********')
string=str(input ('\nEnter your string:\n>>'))
sr=len(string)
print ("\n-------------------------------------")
print ("The length of string is:\n      ",sr,"characters\n")
rev=''
i=sr-1
space=0
spaces_posi=[]
reverse_words=""
word=0
words=[]

#reverse all string left to right function 
def RevAllChar(string):
    rev=''
    sr=len(string)
    i=sr-1
    while i>=0:
        rev=rev + string[i]
        i-=1
    return rev
    
#reverse the position of wordes function    
def RevWordPosition(string):
    space=0
    t=0
    reverse_words=''
    i=len(string)-1
    while space<=i:
        if string[space]==" ":
            spaces_posi.append(space)
            words.append(string[t:space])
            t=space+1
        if i==space:
            words.append(string[t:space+1])
        space+=1    
    no_word=len(words)-1
    while no_word>=0:
        reverse_words= reverse_words + words[no_word]+' '
        no_word-=1
    return reverse_words 
    
    
#reverse charactors in any word function    
def RevCharInWord(string):      
    space=0
    temp=[]
    words=""
    str=string 
    t=0
    while space<=i:
        if str[space]==" " or i==space:
            if space == i:
                temp= RevAllChar(str[t:space+1])#for last char if string is not end with space
            else:
                temp= RevAllChar(str[t:space])
            words=words+temp+' '
            temp=[]
            t=space+1
        space+=1
    return words
        
       
#select type of reverse            
print ('------------------------------------')
reverse_type=input('Enter revers type:\nReverse all string    :"A"\nReverse words position:"W"\nReverse char in words :"C"\npress any key to exit\n:>>'). lower()    
print ('\n------------------------------------')
if (reverse_type=="a"):
    rev=RevAllChar(string)
    print('The Reverse string is:')
    print (rev)    
elif(reverse_type=="w"):    
    rev=RevWordPosition(string)    
    print('The Reverse string is:')
    print (rev)
elif(reverse_type=="c"):     
    rev=RevCharInWord(string)  
    print('The Reverse string is:')    
    print (rev)
else:
    pass
