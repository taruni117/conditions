#conditions
#if-condition by using comparision operators
#<,>,<=,>=,!=,==
#<
'''a=2
b=4 
if a<b:
    print("True")'''
#>
'''a=2
b=4
if a>b:
    print("false")'''
#<=
'''a=10
b=15
if a<=b:
    print("true")'''
#>=
'''a=8
b=2
if a>=b:
    print("right")'''
#!=
'''a=2
b=4
if a!=b:
    print("true")'''
#==
'''a=4
b=4
if a==b:
    print("true")'''
#runtime 
'''a=int(input("a value"))
b=int(input("b value"))
if a>b:
    print("greater")'''
#strings ==
'''a="python"
b="java"
if a==b:
    print("true")'''

'''a="python"
b="python"
if a==b:
    print("true")'''

'''a=20
b=30
if a<b:
    print("true")'''

#if-condition by using logical operators
#and,or,not
#and (both should be true)
'''a=5
b=4
if a<b and b<a:
    print("true")'''

'''a=5
b=4
if a<b and b>a:
    print("true")'''
#or (any one value should be true)
'''a=5
b=6
if a<=b or b<=a:
    print("true")'''

'''a=5
b=6
if a!=b or b<=a:
    print("true")'''

'''a=20
b=30
if a<b or b>a:
    print("less")'''

#not
'''a=4
b=8
if not a<b:
    print("true")'''

'''a=4
b=8
if not a>b:
    print("true")'''
#runtime
'''a=int(input("a value is"))
b=int(input("b value is"))
if a<b or b<a:
        print("true")'''

#if-condition by using identify operators
#is , is  not
#integer
'''a=7
if type(a) is int:
    print("it is int")'''

'''a=7
if type(a) is not int:
    print("it is int")'''
#float
'''a=3.6
if type(a) is float:
    print("it is float")'''
'''a=3.6
if type(a) is not float:
    print("it is float")'''
#string
'''a="python"
if type(a) is str:
    print("it is string")'''
'''a="python"
if type(a) is not str:
    print("it is string")'''
#complex
'''a=9+8j
if type(a) is complex:
    print("it is complex")'''
'''a=9+8j
if type(a) is  not complex:
    print("it is complex")'''
#bool
'''a=True
if type(a) is bool:
    print("it is boolean")'''
'''a=True
if type(a) is not bool:
    print("it is boolean")'''
#runtime
'''a=int(input("enter a value"))
if type(a) is int:
    print("it is int")'''

#if-condition by using membership operators
#in, not in
'''a=[2,3,4,5,6,7,8,9,10]
if 2 in a:
    print("true")'''
'''a=[2,3,4,5,6,7,8,9,10]
if 20 in a:
    print("true")'''
'''a=[2,3,4,5,6,7,8,9,10]
if 20 not in a:
    print("true")'''
#runtime
'''a=int(input("enter a value"))
if 2 in a:
      print("true")'''#error
a=[10,20,30,40,50]
b=int(input("value"))
if b in a:
    print("the value is b",b)



    

