#nested if condition
'''a=10
b=20
if a<b:
    print("less")
    if b>a:
        print("greater")'''

'''a=10
b=20
if a==b:       
    print("less")        #here 1st condition fails it stops 
    if b>a:
        print("greater")'''

'''a=10
b=20
if a==b:
    print("less")
if b>a:
    print("greater")'''

'''a=10
b=20
if a<=b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")'''
 
'''a=10
b=20
if a==b:
    print("less")
    if b!=a:
        print("greater")
else:
    print("true")'''

'''a=10
b=20
if a<=b:
    print("less")
    if b==a:
        print("greater")
    else:
        print("true")
else:
    print("false")'''

'''a=10
b=20
if a<=b:
    print("less")
    if b==a:
        print("greater")
    elif a==b:
        print("not equal")
    else:
        print("true")'''
        
#task
'''a=int(input("enter your age"))
if a >=18:
      print(" eligible for vote")
else:
    print("not eligible for vote")'''
      
#task-even or odd
'''num=int(input("enter a number:"))
if num %2 ==0:
    print("even number")
else:
    print("odd number")'''

#leap year
'''year=int(input("enter a year:"))
if year %400==0:
         print("leap year")
elif year %100==0:
    print("not leap year")
elif year %4==0:
    print("leap year")
else:
    print("not a leap year")'''
#vowels
'''a=["a","e","i","o","u"]
b=(input("enter characters:"))
if b in a:
    print("it is vowels")
else:
    print("it is consonant")'''
