DP L3

字符串或连续的事物如何确定子问题？

-后缀X[ i : ]

-前缀X[ : i ]

-子字符串X[ i : j ] I<=j

Edit Distance Problem

两个字符串X、Y，用最少的开销把一个字符串变得和另一个一样

可以进行三种操作，删除、插入、替换，三种操作可以定义不同的开销

1.重叠子问题

​	对于X[ i : ] & Y[ j : ] 对于 i , j

​	子问题的数量=Θ(|x|*|y|)（x的长度乘以y的长度）

2.最优子结构

​	猜测

​	把X变成Y的情况

​	替换x[i]->y[j]

​	插入y[j]

​	删除x[i]

3.递归

​	DP( i , j ) = min(

​		(1)替换x[ i ]->y[ j ]的开销 + DP( i+1 , j+1 )

​		(2)插入y[ j ]的开销 + DP( I , j+1 )

​		(3)删除x[ I ]的开销 + DP( I + 1 , j )

​	)

4拓扑排序

​	从最小后缀到全部，从字符串尾到头

​	for i = |x|……0

​		for j = |y|……0

​	一个二维邻接有向图 

5.原问题

​	解决

复杂度

​	时间 = Θ(|x|*|y|) 二次的时间

​	空间 线性空间

DP L4：吉他指法问题，俄罗斯方块问题，超级玛丽兄弟问题

算法复杂度

P——多项式级时间解决的问题

NP——非确定的多项式级

EXP——指数级时间解决的问题

R——有限时间内解决的问题

​	例子：

​	-负权重环检测 ∈P

​	-n*n 国际象棋问题（给特定布局谁会赢  ∈EXP  ∉P

​	-俄罗斯方块 ∈EXP

​	-halting problem（停机问题）∉R

大多数决定问题是不可计算问题 ∉R

​	-程序≈二级制字符串≈常数∈N——是有限的

​	-ducision problems决定问题（定义：函数输入得出布尔结果）如果输入是个自然实数∈R——是无线的

​	|R|>>|N|所以问题远多于能处理它的程序

​	所以在数学上几乎所有的问题都无法被程序解决

NP定义：

​	1.决定问题通过一个“幸运”的算法能在多项式级时间内解决

​	-非确定模型（非计算模型而是理论模型）；算法作出猜测，最终算法得出布尔结论

​	2.决定问题有一个“解决方案”可以在多项式级时间内“检验”

​	-决定的答案是ture，且能证明，多项式级时间内能证明检验

​	俄罗斯方块∈NP

​		证明 = 连续的进行的移动

P ≠ NP：巨大的争议点

​	≈“can’t engineer luck”（“不能造出幸运”）

​	≈generating or proofs solutions can be harder than checking them

如果P ≠ NP 俄罗斯方块∈NP-P=>∉P

​	为什么？俄罗斯方块是NP-hard as hard as every problem ∈P

​	-事实上俄罗斯方块是NP-complete（NP完全）

​	NP-complete = NP-hard∩NP （线上NP的右端点）

​	国际象棋问题∈EXP-complete（线上EXP的右端点）

问题规约：A->B

​	A转化为问题B

​	例如：无权图规约成权重都是1的加权图