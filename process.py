import os,sys,logging

class ProcessMonitor(object):
    def __init__(self,pernic=True):
        self.pernic = pernic
	
	def process_info(self):
		os.system("top | awk '{printf $2}'")
		pass

		

