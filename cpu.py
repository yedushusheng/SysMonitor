import psutil

class CPUMonitor(object):
    #获取CPU信息
    def cpuInfo(self):
        print("CPU信息".center(20,'*'))

        #获取CPU逻辑核数(默认)
        cpuLogicCore = psutil.cpu_count()
        print("CPU(逻辑核数)：%d" % cpuLogicCore)
        #获取CPU物理核数
        cpuPhysicCore = psutil.cpu_count(logical=False)
        print("CPU(物理核数)：%d" % cpuPhysicCore)

        #获取CPU主频
        cpuFreq = psutil.cpu_freq()
        for index in range(len(cpuFreq)):
            cpuFreq[index]
        currnetCpuFreq = cpuFreq[0]
        minCpuFreq = cpuFreq[1]
        maxCpuFreq = cpuFreq[2]
        print("CPU主频(current):%d" % currnetCpuFreq)
        print("CPU主频(min):%d" % minCpuFreq)
        print("CPU主频(max):%d" % maxCpuFreq)

        #获取CPU状态
        cpuStatus = psutil.cpu_stats()
        for index in range(len(cpuStatus)):
            cpuStatus[index]
        #上下文切换时间
        ctx_switches = cpuStatus[0]
        print("上下文切换时间: %d" %ctx_switches)
        #中断
        interrupts = cpuStatus[1]
        print("系统中断:%d" % interrupts)
        #软中断
        soft_interrupts = cpuStatus[2]
        print("软中断:%d" % soft_interrupts)
        #系统调用
        syscall = cpuStatus[3]
        print("系统调用:%d" % syscall)

        #获取时间
        cpuTime = psutil.cpu_times()
        print(cpuTime)
        for index in range(len(cpuTime)):
            cpuTime[index]
        userTime = cpuTime[0]
        systemTime = cpuTime[1]
        idleTime = cpuTime[2]
        interruptsTime = cpuTime[3]
        dpcTime = cpuTime[4]
        print("用户执行进程时间:%f" % userTime)
        print("执行内核进程和中断时间:%f" % systemTime)
        print("CPU处于空闲状态时间:%f" % interruptsTime)
        print("DPC时间(Windows):%f" % dpcTime)
