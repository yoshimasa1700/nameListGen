#!/usr/bin/python
# coding: UTF-8

from sys import argv
argc = len(argv)

if argc < 6:
    name       = raw_input("name:")
    width      = raw_input("image width:")
    height     = raw_input("image height:")
    class_name = raw_input("class:")
    num        = raw_input("image num:")
else:
    srcipt, name, width, height, class_name, num = argv


f = open(name+".txt", 'w')
f.truncate()

f.write(num)
f.write("\n")

for i in range(int(num)):
    f.write(name + "_" + str(i + 1) + "_crop.png")
    f.write(" ")
    f.write(name + "_" + str(i + 1) + "_depthcrop.png")
    f.write(" ")
    f.write(name + "_" + str(i + 1) + "_maskcrop.png")
    f.write(" ")
    f.write('0')
    f.write(" ")
    f.write('0')
    f.write(" ")
    f.write(width)
    f.write(" ")
    f.write(height)
    f.write(" ")
    f.write(str(int(width)/2))
    f.write(" ")
    f.write(str(int(height)/2))
    f.write(" ")
    f.write(class_name)
    f.write(" ")
    f.write(str(int(i) * 6))
    f.write("\n")
f.close()
