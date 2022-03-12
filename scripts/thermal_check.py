import os

line = os.popen("acpi -t")
line = line.read()
charging = ""
#if line.__contains__("Charging"):
#    charging = "^"
line = line.split(" degrees")[0][-5:]
#line = line.strip()
if line[0] == " ":
    line = line[1:]
    #line.strip()

print(line+"\u00B0C")
