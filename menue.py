from time import MonitorTime

class MonitorMenue(object):

    time = MonitorTime().Time()
    def Menue(self):
        print("System Monitor platform".center('*',20))
        print("Monitor item:" %'\n')
        print("CPU information".ljust('-',5))
        print("Mem information".ljust('-',5))
        print("Net status".ljust('-',5))
        print("Process status".ljust('-',5))
        print("Monitor time:%s".ljust('-',5) )


if __name__ == '__main__':
    menue = MonitorMenue()
    menue.Menue()