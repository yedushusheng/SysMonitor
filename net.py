import psutil
import time
import netifaces

class NetMonitor(object):
    def __init__(self,pernic=True):
        self.pernic = pernic

    #获取网络信息
    def netInfo(self):
        print("Net information".center(20,'*'))
        #获取网络总IO信息
        netTotalIO = psutil.net_io_counters()
        print(type(netTotalIO))
        print(netTotalIO)


        #获取每个网络接口的IO信息
        counter = psutil.net_io_counters(pernic=True)

        #获取网络ip地址
        netIP = psutil.net_if_addrs()
        #获取网络状态
        netStatus = psutil.net_if_stats()
        #获取网络连接种类
        netConn = psutil.net_connections()


