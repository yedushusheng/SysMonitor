import psutil

class MemMonitor(object):
    #内存监控
    def memInfo(self):
        print("Memory information".center(20,'*'))
        #获取虚拟内存大小
        memVirtual = psutil.virtual_memory()
        print("Virt mem:%s" %memVirtual)
        #获取交换分区大小
        memSwap = psutil.swap_memory()
        print("Swap mem:%s" %memSwap)
        #获取实际物理内存
        memPhysical = psutil._TOTAL_PHYMEM
        print("Phisical mem:%s" %memPhysical)

if __name__ == '__main__':
    mem = MemMonitor()
    mem.memInfo()