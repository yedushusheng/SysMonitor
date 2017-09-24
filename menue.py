from time import MonitorTime

class MonitorMenue(object):

    time = MonitorTime().Time()
    def Menue(self):
        print("系统监控平台".center('*',20))
        print("监控内容:" %'\n')
        print("CPU性能".ljust('-',5))
        print("内存性能".ljust('-',5))
        print("网络状态".ljust('-',5))
        print("进程监控".ljust('-',5))
        print("监控时间:%s".ljust('-',5) )
