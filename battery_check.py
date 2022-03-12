import os

line = os.popen("acpi -b")
line = line.read()
charging = ""
if line.__contains__("Charging"):
    charging = "\u26A1"
line = line.split("%")[0][-3:]
line = line.strip()

#symbols = "%\u25D8"

if line[0] == ",":
    line = line[1:]
    line.strip()
    #symbols = "%\u25D9"

print(charging+line+"%")
