## UC Berkeley Computer Graphics Lecture

### 加州大学伯克利分校计算机图形学



####L1-V1: 课程概述
本课程需要坚实的编程基础，不需要预先了解CG方面的知识，全部课程用C++实现，对数学线性代数有一定要求，之后的课程会复习CG相关数学知识

####L1-V2: 计算机图形学发展史
60年代的渲染算法有“隐藏线算法”，“隐藏表面算法”，可见性=排序。70年代光照算法漫反射光照，高光光照，曲面材质，Z-Buffer隐藏表面。八九十年代全局光照算法，包括：光线追踪、光辐射和渲染等式。目前人们追求的是照片般真实的渲染效果，甚至实现实时渲染

####L2-V3~4: 基础数学：点积 叉积
向量可以用来表示偏移、位移和位置。向量的加法a+b=b+a。

#####向量乘法：

点积（数量积）a·b=$\begin{vmatrix}a\end{vmatrix}\begin{vmatrix}b\end{vmatrix}$·cosθ   a·b=$x_ax_b+y_ay_b$。点积在CG中的应用：找到两个向量的夹角（例如找到光源和表面夹角的cos值用于shading），找到一个向量在另一个的投影（例如点在任意坐标系中的坐标）。优点是计算容易。

叉积（向量积）几何意义：垂直于$\vec a$、$\vec b$的向量$\vec c$，模为$\begin{vmatrix}c\end{vmatrix}=\begin{vmatrix}a\end{vmatrix}\begin{vmatrix}b\end{vmatrix}$·sinθ方向遵守右手定则。
$$
a×b =
	\begin{pmatrix}
	y_az_b - y_bz_a \\
	z_ax_b - x_az_b \\
	x_ay_b - y_ax_b \\
	\end{pmatrix}
\\
a×b=A^*b=
	\begin{pmatrix}
	0 & -z_a & y_a \\
	z_a & 0 & -x_a \\
	-y_a & x_a & 0 \\
	\end{pmatrix}
	\begin{pmatrix}
	x_b \\
	y_b \\
	z_b \\
	\end{pmatrix}
$$
####L2-V5: 基础数学：正交基础/坐标系
对于表示点、位置和地点非常重要
通常有许多组坐标系统（不只是X，Y，Z）。全局、本地、世界、模型、模型的一部分（头、肩膀、躯干、手）
接下来的三讲都与之有关，很重要的是：在统一的参考坐标系中得到所有的对象，在不同的坐标系中变换

#####何为坐标？
任何三个相互正交的单位向量：

$$
\begin{Vmatrix}
	u \\
	\end{Vmatrix}
	=
	\begin{Vmatrix}
	v \\
	\end{Vmatrix}
	=
	\begin{Vmatrix}
	w \\
	\end{Vmatrix}
=1
\\
u·v=v·w=u·w=0
\\
w=u×v
$$
一个点p在uvw构建的坐标系中
$$p = (p·u)u+(p·v)v+(p·w)w$$
#####如何构建坐标系，为什么要构建坐标系？
通常的情况是给于一个向量a（作业1中视角朝向），想要构建一个标准正交基，所以需要第二个坐标b（作业1中摄像机向上的方向）（例如作业讲世界坐标系中的物体转变到摄像机坐标系）
直观地讲，你需要讲向量w与a相关联，向量v与b相关联，但a、b既不是正交向量也是不单位向量，还需找到u向量
$$
w=\frac a{\begin{Vmatrix}a \\\end{Vmatrix}}
\\
\vec u = {b×w \over \begin{Vmatrix}b×w \\\end{Vmatrix}}
\\
v=w×v
$$
如果a与b平行，即b×w=0，则无法创建坐标系

####L2-V6: 基础数学：矩阵
矩阵可以用来变换点（向量）
移动，旋转，剪切，缩放
#####何为矩阵？
数字数组（m×n m行n列）
矩阵加法、乘以一个倍数
矩阵与矩阵相乘，第一个矩阵的列数要等于第二个的行数，积的（i,j）元素是第一个矩阵的行与第二个矩阵j列的点积
#####矩阵-向量 乘法
把向量看做一个一列的矩阵（m×1）
例如：关于y轴的2D反射
$$
\begin{pmatrix}
	-1 & 0 \\
	0 & 1 \\
	\end{pmatrix}
	\begin{pmatrix}
	x \\
	y \\
	\end{pmatrix}
=
	\begin{pmatrix}
	-x \\
	y \\
	\end{pmatrix}
$$

#####矩阵（向量）转置
$$
\begin{pmatrix}
	1 & 2 \\
	3 & 4 \\
	5 & 6 \\
	\end{pmatrix}^T
=
	\begin{pmatrix}
	1 & 3 & 5\\
	2 & 4 & 6\\
	\end{pmatrix}
$$

$$(AB)^T=B^TA^T$$
#####单位矩阵和逆矩阵
$$
I_{3×3}=
	\begin{pmatrix}
	1 & 0 & 0 \\
	0 & 1 & 0 \\
	0 & 0 & 1 \\
	\end{pmatrix}
$$

