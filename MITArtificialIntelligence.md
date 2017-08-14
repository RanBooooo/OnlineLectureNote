L1

人工智能的定义：支持进一步理解想法、知觉和行动的模型的呈现所揭示的约束条件所构造的算法

并用循环把想法、知觉和行动串在一起

人工智能发展的几个时代：黎明时代，离奇时代，推土机时代和现在所处的时代（the right way）

L2

以解微积分为例讲解

problem reduction tree / goal tree / and or tree

L3

演示吊车小程序如何回答关于自身行为的问题（Why How）通过建立goal tree回答why的问题是向下，回答how的问题是向上

forward-chaining rule-based expert system如何根据特征识别出动物园中的一种动物，

Backward-chaining …作出假设根据其特征确定是否是这种动物

统称为deduction system推理系统

L4 搜索：深度优先搜索，Hill Climbing，Beam

DFS后进先出（栈），BFS先进先出（队列），Hill Climbing空间距离排序的队列，Beam BFS基础上根据w（宽度）选择前w名入列

Hill Climbing的局限：被困在局部最大，电线杆问题（都是平面），维度太低（向正方向搜索）

L5 搜索：最优，Branch and Bound，A星

Oracle先指出一条路径，再比较别的路径没有比他短。Branch and Bound，按累计距离排序，取最短继续搜索；直到找到目标后再Oracle。+Extended List探过的点不继续拓展。+admissible heuristic排序时加上与目标点的空间距离。A*就是Branch and Bound + Extended List + admissible heuristic。

在非地图（空间分布不可靠时）求最短路径时A*可能无法得到最短路劲。应该加一个改进条件。admissible（可接受性） 空间距离<=实际距离，则这是符合一般地图空间的。consistency（一致性） 一点到目标的空间距离减另一点到目标的空间距离取绝对值 应该小于等于这两点的实际距离

L6 搜索：Games，Minimax和Alpha-Beta

计算机下象棋战胜人类的方法：1. 分析策略与战术来决定下一步的行动 （机器无法实现）2.If-Then规则，检查棋盘上能下哪些步，评估每个的优劣，选最优的（但是无法战胜人类）3.向前看并评估，那种下法最终最优

第三种方法可行但是，以此建立Game树，要评估一盘棋往往要约15^120次方次计算，每步有约15种可能性，一盘棋大约120步，无法完成计算

Minimax：

树的每层分别由max玩家和min玩家决策，min玩家选择最小的，max玩家选择最大的，从树底往上选出答案。虽然不会取到最大值但是是一个对抗游戏。

能计算的树越深，就能得出更好的结果。

Alpha-Beta：

在Minimax的基础上逐个计算树叶，当发现某一子树肯定不会出现比已知的子树更大的结果时，砍掉分子树减少计算量

有了Alpha-Beta能计算的树的深度提高一倍，从大约7步变为14步，达到世界冠军水平

Progressive deepening（逐步深化）能够随时终止获取结果，时间越长计算约深效果越好

深蓝=Minimax+Alpha-Beta+Progressive deepening+许多的平行计算+opening book（开局库）+为了结束游戏特殊目标物+非均匀的树结构

L7 约束：解释画线

计算机识别物体个数 理论的发展：1.假设物体是立方体，在立方体交接处连线，连接两个以上的两个平面是同一物体（不靠谱）2.增加假设都是三面顶点，定义凹凸边和边界5种图标，形成共18种可能的结果（也不够准确）3.在此基础上增加间隙、阴影、非三面顶点、光线，定义50多种图标，形成可能的上千种结果，通过约束减少DFS计算量

L8 约束：搜索，Domain Reduction

地图上色问题。。几种约束从少到多的顺序：1. 不检查，得不到相邻不同色的效果。2. 仅分配颜色，当决定了部分块的颜色后会出现有些邻接块没有颜色可上，陷入极长的运算。3.检查分配用Domain Reduction算法，分配一个块颜色后检查相邻块是否冲突（有结果但是也要很长时间）。4. 不一直传递，只在有多重颜色可选的块传递，直到只剩一种颜色可选 5.不断传递对相邻块的检查 。6. 检查每一块。

同时优先从约束最多的开始（邻接最多）分配，也能降低运算时间

此问题等同于航班安排问题，也就是安排行程问题

L9 约束：视觉对象识别

30年的图像识别的发展缓慢

一个物体任意旋转三个方向的正交投影，来确定另一个物体的投影是不是同一物体

运用到人脸识别上，不能将脸看做整体，而要看五官的相互关系决定，例如2个眼睛，2个眼睛+鼻子，鼻子+嘴巴

用这些五官条件作为约束，对图像中的标准化，求积分，就能匹配出相似的人脸

但问题是颠倒转动脸，识别率就会大打折扣

L10 机器学习导论，Nearest Neighbors

机器学习分为两类

第一类：观察规律（可认为是推土机计算，计算机处理信息就像推土机处理沙堆）

1.最近邻居，辨识模式

2.神经网络，模拟生物学

3.boosting，理论学家的礼物

第二类：基于约束（更像人的一条分支）

1.One Shot， 某事的经验学到确切的东西

2.基于解释的学习，从自我解释中学习

最近邻居：侦测对象的各项属性，将属性向量传入比较器，比较器中与一个大量数据的库中的数据比较，得到这个对象是什么，或给这个对象分类

