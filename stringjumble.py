"""
stringjumble.py
Author: <your name>
Credit: 

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
text=input("Please enter a string of text (the bigger the better): ")
count=len(text)
words=list(text)
print("You entered '"+text+"'.  Now jumble it:")
backwords=[]
for i in range (1,(count+1)):
    backwords.append(words[-i])
a=""
for i in range (0,count):
    a=a+str(backwords[i])
print(a)
spaces=[]
spacecounter=0
for i in range (1,count):
    if backwords [i]==" ":
        spaces.append(i+1)
        spacecounter=spacecounter+1
list=[]
backwurds=""
print(spaces)
for i in range (1,spacecounter,-1):
    for l in range (spaces[i],spaces[i]):
        backwurds=backwords[l]+backwurds
        list.append(backwurds)

print(backwurds)
"""store a string as a list of words"""