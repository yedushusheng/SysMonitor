import time

class MonitorTime(object):

    def Time(self):
        ticks = time.time()
        return ticks
        print("当前时间戳为:%s" %ticks)