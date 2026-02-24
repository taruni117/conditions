#if-else
#conditions by using comparision operators
'''a=6
b=8
if a<b:
    print("less")'''

'''a=6
b=8
if a>b:
    print("less")
else:
    print("true")'''
'''a=5
b=6
if a<=b:
    print("less")
else:
    print("true")'''
'''a=3
b=9
if a!=b:
    print("true")
else:
    print("less")'''
'''a=3
b=9
if a==b:
    print("equal")
else:
    print("not equal")'''
'''a=int(input())
b=int(input())
if a>b:
    print("greater")
else:
    print("true")'''
#logical operators
#and ,or,not
'''a=6
b=12
if a<b and b>a:
    print("true")
else:
    print("false")'''
'''a=3
b=8
if a!=b or a==b:
    print("equal")
else:
    print("not equal")'''
'''a=8
b=9
if not a<b:
    print("true")
else:
    print("false")'''
#runtime
'''a=int(input())
b=int(input())
if a<b and b>a:
    print("true")
else:
    print("false")'''
'''a=int(input())
b=int(input())
if a<b or b>=a:
    print("true")
else:
    print("false")'''
#if-else condition by using identify operator
#is , is not
'''a="python"
if type(a) is str:
    print("it is string")
else:
    print("it is not string")'''
'''a=123
if type(a) is int:
    print("it is integer")
else:
    print("it is not integer")'''
'''a="123"
if type(a) is int:
    print("it is integer")
else:
    print("it is not integer")'''
'''a=4.5
if type(a) is float:
    print("it is float")
else:
    print("it is not float")'''

'''a=4+9j
if type(a) is complex:
    print("it is complex")
else:
    print("it is not complex")'''
'''a=True
if type(a) is bool:
    print("it is boolean")
else:
    print("it is not boolean")'''
#is not
'''a="python"
if type(a) is not str:
    print("it is string")
else:
    print("it is not string")'''
'''a="python"
if type(a) is not int:
    print("it is integer")
else:
    print("it is not integer")'''
'''a=55
if type(a) is not str:
    print("it is string")
else:
    print("it is not string")'''
'''a=int(input())
b=int(input())
if type(a) is int and type(b) is float:
    print("true")
else:
    print("false")'''
'''a=float(input("a value"))
if type(a) is not float:
     print("true")
else:
     print("false")'''
#if-else conditions by using membership
#in, not in 
'''a=[1,2,3,4,5,6]
if 2 in a:
    print("true")
else:
    print("false")'''
'''a=[1,2,3,4,5,6]
if not 2 in a:
    print("true")
else:
    print("false")'''
'''a=[3,4,5,6,7]
b=int(input("a value"))
if b not in a:
    print("the value is", b)
else:
    print("false")'''

#if-elif-else
#comparitive 
'''a=4
b=11
if a>b:
    print("less")
elif a<b:
    print("greater")
else:
    print("true")'''

'''a=5
b=11
if a>b:
    print("less")
elif a<b:
    print("greater")
elif a==b:
    print("false")
else:
    print("true")'''
#logical
#and,or,not
'''a=3
b=4
if a>b and b<a:
    print("greater")
elif a<b or b>a:
    print("lesser")
elif not a!=b:
    print("false")
else:
    print("true")'''
'''a=9
b=3
if a<b and a==b:
    print("false")
elif a>b or a<b:
    print("true")
elif not a!=b:
    print("greater")
else:
    print("yes")'''
#membership
#in,not in
'''a=[1,2,3,4,5]
if 2 in a:
    print("yes")
elif 3 not in a:
    print("no")
else:
    print("good")'''
'''a=[1,2,3,4,5]
if 20 in a:
    print("yes")
elif 3 not in a:
    print("no")
else:
    print("good")'''

