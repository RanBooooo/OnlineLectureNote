##仿真法（模拟法）与计算机
##解析法——给出先觉条件和参数可以预测出结果的方法。例如牛顿物理学、微积分和概率论。解决宏观物理问题

##使用仿真法的原因：
##当无法通过数学处理、难以构建模型，解析法就无法解决此类问题，此时就需要仿真法
##当问题变得十分复杂，连续提炼一系列的模拟，能解决问题
##相比构建精确分析模型，从模拟中提取中级的结果相对容易
##能用计算机来处理

##仿真法的方法：
##建立模型
##给出系统行为的有用信息
##能出现实结果的近似值
##仿真模型是描述性的不是指定性的
##（每次执行模拟可能得出的结果不同，但是我运行很多次就能大致得出近似结果）

##布朗运动是随机游动的例子
##醉汉游走问题，用仿真法的例子，一个醉汉每秒走一步，向正东西南北走，向每个方向走的概率相同，出发后一千秒后他距离出发点多远？

##波尔和海森堡提出的哥本哈根主义，最基础的层面的物理活动是不可预测的，一切皆是随机有可能发生的
##爱因斯坦和薛定谔的观点与前者相悖，争论的焦点在于这两点：
##causal non-determinism（因果不确定性）和predictive non-determinism(可预测不确定性)
##爱因斯坦认为：之所以不可预测是因为物理系统的描述不完整,通俗来讲就是：之所以无法预测是因为知道的不够，

##stochastic processes （随机过程）：
##下一个状态依赖于上一状态和一个随机元素
##一个独立结果对另一个结果没有影响

##Python Randon.choice（从数组中随机取一个数）的实现用了random.random,生成一个[0,1)的浮点数

##Python中的绘图库是Pylab 类似于MATLAB
##Python中的Plotting是和MATLAB很像
import pylab

##pylab.plot([1,2,3,4],[1,2,3,4])
##pylab.plot([1,3,2,3],[5,6,7,8])
##pylab.show()

##pylab.figure(1)
##pylab.plot([1,2,3,4],[1,2,3,4])
##pylab.figure(2)
##pylab.plot([1,4,2,3],[5,6,7,8])
##pylab.savefig('firstSaved')
##pylab.figure(1)
##pylab.plot([5,6,7,10])
##pylab.savefig('secondSaved')
##pylab.show()

##计算复利
principal = 1000 #initial investment
interestRate = 0.05
years = 100
values = []
for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(values)

pylab.title('5% Growth, Compounded Annually')
pylab.xlabel('Years of Compounding')
pylab.ylabel('Value of Principal ($)')

pylab.show()


##坐标轴取对数，比较有用
##pylab.semilogx
##pylab.semilogy

##柱状图
##pylab.hist([1,2,3,4,5,2,2,1],bins = 6)

##定义图的标尺，可用于在同一标尺下比较两张图
##pylab.xlim(xmin,xmax)
##pylab.ylim(ymin,ymax)

##用随机解决非随机问题
##计算π

##曲线求律法
##用pylab内置函数，其使用了线性回归
##a,b,c,d = pylab.polyfit(observedX,observedY,degree)
##返回多少项表示y=ax**3+bx**2+cx+d
##两项表示直线，三项开始是曲线，项越多曲线越贴合点
##衡量数据与所求曲线模型的关系，公式：R**2=1-estimateError/mesurementVarient
##越接近1越好，0表示毫无关系

