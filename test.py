import os
import time

s = time.time()

count = 0

inp = open("input.txt", "r")

ilist = inp.read().split(" |\n")

inp.close()

for i in range(len(ilist)-1):

    xd = open("xd.txt", "w")
    xd.write(ilist[i])
    xd.close()
    os.system('./the1.exe <xd.txt>> output.txt')
    o = open("output.txt", "a")
    o.write(" |\n")
    o.close()

file1 = open('case1.txt', 'r')
file2 = open('output.txt', 'r')
a1 = file1.read()
a2 = file2.read()
case1 = a1.split(" |\n")
outs = a2.split(" |\n")

for i in range(len(outs)-1):
    if outs[i] == case1[i]:
        print("Test "+str(i+1)+" Passed!")
        count += 1

    else:
        print("Test "+str(i+1)+" Failed!")
        fa = open("difference.txt", "a")
        fa.write("Expected Output:\n")
        fa.write(case1[i])
        fa.write("Given Output:\n")
        fa.write(outs[i])
        fa.write("\n")
        fa.close()
        

e = time.time()
print("Time: "+str(e-s)+" s")
print("Grade: "+str(count)+"/"+str(len(outs)-1)+"\n")
print("Check difference.txt for differences between expected output and your output. (If there are any.)")