$$AA^{-1}=A^{-1}A=I$$
$$(AB)^{-1}=B^{-1}A^{-1}$$
#####向量以矩阵的形式做乘法
点积
$$
a·b=a^Tb
\\
\begin{pmatrix}
	x_a & y_a & z_a \\
	\end{pmatrix}
	\begin{pmatrix}
	x_b \\
	y_b \\
	z_b \\
	\end{pmatrix}
=(x_a x_b + y_a y_b + z_a z_b)
$$

叉积
$$
a×b=A^*b=
	\begin{pmatrix}
	0 & -z_a & y_a \\
	z_a & 0 & -x_a \\
	-y_a & x_a & 0 \\
	\end{pmatrix}
	\begin{pmatrix}
	x_b \\
	y_b \\
	z_b \\
	\end{pmatrix}
$$

其中$A^*$是向量a的伴随矩阵

####L3-V7: 转换1：复合转换
经常需要用到复合转换，例如先扩大2倍再旋转45度
用矩阵的好处是：转换后仍是矩阵，
不可改变顺序，受顺序的影响
#####复合转换求逆
如果要逆转一个由三个转换组成的复合转换
方法一：找到复合矩阵，求逆
方法二：倒序分别求逆
举例
$$
M = M_1 M_2 M_3
\\
M^{-1} = M_3^{-1} M_2^{-1} M_1^{-1}
\\
M^{-1} M = M_3^{-1} (M_2^{-1} (M_1^{-1} M_1) M_2) M_3
$$

####L3-V8: 转换1：3D旋转
在2D情况下
旋转后的向量等于旋转矩阵乘以原向量
$$
\begin{bmatrix}
	x' \\
	y' \\
	\end{bmatrix}
	=
	\begin{bmatrix}
	cos𝜃 & -sin𝜃\\
	sin𝜃 & cos𝜃 \\
	\end{bmatrix}
	\begin{bmatrix}
	x \\
	y \\
	\end{bmatrix}
$$

直角时 
$$
R^T R = I （单位矩阵）
$$

在3D情况下
基于某一坐标轴的旋转，很简单
$$
R_z=\begin{pmatrix}
	cos𝜃 & -sin𝜃 & 0 \\
	sin𝜃 & cos𝜃 & 0 \\
	0 & 0 & 1 \\
	\end{pmatrix}
\\
R_x=\begin{pmatrix}
	1 & 0 & 0 \\
	0 & cos𝜃 & -sin𝜃 \\
	0 & sin𝜃 & cos𝜃 \\
	\end{pmatrix}
\\
R_y=\begin{pmatrix}
	cos𝜃 & 0 & sin𝜃 \\
	0 & 1 & 0 \\
	-sin𝜃 & 0 & cos𝜃 \\
	\end{pmatrix}
$$

#####3D旋转几何上的解释
矩阵的行是新坐标系中的三个单位向量
能够从三个垂直的向量构建旋转矩阵

$$
R_{uvw}=\begin{pmatrix}
x_u & y_u & z_u \\
x_v & y_v & z_v \\
x_w & y_w & z_w \\
\end{pmatrix}
$$
此处
$$u=x_u X + y_u Y + z_u Z$$
v、w也是如此

u、v、w是三个互相垂直的单位向量

旋转矩阵乘以一个点，
旋转矩阵乘以向量P
$$
R_p=\begin{pmatrix}
	x_u & y_u & z_u \\
	x_v & y_v & z_v \\
	x_w & y_w & z_w \\
	\end{pmatrix}\begin{pmatrix}
	x_p \\
	y_p \\
	z_p \\
	\end{pmatrix}=\begin{pmatrix}
	u·p \\
	v·p \\
	w·p \\
	\end{pmatrix}
$$
即P在uvw构成的新坐标系中的投影
总结
旋转矩阵的行是新坐标系的3个单位向量
可以从3个垂直的向量构建旋转矩阵
即点在新坐标系中的投影
#####任意旋转公式
b关于轴a旋转角度𝜃（其他旋转的方式乌拉角和四元数）

三步公式

第一步：b由两个向量组成，一个与a垂直的b⟂，一个与a平行的b∥
旋转时b⟂保持不变，
$$
b_∥=(a·b)\vec a
\\
b_⟂=b-b_∥
$$

第二步：定义一个向量c，它垂直于a与b。
用叉积实现求c,$c= \vec a × \vec b$

第三步：考虑b⟂
$$
\vec c sin𝜃
\\
b_⟂ cos𝜃
\\
b_∥
$$

合并在一起的公式如下：
$$
(b_⟂ a)_{ROT}=(I_{3×3} - a a^T cos𝜃) b + (A^* sin𝜃) b
\\
(b_∥ a)_{ROT} = ( a a^T ) b
\\
R(a,𝜃) = I_{3×3} cos𝜃 + a a^T(1-cos𝜃) + A^* sin𝜃
$$

####L4-V9: 转换2：法线的转换
法线在很多绘图任务中起重要作用，例如光照
物体表面亮度取决于光源与表面法线的夹角
物体表面的高光取决于视角、法线和光源
#####找到法线的转换
物体表面切线为t 法线为n 法线与切线垂直所以$n·t=0$即$n^T t = 0$
当t转换为Mt,n转化为Qn 求Q
代入  $n^T Q^T Mt = 0 \quad ⇒ \quad Q^T M = I$
得出  $Q = (M^{-1})^T$ 

