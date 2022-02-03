f = open("threelinefile.txt", "w")
f.write("""Line 1
Line 2
Line 3""")
f.close()

f = open("threelinefile.txt", "r")
print(f.readline())

os.remove("threelinefile.txt")