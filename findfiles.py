import os

for root, dirs, files in os.walk('/mnt/f002/jr'):
    print " root= ", root, "\n diry= ",
    for d in dirs:
        print d,
    print "\n files= ",
    for f in files:
        print f
    print "\n"