####L4-V10: 转化2：旋转复习，坐标系
之前都讨论的是点
但同样也可坐标系的移动
点左移 可以视为坐标系右移
点逆时针旋转 可以视为坐标系顺时针旋转

####L4-V11: gluLookAt
之前已经学习了所有要用到的数学工具
#####案例学习：获取gluLookAt
定一个摄像机作为构图的基础
gluLookAt(eyex, eyey, eyez, centerx, centery, centerz, upx, upy, upz)
摄像机坐标是eye 看这center 向上的方向是up
#####构建坐标系uvw
$$
w=\frac a{\begin{Vmatrix}a \\\end{Vmatrix}}
\qquad
u = {b×w \over \begin{Vmatrix}b×w \\\end{Vmatrix}}
\qquad
v=w×v
$$
目标是相机设置在原点，向-z方向看去
因此向量a由$eye-center$获得
向量b就是up方向
步骤：为相机创建坐标系，定义旋转矩阵，给相机（eye）应用适当的位移。
不能先旋转后位移，必须先位移（把相机移到原点）再施加旋转
合并位移和旋转
$$
P' = (RT)P = MP = R(P+T)=RP+RT \\
M = \begin{pmatrix} 
R_{11} & R_{12} & R_{13} & 0 \\
R_{21} & R_{22} & R_{23} & 0 \\
R_{31} & R_{32} & R_{33} & 0 \\
0 & 0 & 0 & 1 \\ \end{pmatrix}
\begin{pmatrix} 
1 & 0 & 0 & T_x \\
0 & 1 & 0 & T_y \\
0 & 0 & 1 & T_z \\
0 & 0 & 0 & 1 \\ \end{pmatrix}
=\begin{pmatrix} 
R_{3×3} & R_{3×3}T_{3×1} \\
0_{1×3} & 1 \\ \end{pmatrix}
$$
以上就是gluLookAt的原理

####L5-V12: 视图：正交投影
最终我们看CG图像是以2D的形式，
以类似人眼和相机的模式将3D物体投影为2D
到目前为止我们学习了转化（移动，旋转，缩放）可视为4×4均匀矩阵
目前它最后一行永远是 0 0 0 1。 最后w分量永远是1
对于视图（透视）我们会让最后一行和w分量不再是1（必须除以它）
#####大纲
正交投影（简单的）
透视投影，基本概念
获取gluPerspective（课件：glFrustum）
简要讨论非线性z布局（nonlinear mapping in z）
#####投影
得到低维度（自处3D->2D）
保留直线
琐碎的例子：丢掉一个坐标（正交）
变化立方体的例子，通过位移和缩放（大M 4×4均匀矩阵），把立方体移到原点再缩放成单位正方体
将其运用到世界中的某一部分，就是正交投影

####L5-V13: 视图：透视投影
最常见的CG，艺术和可视系统
近大远小（尺寸和距离成反比）
平行线不平行，汇聚成一点
eye和世界中的两点构成三角形，与这两点在投影平面上两点是相似三角形，用公式可以计算出投影平面上的两点
#####投影屏幕的俯视图
eye和世界中的一点(x, y, z)，连线经过投影屏幕的到一点(x', y', d)，d是eye到屏幕的距离。
构成一对相似三角形,得到:
$ x' = { d×x \over z } $
$ y' = { d×y \over z } $
#####矩阵计算
$$
	\begin{pmatrix}
	1 & 0 & 0 & 0 \\
	0 & 1 & 0 & 0 \\
	0 & 0 & 1 & 0 \\
	0 & 0 & -{1 \over d} & 0 \\
	\end{pmatrix}
	\begin{pmatrix}
	x \\ y \\ z \\ 1 \\
	\end{pmatrix}
	=
	\begin{pmatrix}
	x \\ y \\ z \\ - {z \over d} \\
	\end{pmatrix}
	=
	\begin{pmatrix}
	- { d×x \over z } \\ - { d×y \over z } \\ -d \\ 1 \\
	\end{pmatrix}
$$
####L5-V14: 视图：gluPerspective
gluPerspective有四个参数，视野范围（field of view, 缩写fov）、宽高比例、近平面、远平面
视图截头锥体,锥体边延长线交于摄像机
gluPerspective(fovy, aspect, zNear>0, zFar>0)
fovy = field of view in y direction视野范围在y轴上的距离
Fovy，aspect控制在x，y方向上的视野范围
zNear，zFar控制视图截头锥体
fovy还决定了点与eye连线和z轴的夹角θ
$θ = { fovy \over 2 }$   $ d = cotθ $
#####矩阵计算
简单形式：
$$
P = 
	\begin{pmatrix}
	{ 1 \over aspect} & 0 & 0 & 0 \\
	0 & 1 & 0 & 0 \\
	0 & 0 & 1 & 0 \\
	0 & 0 & -{1 \over d} & 0 \\
	\end{pmatrix}
$$
考虑宽高比
齐次化，乘以d更加简单
必须基于远近平面映射z的值

