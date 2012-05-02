import os

class FileReader(object):

    def __init__(self):
        self.topdir="/mnt/f002/jr/journals/new"

    def find_text(self,topdir):
        file_list = []
        for root, dirs, files in os.walk(topdir):
            for f in files:
                if f[-3:] == 'pdf':
                    fulp = os.path.join(root,f)
                    file_list.append(fulp)
        return file_list