import platform


class ArchInfo(object):
    #定义属性
    global SYS_TYPE
    global SYS_BIT
    Windows = None
    Linux = None
    OTHER = None

    #定义类的初始化函数
    def __init__(self):
        self.SYS_TYPE = None
        self.SYS_BIT = None
        self.Windows = None
        self.Linux = None
        self.OTHER = None

    def PlatformInfo(self):
        print("平台信息".center(20,'*'))
        plat = platform.platform()
        print(plat)


    def SystemInfo(self):
        print("系统消息".center(20,'*'))
        system = platform.system()
        print(system)


    def SystemType(self):
        print("系统类型".center(20,'*'))
        plat = platform.architecture()
        sys_bit,sys_type = plat
        '''
        等价于：
        sys_bit = plat[0]
        sys_bit = plat[1]
        '''
        #判断系统位数
        if "64" in sys_bit:
            self.SYS_BIT = 64
        elif "32" in sys_bit:
            self.SYS_BIT = 32
        else:
            self.SYS_BIT = None

        #判断系统类型
        #将元组转为字符串，然后利用字符串的startswith方法判断
        if str(sys_type).startswith('Win'):
            self.SYS_TYPE = self.Windows
        #也可用in判断
        elif "Linux" in sys_type:
            self.SYS_TYPE = self.Linux
        else:
            self.SYS_TYPE = self.OTHER
            print("Warnning:Not Support!")
        print(sys_type)


        return self.SYS_TYPE