因为是齐次坐标所以可以整个乘以d，得到：
$$
P = 
	\begin{pmatrix}
	{ d \over aspect} & 0 & 0 & 0 \\
	0 & d & 0 & 0 \\
	0 & 0 & A & B \\
	0 & 0 & -1 & 0 \\
	\end{pmatrix}
$$
选择A和B来分别匹配n和f从-1到1
对右下的2x2矩阵进行计算来使z正确匹配（不考虑x和y）
#####获得z映射
$$
	\begin{pmatrix}
	A & B \\
	-1 & 0 \\
	\end{pmatrix}
	\begin{pmatrix}
	z \\
	1 \\
	\end{pmatrix}
	=
	\begin{pmatrix}
	Az + B\\
	-z \\
	\end{pmatrix}
	= -A - {B \over z}
$$
此处看成只对z求齐次坐标，最后去转化为笛卡尔坐标$ -A - {B \over z} $

联立等式,来考虑近/远平面正确的位置
$z = -n → -1$        $ -A + { B \over n} = -1$
$z = -f → +1$        $ -A + { B \over f} = +1$
等式替换得到B的公式，再做替换得到A的公式
$A = - {f+n \over f-n}$
$B = - {2fn \over f-n}$
#####z的映射是非线性的
$$
	\begin{pmatrix}
	Az + B\\
	-z \\
	\end{pmatrix}
	= -A - {B \over z}
$$
许多提出的映射都包含非线性
优势：能够处理深度范围（10cm - 100m）
劣势：深度分别率不统一，靠近近平面分辨率更高，越远越低
常见错误：不能设置近平面距离为0，会丢失深度分辨率
#####视图管线
模型坐标→模型变化→世界坐标→相机变换（gluLookAt）→eye坐标→透视变化（gluPerspective）→屏幕坐标→视窗变化→窗口坐标→光栅变换→设备坐标

####L6-V15: OpenGL1：总览
OpenGL是图像API（abstract programming interface）
是某一图像硬件与程序员之间的抽象层，独立于硬件平台可移植的软件库，统一的指令集
例如GLUT和GLM是建立在OpenGL之上的
#####为何需要OpenGL？
封装许多基础2D/3D功能
使用了高级语言C++
作为先驱，指导了DirectX，WebGL，Java3D等的发展

####L6-V16: OpenGL1：缓冲区和矩阵
#####缓冲区和窗口交互
缓冲区类型：色彩（前，后，左，右（左右用于立体成像，本课程不考虑）），深度（z），积聚，刻板。
当绘图时，你写缓冲区（最简单的，前后缓冲区），你会用到Z-Buffer来只绘制直接可见的物体，把后面的物体去掉
OpenGL不包含任何窗口操作，以提高可移植性
但可以使用GLUT（Motif，GLX，Tcl/Tk）来实现键鼠交互
#####Open中的视图
视图由两部分组成：
1. 物体的位置：模型-视图 变化矩阵
2. 视图投影：投影变化矩阵

老OpenGL中（任然支持），2两个矩阵栈：
GL_MODELVIEW_MATRIX，GL_PROJECTION_MATRIX
能够在栈上压入和弹出矩阵

新OpenGL中，使用了C++的STL标准库来按需建立栈：
例如stack<mat4> modelview; modelview.push(mat4(1.0));
GLM库替换了许多过时的指令，包括mat4

OpenGL的摄像机永远在原点指向Z轴负方向
变化把物体相对于摄像机来移动
老OpenGL中矩阵是列优先的（会引起很多误会，应为标准数学上是行优先）右乘在栈顶（你放一个矩阵到栈上，会首先应用这个变换，代码里最后一个变化却是第一个应用的）
新OpenGL中。矩阵是行优先的但是仍然是右乘，所以让人困惑（）亲仔细阅读作业和文档


####L6-V17: OpenGL1：窗口系统与回调
简单介绍了glut响应按键、窗口变形、鼠标等交互的方法的代码

####L6-V18: OpenGL1：绘图
在设置了Buffer和回调后，要开始显示几何体网格了
OpenGL提供了很多基础的几何体网格：点、线、多边形、三角形、四边形、四边形条、三角条、三角扇
#####几何体网格
点（GL_POINTS） 存储在同质坐标中
线段（GL_LINES）
多边形：简单的，凸的（尝试凹的），镶嵌的，复杂图像使用GLU，矩形：glRect
特殊情况（条，环，三角，扇，四边形）
更多复杂基础几何体（GLUT）：圆球，茶壶，方块

OpenGL绘图经过升级，由老版升级到新版,有人认为老版更容易理解，新版用的是点缓冲区对象，老版本目前任然支持
#####老OpenGL绘图
在glBegin和glEnd之间装入一系列的点
可以包含一般的C代码和属性例如颜色
指令有例如glVertex3f，glColor3f（C语言没有函数重载，3f表示3个浮点型的输入）
属性必须在vertex之前，例如建一个点，先颜色glColor3f再点glVertex3f（因为C代码是状态机实现，要先改颜色再建点）
装配线（传入顶点，变换，阴影）
这些顶点，片段着色器在当前GPU上
立即模式：发送给服务器并绘制（你发出的指令立即被OpenGL处理）
保持模式：它保持住，可以复用和优化（事实上新OpenGL点缓冲区对象其实就是快速高效的保持模式算法）
客户端-服务器模型（客户端生成顶点，服务器端绘制）即使在同一计算机上
glFLush()迫使客户端发送网络包
glFinish()等待应答，保守的使用同步
#####新OpenGL：顶点缓冲对象（更优雅、更高效，同时也更复杂）
代码：很复杂难以理解，OpenGL标准语式
大致是定义顶点、颜色、序号、缓冲区，再绑定缓冲区。
再初始化绘图和着色器，顶点着色器和片段着色器共同构成着色器程序，shader文件是运行时编译的。

