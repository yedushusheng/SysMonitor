import psutil

class DiskMonitor(object):
    # 获取磁盘信息
    def diskInfo(self):
        print("磁盘信息".center(20,'*'))
        #获取磁盘完整信息
        diskAllInfo = psutil.disk_partitions()
        #获取磁盘总的IO个数
        diskIO = psutil.disk_io_counters()
        #获取磁盘分区信息
        diskPartition = psutil.disk_usage('/')

if __name__ == '__main__':
    disk = DiskMonitor()
    disk.diskInfo()