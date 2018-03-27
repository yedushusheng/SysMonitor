import psutil
import sys
class TempMonitor(object):
    def TempInfo(self):
        temperature = psutil.sensors_temperatures()
        print(temperature)
        sys.exit()

if __name__ == '__main__':
	temp = TempMonitor()
	temp.TempInfo()