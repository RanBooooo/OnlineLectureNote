##x=3
##x=x*x
##print (x)
##y=float(input('Please input a number: '))
##print(y)
##x = int(input())
##if x%2==0:
##    print('Evan')
##else:
##    print('Odd')
##    if x%3!=0:
##        print('also not divisible by 3')
    
##def withinEpsilon(x,y,epsilon):
##    """x,y,epsilon floats. epsilon>0.0 return true if x is within epsilon of y"""
##    return abs(x-y)<=epsilon
##
##print (withinEpsilon(2,3,1))

# def f(x):
#     x=x+1
#     print("x=",x)
#     return x
# x=3
# z=f(x)
# print('z=',z)
# print('x=',x)

##def f1(x):
##	def g():
##		x='abc'
##		#assert False
##	x=x+1
##	print ('x=',x)
##	g()
##	#assert False
##	return x
##
##x = 3
##z = f1(x)

##test=(1,2,3,4.3,'5')
##print(test)

# L1=[2]
# L2=[L1,L1]
# L1.append(3)
# print(L2)

# D1={'Tim':80,'Tom':90,'Jack':100}
# print(D1)

#河内塔问题 典型的递归思路

def hanoi(number,first,second,third):
    global x

    if(number==1):
        x+=1
        #print('move form '+first+' to '+second)
    else:
        hanoi(number-1,first,third,second)
        hanoi(1,first,second,third)
        hanoi(number-1,third,second,first)

x=0       
hanoi(32,'RedTower','BlueTower','GreenTower')
print(x)



