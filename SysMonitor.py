from cpu import CPUMonitor
from mem import MemMonitor
from disk import DiskMonitor
from net import NetMonitor
from misc import MiscMonitor
from temperature import TempMonitor
from arch import ArchInfo
from process import ProcessMonitor

if __name__ == '__main__':
    cpu = CPUMonitor()
    cpu.cpuInfo()
    mem = MemMonitor()
    mem.memInfo()
    disk = DiskMonitor()
    disk.diskInfo()
    net = NetMonitor()
    net.netInfo()
    misc = MiscMonitor()
    misc.userInfo()
    misc.bootTime()
    misc.Battery()
    #TempMonitor.TempInfo(0)
    arch = ArchInfo()
    arch.SystemType()
    arch.SystemInfo()
    arch.PlatformInfo()

    process = ProcessMonitor()



