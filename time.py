import time

class MonitorTime(object):

    def Time(self):
        ticks = time.time()
        #return ticks
        print("当前时间戳为:%s" %ticks)

        #获取时间元组并打印基本信息
        localtime_tumple = time.localtime(ticks)

        '''print("本地时间元组:%s %s %s" % str(localtime_tumple.tm_hour)
                                    % str(localtime_tumple.tm_min)
                                    % str(localtime_tumple.tm_sec)
                )
        '''

        #格式化输出时间
        localtime = time.asctime(localtime_tumple)
        print(localtime)

if __name__ == '__main__':
    _time = MonitorTime()
    _time.Time()