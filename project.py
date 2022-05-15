a = open("b.txt")
b = open("a.txt")

switch = a.read()
switch2 = b.read()

read2 = open("a.txt", "w")
read3 = open("b.txt", "w")

read2.write(switch)
read3.write(switch2)