
#1: Print only the words that Start with s in the sentence

string = 'print only the words that Start with s in the sentence'
string.split()
for s in string.split():
    if s[0].lower() == 's':
        print(s)



#2: Use range() to print all the even numbers from 0 to 10

list1 = [x for x in range(0,11) if x%2==0]




#3: Use a list comprehension to create a lost of all numbers  between 1 & 50 that are divisible by 3

mylist = [x for x in range(0,51) if x%3==0]



#4: Go through the string below and if the length of a word is even print Even

st = "Print every word in this sentence that has an even number of letters"
for s in st.split():
    if len(s)%2==0:
        print(s)



#5: Go through the string below and of the length if a word is even print the word

st = "Print every word in this sentence that has an even number of letters"
for s in st.split():
    if len(s)%2==0:
        print(s)
    
#6: Write a program that prints the integer from 1 to 100 but for te multiples of three print “Fizz” and for multiple of 5 print “Buzz” and for multiple of both 3 and 5 print “BuzzFizz”

for x in range(1,101):
    if x%3==0 and x%5==0:
        print("FizzBuzz")
    
    elif x%5==0:
        print("Buzz")
    elif x%3==0:
        print("Fizz")
    else:        print(x)


#7:  Create a list of the first letters of every word in this sentence

st = 'Create a list of the first letters of every word in this sentence'
[s[0] for s in st.split()]



#8: Program to remove check the duplicate elements in a list and removing the duplicates


mylist = [5,9,2,4,7,1,3,8,1,1,1,1,6,0,0,0,10]
newlist = []
newlist2 =[]
for x in mylist:
    if mylist.count(x) > 1:
        newlist.append(x)
        
    elif mylist.count(x) == 1:
        newlist2.append(x)
        
        #print(x)
        
print("Duplicate elements are :", newlist)        
print("Non-Duplicate elements are :", newlist2) 



res=[]
for x in mylist:
    if x not in res:
        res.append(x)
print("The list without duplicates is :", res)






# Lesser of two numbers: write a function that returns the lesser of two given numbers if both numbers 
# are even, but return the greater if one or both numbers are odd

def myfunc(a,b):
    if a and b % 2 == 0:
        if a > b:
            return b
        else:
            return a
    elif a or b % 2 != 0:
        if a > b:
            return a
        else:
            return b
        
        
myfunc(7,1)



# Animal Crackers: Write a function that takes two- word string and returns True if bith begin with same letter
def func1(text):
    word = text.lower().split()

    
    print(word)
    
    first = word[0]
    second = word[1]
    
    return first[0] == second[0]
    
func1('hello How')



# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def func2(a,b):
    if a+b == 20 or a == 20 or b == 20:
        return True
    else:
        return False

func2(2,3)




#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name


def func3(name):
    mylist = list(name)
    mylist[0]=mylist[0].upper()
    mylist[3]=mylist[3].upper()
    #glue = ''
    name = ''.join(mylist)
    return name

func3('macdonalds')



#MASTER YODA: Given a sentence, return a sentence with the words reversed

#reverse the whole string

def strev(string):
    mylist = list(string)
    mylist1 = mylist[::-1]
    string = ''.join(mylist1)
    print(string)

strev("Test this string for reverse")

#reversing each wors in a string

def rvstr(string):
    inp = string.split(" ")
    inp = inp[-1: :-1]
    output = " ".join(inp)
    print('\n')
    print(output)

rvstr('this is to test reversal of each element of string')






#plusMinus yet to be solved
def plusMinus(arr):
    pos = 0
    nev = 0
    neu = 0
    num = 0
    mylist = []

    for item in arr:
        num += 1
        

        if item > 0:
            pos += 1
        
        elif item < 0:
            nev += 1
    
        else:
            neu += 1
            
    ptv = pos/num
    ngt = nev/num
    ntg = neu/num
    
    return ptv,ngt,ntg
    
        
#     print('Total :',num)
#     print('Positive :',pos)
#     print('Negative :', nev)
#     print('Zero :', neu)

a = [-4, 3, -9, 0, 4, 1]
plusMinus(a)    
    
    



#return pos, nev, neu  