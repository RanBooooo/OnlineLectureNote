
##x=0.0
##numIters = 10000000
##for i in range(numIters):
##    x+=0.1
##print (x)
##print (repr(x))
##print (10.0*x==numIters)

#Python类的声明用例
class myObject:
    y=4#类公有的变量应该是不可变类型的
    def __init__(self):
        self.x = 3#成员属性
    def myMethod(self):#第一个参数时self的方法是成员方法
        return 3
    def myMethod2(self):
        return self.x
    def myMethod3():#这个是静态函数
        return self.y


##特殊的成员方法
##__init__ 构造函数
##__str__ ToString方法
##__lt__ 比较方法

##pass是python中什么都不做的关键字，在缩进的语块中防止句式错误
##例如申明新类继承自父类，实现中使用只使用pass，表示和父类完全一样

##Python异常处理
##raise关键字抛出异常
##try exception关键字组合使用接受处理各类异常

##in关键词 直接可以检查数组中是否包含某个元素
##if who in self.student

##yield关键词 是一种generator（生成器）
##用yield在函数中代替return，yield函数会记住函数体中上次返回的位置和局部变量
##可以用for in语句迭代此函数，常用于间接操作对象的成员数组

    
    


