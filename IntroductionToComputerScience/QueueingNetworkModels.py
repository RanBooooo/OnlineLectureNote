##队列网络模型
##符合经济规律，当资源有限时，需要排队来等待服务，例如超市收银台
##客户服务与资源利用率之间的平衡
##因为需求的出现时间是不确定的

##建模

##一份任务 -> 进入队列 -> 服务器 -> 离开

##任务到达过程，一个个来或者成群结队的，称为到达的时间分布（inter-arrival time distribution）
##有常规间隔、常数间隔、但往往是随机到达的泊松过程，结果为指数分布

##服务机制
##服务用时的分布，有两个因素决定：任务量和服务器的速度
##服务器的数量和队列的数量，单队列效率更高,但不一定有空间
##是否有优先权

##队列的特性
##三种处理方式：
##先进先出FIFO
##后进先出LIFO
##最短的剩余处理时间（shortest remaining processing time）SRPT其特点是快速处理短任务，使队列中的任务数量少，避免阻塞，也可减少平均等待时间，但在实际生活中运用不多，因为认为不公平
##平均等待时间是多长 是否有等待时限
##平均队列长度是多长 是否有队列长度限制

##服务器利用率

##MIT短驳车模拟队列程序
##抽象数据类型
##class Job(object)（包含：任务到达率、任务所需时间、记录等待时间的属性）
##class Passenger(Job) pass
##class JobQueue（包含：任务list、入list的方法、查询队列长度的方法。不包含出列方法，在子类中实现）
##class FIFO(JobQueue)（包含：出列的方法）
##class Srpt(JobQueue)（包含：取用时最短的任务的方法）
##class BusStop(FIFO) pass
##class Bus(object)（包含：容量、速度、乘客数量、上下车方法（乘客数量加减）、unload方法（下车直到没有乘客））
##运用以上类的simBus方法
##def simBus(bus，numStop = 6, loopLen = 1200, meanArrival = 90, meanWork = 10, simTime = 30000)
##伪代码：创建车站并初始化
##whild未超时
  ##移动bus
  ##乘客到达车站
  ##if有车在车站
  	 ##下客
  	 ##上客
##计算统计结果