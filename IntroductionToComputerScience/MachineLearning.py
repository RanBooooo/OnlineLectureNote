 ##机器学习
##设计开发算法，让计算机算法能够给予过往数据，改进行为
##自动认知复杂模式，基于数据并作出聪明的决策
##归纳推理，程序根据一个统计现象的不完整数据，尝试建模总结数据中的一些统计属性，用这些数据来预知未来

##可分为两类：
##监督学习supervised learing &非监督学习unsupervised learing
##supervised learing：
##将一个标签与训练集中的每个例子关联，如果标签是不相关的就称为分类学问题。
##如果标签是真实值，就认为它是回归问题
##试图猜测特征和标签的联系

##以下主要讲后者
##unsupervised learing：
##没有标签，学习数据的规律性，学习其结构
##unsupervised learing中占主流地位的是聚类（Clustering）算法
##把有相似点的成员归为一组，聚类内的不相似性低，聚类间的不相似性高。用方差来衡量相似性
##不是方差越小越好，方差最小是每个聚类只有一个元素，要添加约束条件防止过于琐碎的结果，例如限制聚类总量
##计算此类问题计算量一般很大，所以往往用贪心算法
##过程
##一、为每个元素分配一个聚类
##二、合并相似的一对
##三、重复这一过程
##第二步需要定义何为相似，使用连锁标准：单连锁、完全连锁和平均连锁。分别代表取最好取最坏或取平均
##多属性情况下的聚类，例如城市的距离与温度，要考虑各属性的比例权重
##聚类重点往往在于属性的选择和比例的确定，把不同的属性分配何时的比例成为规格化

##学习的过程
##如何确定比例？使用 Minkowski metric明可夫斯基度规
##dist(X1,X2,p)=(∑abs(X1-X2)**p)**1/p
##其中p表示度数
##当p==1时 Manhattan distance曼哈顿距离
##当p==2时 Euclidean distance欧几里得距离

##对于用语义表示的属性，我们一般将他们转化为数字

##例如将哺乳动物按所吃食物分类，但没有完整的数据，我们可以根据其牙齿推测食物
##实现聚类的所用到的抽象类：
##Point（包含名字、属性数组、规格化的属性数组）
##Cluster（点的集合，计算点间距离的方法：最短链、最长链和平均链，以及一个属性centroid（质心））
##ClusterSet（聚类的集合，主要有的方法：合并，找到最近的聚类）
##哺乳动物聚类的具体类
##Point类的子类Mammal用牙齿来代表每种动物

##k-means Clustering,约为线性的时间复杂度，可以解决大型问题
##其中k表示要分成几个聚类
##步骤：
##1.选择k是多少
##2.选择k个point作为质心（centroid）（质心是一个聚类中点的平均中心）一般随机选择
##3.把每个点分配到最近的质心
##4.为每个聚类选择心得质心
##5.重新把每个点分配到最近的质心
##6.重复4和5步知道变化很小为止（4和5步重新分配了多少点）（防止无线循环会设置最大循环次数）
