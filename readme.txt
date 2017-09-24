System Monitor Project Base on Python(Linux)
1、搭建开发环境
开发平台：Windows
运行平台：Linux
开发工具：PyCharm
开发步骤：
    (1)下载Python IDE
       推荐使用PyCharm，也可以使用SublimeText3,Eclipse,VS
    (2)搭建GNU环境
       这里推荐使用MinGW
       技巧：安装MinGW后，运行msys.bat批处理文件，然后将PyCharm运行文件直接拖拽至命令行即可
2、安装Python插件
    pip install psutil

3、运行程序
    python /path/SysMonitor.py
    或者单独运行某一个监控程序：
    python /path/cpu.py