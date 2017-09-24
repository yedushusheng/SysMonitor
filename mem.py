import psutil

class MemMonitor(object):
    #内存监控
    def memInfo(self):
        print("内存信息".center(20,'*'))
        #获取虚拟内存大小
        memVirtual = psutil.virtual_memory()
        #获取交换分区大小
        memSwap = psutil.swap_memory()
        #获取实际物理内存
        memPhysical = psutil._TOTAL_PHYMEM