####L6-V19: OpenGL1：片段着色器
#####渲染管线
顶点->可编程顶点着色器->扫描转化（光栅化）->可编程片段着色器->帧缓冲区
图像->像素操作↑->材质内存↑
2003年以前，确切的函数管线（状态机）
2003年以后，可编程管线(Shader)

####L7-V20: OpenGL Shading：动机
物体的Shading对辨别物体的形状起着关键性的作用，例如这个红球在flat shading看着就是有明显的棱角，而用差值shading就能使其变得光滑。
#####颜色基础
RGA红绿蓝三色组成，R+G=黄，B+G=蓝绿色，B+R=品红，每个通道分开处理。显示器和印刷品不同。OpenGL常使用RGBA 32bit模式，每个通道8bit。zaiOpenGL中颜色规格化为0到1代表0~255。
#####顶点VS片段着色器
两者都能用来处理光照
顶点着色器用光栅化来计算差值（Gouraud （光滑）shading 如mytest1中，Flat shading没有差值）
要么计算顶点的颜色，和差值（老OpenGL中的标准方法，能用顶点着色器实现）
要么差值计算顶点的法线等
片段着色器计算每个像素的（Phong shading（与Phong光照不同）更精确）

####L7-V21: OpenGL Shading：Gouraud 与 Phong 着色器
#####Gouraud Shading
三角形三个顶点$I_1,I_2,I_3$。给予三个顶点颜色，接着OpenGL控制硬件做差值运算完成光栅化。
光栅化的过程：扫描线从上向下，线上的三点$I_a$（与$I_1 I_2$相交）$I_b$(与$I_1 I_3$相交)$I_p$（某一点）
求$I_a I_b$公式：
$$
I_a={ I_1 ( y_s - y_2 ) + I_2 ( y_1 - y_s ) \over y_1 - y_2 } \\
I_b={ I_1 ( y_s - y_3 ) + I_3 ( y_1 - y_s ) \over y_1 - y_3 }
$$
求$I_p$:
$$
I_p={ I_a ( x_b - x_p ) + I_b ( x_p - x_a ) \over x_b - x_a } 
$$
实际的方法效率比公式更高。完全不做除法，直接逐行增加一个量。这一过程称为扫描转换
#####Gouraud与错误
在极限的情况下
$I_1=0$由于N点乘E是负的
$I_2=0$由于N点乘L是负的
所以对$I_1$和$I_2$的差值都是0，所以之间就不可能产生高光，
防止这一错误的方法是将模型切分足够多的三角形
#####两种Phong（Phong shading和Phong光照）来营造高光
Phong shading就是用法线差值取代颜色差值
所以即使是在上面的极限情况中，差值计算法线，依然能在两个为0的点之间得到正确的法线。所以对光线整体的计算要针对每个像素。（老OpenGL中没有Phong shading 只有Gouraud所以极限情况必须拆分小三角面，新OpenGL中用Phong即可）
#####讲解顶点着色器代码
version 120越老越能与老版本兼容
三个变量color、mynormal和myvertex，要传递给片段着色器（version 130以上应该加out）
主函数中：
gl_TexCoord[0] = gl_MultiTexCoord0 ; // 贴图坐标。把从OpenGL中得到的设置为贴图坐标，之后会细讲贴图
gl_Postition = gl_ProjectionMatrix * gl_ModelViewMatrix * gl_Vertex ; // 把gl_Position设为投影矩阵、模型视图矩阵乘顶点
color = gl_Color ; // 赋予自己申明的变量来演示，OpenGL正在从顶点做差值运算，差值结果可以在片段着色器中使用
mynormal = gl_Normal ; // 
myvertex = gl_Vertex ; // 



####L7-V22: OpenGL Shading：光线与着色器
#####光源的类型
######点光源
位置（vec4），颜色（RGBA）
衰减  $ atten={1 \over k_c + k_l d + k_q d^2 } $(d是和光源的距离)
######衰减
通常假设没有衰减
点光源：二次方反比衰减$ k_q ≠ 0 $
线状光源：线性衰减代表
面光源：常数衰减代表（线状光源和面光源都假设物体与光源在较近距离）（若物体与线状/面光源很远可视为点光源）
不衰减代表平行光 
######平行光
（坐标为0(代表光源在无线距离)，没有衰减（$k_l k_q$为0））
#####材质属性（物体表面如何反射光）
需要法线（来计算有多少漫反射、镜面反射，寻找反射方向等等）
通常找到每个顶点的法线，再差值计算
GLUT自动为茶壶（程序化的模型）做了计算
可以手动计算参数表面的法线
对于复杂形状，可以求表面法线的平均值

