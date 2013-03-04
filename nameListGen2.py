#!/usr/bin/python
# coding: UTF-8

from sys import argv
argc = len(argv)

if argc < 4:
    name       = raw_input("name:")
    class_name = raw_input("class:")
    num        = raw_input("image num:")
else:
    srcipt, name, class_name, num = argv


fnum = int(num) / 2

f = open("dataList1.txt", 'w')
f.truncate()

f.write(str(fnum))
f.write("\n")

f2 = open("dataList2.txt", 'w')
f2.truncate()

f2.write(str(fnum))
f2.write("\n")

for i in range(int(fnum)):
    
    j = i * 2
    f.write(name + "_" + str(j + 1) + "_crop.png")
    f.write(" ")
    f.write(name + "_" + str(j + 1) + "_depthcrop.png")
    f.write(" ")
    f.write(name + "_" + str(j + 1) + "_maskcrop.png")
    f.write(" ")
    f.write(class_name)
    f.write(" ")
    f.write(str(int(j) * 6))
    f.write("\n")
    
    k = j + 1;
    
    f2.write(name + "_" + str(k + 1) + "_crop.png")
    f2.write(" ")
    f2.write(name + "_" + str(k + 1) + "_depthcrop.png")
    f2.write(" ")
    f2.write(name + "_" + str(k + 1) + "_maskcrop.png")
    f2.write(" ")
    f2.write(class_name)
    f2.write(" ")
    f2.write(str(int(k) * 6))
    f2.write("\n")
    
f.close()
f2.close()
