import os
for i in range(10):
    os.rename("file ({}).txt".format(i+1), "file_{}.txt".format(i+1))