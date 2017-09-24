from __future__ import print_function
import psutil
import sys
import datetime
import time

#秒转为小时
def SecToHour(secs):
    mm , ss = divmod(secs,60)
    hh , mm = divmod(mm,60)
    return ("%02d:%02d:%02d") %(hh,mm,ss)

#将时间转换为年:月:日的形式
'''易错：strftime("%年-%月-%日-%时:%分：%秒")'''
def ModifyTime(time):
    newtime = datetime.datetime.fromtimestamp(time).strftime("%Y-%m-%d-%H:%M:%S")
    return newtime

class MiscMonitor(object):
    #获取用户信息
    def userInfo(self):
        print("用户信息".center(20,'*'))
        userinfo = psutil.users()
        print(type(userinfo))
        for index in userinfo:
            #获取用户名
            username = index[0]
            print(username)
            #获取终端
            terminal = index[1]
            print(terminal)
            #获取主机IP
            host = index[2]
            print(host)
            #获取启动时间
            started = index[3]/3600
            print(started)
            #获取PID
            pid = index[4]
            print(pid)


    #获取开机时间
    def bootTime(self):
        print("开机时间".center(20,'*'))
        startTime = psutil.boot_time()
        print(ModifyTime(startTime))

    #获取电池信息
    def Battery(self):
        print("电池监测".center(20,'*'))
        if not hasattr(psutil,"sensors_battery"):
            return sys.exit("平台不支持")
        battery = psutil.sensors_battery()
        if battery is None:
            return sys.exit("未检测到电池")
        #后面的%%是为了输出百分号
        print("电池: %s%%" %round(battery.percent,2))

        #判断电池是否充满
        def BatteryStatus(percent):
            if(percent < 100):
                status = "正在充电"
            else:
                status = "已充满电"
            return status

        #判断是否插电
        if battery.power_plugged:
            print("剩余电池时间:%s" %(SecToHour(battery.secsleft)))
            print("状态:%s" % (BatteryStatus(battery.percent)))
            print("插座充电")
        else:
            print("剩余供电时间:%s" % (SecToHour(battery.secsleft)))
            print("状态:%s" %("未充电"))
            print("未插入插座")