4种shading模式：环境光，漫反射，镜面，放射
######辐射
例如太阳光、光源
（现实中）如果直接看光源，即使没有其他光照到光源上，还是会向你的方向照射光。
在OpenGL中，创建光源并不能看见它，而需要创建网格。能被看到的都是网格，网格被光源点亮，但你看不见光源（也看不到摄像机）。所以创建一个物体赋予辐射属性，设置颜色为白色，才能看见它一直发出白光。与不会辐射光的表面无关。
$$
I={Emission}_{material}
$$
(I强度)
######环境光
即使光没有直接照射到表面，仍然会有光在房间中折射，营造一种漫反射或环境光材质的感觉。模拟光在场景中的所有分布，这方面的研究很多，称为全局光照。最后会有一堂课讲到这方面的研究进展，称之为渲染等式。但环境光照其实很简单，因为光在场景中反射了很多次，最终光线分布近似于各个方向都相同。所以我们就简单的给于一个全局常量，让所有东西都能看得见。给整个场景设置一个环境光强度，一般设置得很低，如0.1，0.2。
$$
I=Ambient
$$
######漫反射
对应的是粗糙，不光滑的表面，例如墙面和没打磨的地板。CG中称为Lambert材质。
光线向所有方向均匀反射，是CG中的一个理想模型。其中关键的cosine衰减
$$
I=\sum^n_{i=0} {intensity}_{light\ i} * {diffuse}_{material} * {atten}_i * [{max}(L·N,0)]
$$
（N法线，L光线）
######镜面
对应表面光滑的物体。
入射方向和反射方向，平面上的法线，入射角等于反射角
但眼睛不在反射角上，所以一般都是rough reflection，如果是光滑镜子，只能又在反射角上有光线强度，在视角上没有强度
所以（反射角和视角）偏斜角度多大会影响反射光的量，所以反射光应该像一个扇叶，反射角强度最强，两侧强度减弱
#####Phong光照
最早在70年代中期发表，即使如今有许多更精准更真实的计算反射的方法，它依然被广泛使用。
Phong的想法是找到一种简单方法来处理视角相关的高光，并不需要真实。
用eye和反射光（关于表面法线）的点积，取cos
再把cos加一个指数来控制高光闪耀的程度。

有一个替换公式，取光源和时间间的半角，用来和法线求点积（和漫反射光照光线和法线的点积很像），再加一个指数
这就是所谓的Blinn-Phong模型，对于真实物理表面，半角公式更加准确。是OpenGL的标准公式。
######Phong公式
$$
I\sim (R·E)^p\\
R=-L+2(L·N)N
$$
（L光线，R反射角，E视角，N法线）
######Blinn-Phong公式
Blinn在Phong的基础上稍加修改
$$
I\sim (N·H)^p\\
I=\sum^n_{i=0} {intensity}_{light\ i} * {specular}_{material} * {atten}_i * [{max}(N·H,0)]^{shininess}
$$

####L7-V23: OpenGL Shading：片段着色器
讲解代码
#####shader设置
attribute关键字
color、mynormal、myvertex（对应V21中顶点着色器中定义的3个变量，version 130以上应该加in 修饰）
uniform关键字表示不随片段着色器变化的变量
#####shader变量
// 假设light 0是平行光，light 1是点光源。
// 实际光线值是主OpenGL程序传递来的
uniform vec3 light0dirn ;
uniform vec4 lighet0color ;
uniform vec4 light1posn ;
uniform vec4 light1color ;

// 设置材质参数，这些可以改变（不用uniform）或绑定缓冲区
// 但目前此处还是设置为uniform
uniform vec4 ambient ; // 环境光、漫反射、镜面都是vec4因为是颜色
uniform vec4 diffuse ;
uniform vec4 specular ;
uniform float shininess ;
#####计算光线函数ComputerLight
vec4 ComputerLight (const in vec3 direction, const in vec4 lightcolor, const in vec3 normal, const in vec3 halfvec, const in vec4 mydiffuse, const in vec4 myspecular, const in float myshininess){}
分别计算lambert和phong
lambert：bDotL=法线点乘光方向，在用漫反射*光颜色*max(bDotL，0.0)
phong：nDotH=法线点乘半向量，高光*光线颜色*pow(max(nDotH, 0.0),myshininess)
返回两者之和
#####main函数
变换，三个分支，如果是贴图，贴图决定片段颜色（忽略光）。如果是光=0，片段颜色=color。
其他情况，摄像机eye总在原点看向z负方向，设置const vec3 eyepos = vec3(0,0,0);
然后vec4 _mypos为用模型视图矩阵乘以顶点myvertex。得到vec3 mypos = _mypos.xyz/ _mypos.w(去均质化)得到了物体在eye中的3d位置，还用eyepos-mypos规格化得到点指向眼睛的方向eyedirn
为着色器计算法线，简单方法vec3 normal = normalize(gl_NormalMatrix * mynormal)
详细方法vec3 _normal = (gl_ModelViewMatrixInverseTranspose*vec4(mynormal,0.0)).xyz; vec3 normal = normalize(_normal);用MV矩阵的逆转置矩阵乘以normal，取xyz再规格化。
#####主线程
处理平行光和点光源
Light 0 平行光：规格化光线方向，与eyedirn相加再规格化得到half0，然后计算光vec4 col4 = ComputerLight(direction0, light0color, normal, half0, diffuse, specular, shininess);（上面定义的函数）
Light 1 点光源：先对光的位置最取均质化vec3 position = light1posn.xyz / light1posn.w;
再计算方向（无衰减）vec3 direction1 = normalize(position - mypos);再计算半向量half1最后计算光（同上）
最终相加取得最终结果gl_FragColor = ambient + col0 + col1;

