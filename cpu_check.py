import os

line = os.popen("sar -u 1 1")
line = line.read()
line = line.split("\n")
line = line[3].split()
idle = line[7]
cpu_usage = 100.0 - float(idle)
print("%.2f" % cpu_usage, end="")
print("%")
