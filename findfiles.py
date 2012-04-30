import os

for root, dirs, files in os.walk('/mnt/f002/jr'):
    for f in files:
        if f[-3:] == 'txt':
            fulp = os.path.join(root,f)
            print fulp