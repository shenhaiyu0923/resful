import psutil,time


print("CPU使用率   内存使用率    C盘使用率")
while True:
    time.sleep(2)
    print("  "
          +str(psutil.cpu_percent())+"%        "
          +str(psutil.virtual_memory().percent)+"%        "
          +str(psutil.disk_usage("c:\\").percent)+"%        "
          )