操作两个转轴（θ1、θ2）的机械臂以某一速度、加速度移动，用牛顿物理学的等式无法得到想要的结果。由于存在各种公差机械各种问题。建立一张大表例如有以下字段：θ1、θ2、速度θ1、速度θ2、加速度θ1、加速度θ2、扭矩1、扭矩2。让机械臂自由挥动记录这些数据，当需要让机械臂执行某一操作时，就到表中查找。

遇到的问题：1.分散问题。例如数据在x轴较集中y轴特别分散，忽略y对x的数据规格化，用统计学的方法求方差σx，计算x’=x/σx

2.什么数据有关，什么数据无关

3.没有数据（没办法）

L11 机器学习：辨识树，混乱度

辨识吸血鬼的例子，在多个维度的属性中，是否有影子，是否吃大蒜，肤色，口音。通过逐个分析每个属性与是否是吸血鬼这个结果，运用信息理论学的混乱度的方法辨别最优维度，以此建立辨识树。

L12 机器学习：神经网络，反向传递

神经网络从生物学的神经元获取灵感。神经细胞一端是轴突，另一端是树突，为下游神经元轴突连接提供了场所。神经脉冲从下游往上游传递，传递时轴突中的囊泡向上游树突挤压

传递类似电脑，有或无，0或1。每次传递完后有一段时间的不应期来恢复神经元的能良

用计算机建模模拟神经元信号的传递，两个输入input1（0或1）和input2（0或1）有各自权重，求和若大于某一阈值则输出1否则输出0。由于不应期异常的偶然，在建模中不包括，同一轴突的分支和时间模式对神经脉冲传递的影响也不了解，所以建模中不包括。

大脑可看作一个充满了权重和阈值的盒子，不同的输入x会有不同的输出结果z。

z=f(x,w,t) z是关于输入x、权重w和阈值t的函数

神经网络可看作是函数预测器

在已知结果d时，用一个表现函数P=-(d-z)^2来评估，0表示无差别表现最好

这样只要改进权重w和阈值t就能改进表现

用hillclimb不可行应为实际中有上千万个参数，所以对每个参数w求P的导，再沿着梯度移动w。但是函数不连续无法进行。

为了摆脱阈值并得到连续的函数，增加一个输入w0=-1为权重为t，再做1/(1+e^-α)，（α是权重求和）得到连续的(0,1)的函数曲线

将两个神经连接在一起就得到了最简单的神经网络，将两层网络并列，每个神经元的结果可以链接到其他层的下一级神经元，就形成了神经网络的深度

L13 机器学习：基因算法

模拟染色体遗传，每次繁衍时在群体中按一定条件选择，将其特点传递给下一代，再加入一定的随机性模拟生物变异。

L14 机器学习：稀疏空间，音律学

与之前的神经网络，基因算法所用的（幼稚的）仿生学不同，接下来的内容是以工程师的角度解释如何让机器理解人能学习的内容。

复数化名词的例子，dogs z音带振动 cats s音不带振动。人们说同一句话，音波曲线中却可能截然不同。将声音曲线处理产生一连串辨别属性的向量，这些向量是二元的，例如判断是否是浊音，就是声带振动与否，如果振动就是浊音。音韵学中共有14种判断声音的辨别属性。所以理论上可以用2^14中单音。但一般一种语言都在100种以内，英语有40多种。用这14中属性分析一个单词

维度越高越容易分类，在14维的音律中分辨英语中的40中发音可以较为平均的分布在14维空间中

这是用类似实验的方法来发明AI算法，步骤如下：1.辨识问题 2.设计表示法 3.决定一种实现方法 4.挑选一个机制（设计算法） 5.实验

经常是在这几条中不断循环

通常计算机科学家喜欢用一种算法实现所有问题，但可能没有收获

L15 机器学习：近的miss，幸运情况

One shot learning，学习arch拱门的例子。每增加一个例子时机器学到一个一般化的属性，每增加一个near miss就增加一个特殊化的的属性。

学习就是想扇形的阵线不断向前拓展，在阵线后的是已经学到的知识，在阵线前的是还未学到的知识，在阵线上的是正在学习的知识

如何包装一个idea，5个s构成的星星symbol、slogan、surprise、salient、story

L16 机器学习：支援向量机

在不同的两类数据中画最宽的分解线。通过解拉格朗日乘子，数据中每个点对结果有影响。

L17 机器学习：Boosting

把失败率略小于50%的多种分类方法相组合，得到失败率较低的分类方法

L18 代表：类，轨迹，转变

人类讲故事结构，角色结构，有施加者和受害者（麦克白是施加者，邓肯是受害者）。人类语义网络语言内部有用的东西：

1.分类。（乐器、钢琴、贝森朵夫；工具、锤子、圆头锤；水果、苹果、mac）逐层具体从 一般->基础->特殊

2.转变。想象一辆车撞墙，车速、车墙距离、车况 三者在事前事中事后的变化。有 增、减、变化、出现、消失 5种加上5种的反面工10种来修饰

3.轨迹。物体沿着轨迹移动，施加者，用某工具，和某人一起，某受益人，通过某运输工具。通过加修饰来连接这些词构成语句，例如英语的介词

4.故事的顺序。将角色结构、转变、轨迹串起来故事库，就像父类和子类，事件->灾难、聚会->地震、飓风、生日、婚礼

写作时要减少读者的语法负担，减少注音（德语、俄语），不用“前者”“后者”，不用不同的词汇描述一个对象。

L19 架构：GPS，SOAR，前提，精神社会

L21 概率性接口

L23 模型融合，跨模型结合，课程总结