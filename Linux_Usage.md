# Linux 常用指令

#### ps 查看当前活动进程
ps -fe|grep trojan (查找符合进程名的进程)

#### kill 杀死目标进程
kill -9 进程名

#### mv 移动文件
short for move 移动文件 格式为 mv +filename +destination

#### & 与 nohup的用法 （no hang up）
若使程序在后台运行 只需在命令行最后加上& ，让程序自动运行。 而nohup则是指不挂断程序，且输出重定向至当前目录下的nohup.out文件中，<必须以exit的方式退出终端！！！！>

#### jobs
查看任务nohup 的任务

#### wc -c 查看文件字节数 和stat +filename 命令一致

#### q! 退出并不保存修改	