####L8-V24: OpenGL2：网格
讲解代码
用参数构建几何体方块，
与顶点缓冲区绑定（除了颜色），
定义颜色，
绘制带不同颜色的立方体

####L8-V25: OpenGL2：矩阵栈
#####总结OpenGL顶点转化
物体坐标->模型视图矩阵->投影矩阵->透视除法->视窗转化->窗口坐标
完成以上操作需要矩阵栈

####L8-V26: OpenGL2：Z Buffer
60~70年代图形学的重大问题，关于可视性检测，或是移除隐藏的物体或点。此间产生了大量的解决方案，但最终被应用与OpenGL的方法却非常简单
深度检测又称Z-buffering
先讨论Double Buffering。
如果你要在场景里的老物体上绘制一个新物体，你刚绘制了老物体又用新物体替换，有种很蠢的赶脚，尤其在绘制速度很慢的时候
Double Buffering的想法是：你先渲染整个场景所有几何体到一个幕后的缓冲区，当渲染完以后，再切换缓冲区，这样整个屏幕是同步刷新的。你就不会等待一个接一个的物体绘制，也不会有闪烁。
#####显示的主函数中启用Double Buffering
glutInitDisplayMode(GLUT_DOUBEL | GLUT_RGB | GLUT_DEPTH);
...
glutSwapBuffers();
glFlush();
#####开启深度检测
OpenGL使用Z-buffer来进行深度检测
每个像素，存储最近的Z值（到相机的举例）
如果新的片段更近则用它代替老的像素的颜色和z值[可以在片段程序中复写]
简单技术却得到了准确的可见性
主函数中修改
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
初始化方法中
glEnable(GL_DEPTH_TEST);
glDepthFunc(GL_LESS); // 默认选项
需要占用大量内存，但由于内存价格的下降，已经被广泛使用

####L8-V27: OpenGL2：动画
初始化茶壶的颜色、朝向、位置、大小。动画函数不断位移。键盘控制播放暂停。

####L8-V28: OpenGL2：材质
#####代码 新的全局和基础设置
GLubyte	woodtexture[256][256][3] ; // 3维GLubyte数组存储贴图
GLuint texName[1] ; //贴图缓冲区
GLuint istex ; //
GLuint islight ; //
GLint texturing = 1 ; // 开关材质
GLint lighting = 1 ; // 开关光照
// 在Display中
glUniform1i(islight,0) ; // 关闭光线（除了茶壶）
glUniform1i(istex,texturing) ; 
drawtexture(FLOOR,texNames[0]) ; // 给地板添加贴图
// drawobject(FLOOR) ;
glUniform1i(istex,0) ; // 其他物体没有贴图
按键控制t键开关贴图，s键开关着色器
#####增加视觉细节
70年代提出的重要概念
基本概念：用图片替代更多的多边形，来代表精细的颜色变化
#####代码 设置贴图

####L9-V29: 光线追踪1：施加光线
#####真实照片所需的效果
（柔和的）阴影
反射（镜子和光亮的东西）
透明（水，玻璃）
相互反射（颜色混合）
复杂光照（自然景物，区域光照）
栩栩如生的材质（丝绒，绘画，玻璃）
#####光线追踪
照片合成所用的方法与OpenGL的硬件管线不同
逐像素而不是逐物体
容易计算阴影、透明等待（在游戏中实现方式与光线追踪不同）（有一些用渲染管线无法实现）
#####光线追踪的历史
40多年前开始研究
80年代重要的论文《递归光线追踪》
大量的研究关于不同的基础几何体，大量的研究关于加速器
目前的研究：
实时光线追踪（历史上是一个很慢的技术）
光线追踪架构
#####代码 
函数输入摄像机、场景、图片的宽和高
逐像素生成新图像
返回新图像
#####施加光线
生成一张与OpenGL光栅化一样的图片
逐像素的检验可见性，不用Z-buffer
向场景中发射光线找到最近的物体，再像OpenGL一样着色
######光线追踪
for循环遍历每个像素
for循环遍历每个物体
######光栅化
for循环遍历所有物体，考虑对应像素的颜色
#####图例
降价从视角向每个像素发射一道光线来决定这个像素最终的颜色，如果光线射到了一个不透明的物体近似于光栅化求颜色

####L9-V30: 光线追踪1：投影与反射
#####阴影（图例）
视角发射光线高物体，再从这点发射光线到光源，如果有遮挡就在阴影中，如果没有就不在阴影中
光栅化的实现shadow map：先存储到光源的深度，再存储到eye的深度。更加复杂
#####镜面反射/折射
光线照射到了镜面，重新计算光线方向得到物体的反射/折射
#####递归光线追踪
foreach 像素
追踪eye的光线找到交点
追踪接着的阴影光线向所有的光源 color = visible
追踪反射的光线 color +=reflectivity * color of reflected ray
#####递归的问题
反射光线可能无限追踪
一般设置最大递归深度（也可设置阈值，当反射小于一个阈值，例如0.02，停止光）
光传递同理（考虑折射）
阈值和递归深度的设置带有偏向性，还有一种叫俄罗斯轮盘赌的方法，反向累加能良来避免偏向性。

####L9-V31: 光线追踪1：光线-平面交叉
是光线追踪的核心，主要的研究领域之一；许多不同的基础类型（三角形、球形、方块等）都有优化的方法。
不同类型的信息，阴影光线：交叉/不交叉；基础光线：交叉点、材质、法线；贴图坐标。
例子：三角形，球形，多边形，一般隐藏的表面
#####光线-球形交叉
定义光线和球体的方法：
$光线 ≡ \vec P = \vec P_0 + \vec P_1 t$
P0是光线起点，P1是光线的方向，t是沿着光的参数，从零开始是正的对应沿着光的距离。
$球体 ≡ (\vec P - \vec C) · ( \vec P - \vec C ) -  r^2 = 0$
代入求交点
$球体 ≡ (\vec P_0 +\vec P_1 t - \vec C) · ( \vec P_0 +\vec P_1 t - \vec C ) -  r^2 = 0$
简化
$t^2 ( \vec P_1 · \vec P_1 ) + 2t \vec P_1 · ( \vec P_0 - \vec C ) + ( \vec P_0 - \vec C ) · ( \vec P_0 - \vec C ) - r^2 = 0$
解t有以下情况：
两个正实数根，取小的那个根就是与球体的第一个交点
两个交点相同，与球体相切
一个正根一个负根，表示起点在球体中，取正根
得到复数根表示没有交点
在解等式前要确定判别式（$Δ=b^2 - 4ac$）来判断根的情况
找到t的解后，将t代回$光线 ≡ \vec P = \vec P_0 + \vec P_1 t$中得到交点的坐标
还需要知道表面的法线，用来着色
在球体中$法线={\vec P - \vec C \over \begin{vmatrix} \vec P - \vec C \end{vmatrix}}$
#####光线-三角形交叉
先讨论一般化的光线多边形交叉，在检查这个交点是否在三角形中
三角形三个顶点A、B、C。求得法线（任意两个边向量叉积再规格化）。法线与平面内仍以一个向量的点积为0
平面的等式：
$平面 ≡ \vec P · \vec n - \vec A · \vec n = 0$
与光线的等式结合
$光线 ≡ \vec P = \vec P_0 + \vec P_1 t$
$(\vec P_0 + \vec P_1 t) · \vec n = \vec A · \vec n$
$t = { \vec A · \vec n -\vec P_0 · \vec n \over \vec P_1 · \vec n}$
当$\vec P_1 · \vec n = 0$即光线方向与法线方向垂直，没有交点
其他正常情况都能找到光线与平面的交点
######光线在三角形内
一旦和平面有交点，接着要确定交点是否在三角形内
一般多边形：一个点向无穷远做射线，如果与平面交叉了奇数次说明在平面内，如果交叉了偶数此说明在平面外
对于三角形：对三角形=各个顶点使用参数的质心坐标（有很广泛的应用例如贴图映射）
点P到三角形顶点A、B、C的举例分别是α、β、γ。取规格化，所以α + β + γ = 1。这就是三角形质心坐标
P = αA + βB + γC
α≥0 β≥0 γ≥0
α + β + γ = 1
从P替换A
P-A = β(B-A) + γ(C-A)
0≤β≤1，0≤γ≤1
β+γ≤1
接着能尝试在0≤β≤1，0≤γ≤1，β+γ≤1情况下求解。
用交点，有三个P的等式
但既然我们讨论的是平坦区域，其中一个变为变质了，就有了足够的等式来决定β和γ，从两个联立的等式
如果这三个等式成立，就说明P在三角形内，否则就不在
#####其他基础形状
许多光线追踪的研究关注光线与基础形状的交点测试
圆锥、圆柱、椭圆
盒子（对边界盒非常有用）
一般的平面多边形
其他
#####变形过的光线交叉
想象要检测光线和一个椭圆交叉
椭圆是进过拉伸变形的圆
假设球形经过矩阵M变换，则对光线作$M^{-1}$变换，再按光线-球形交叉求交点

####L9-V32: 光线追踪1：优化
介绍各种优化加速的方法
网格法：给空间分配网格，只检测光线经过的格子，格子相交的物体与光线检测

####L10-V33: 光线追踪2：相机施加光线
这堂课讨论光线追踪的具体细节，从摄像机光线施加说起
求光线的方向

####L10-V34: 光线追踪2：光线-物体交叉
复习 光线-物体交叉的具体细节

####L10-V35: 光线追踪2：光照

####L10-V36: 光线追踪2：递归光线追踪