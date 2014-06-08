__author__ = 'Administrator'
import os
def BFS_Dir(path, dirCallback = None, fileCallback = None):
    queue = []
    ret = []
    queue.append(path);
    while len(queue) > 0:
        tmp = queue.pop(0)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                queue.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            if fileCallback:
                fileCallback(tmp)
    return ret


def DFS_Dir(path, dirCallback = None, fileCallback = None):
    stack = []
    ret = []
    stack.append(path);
    while len(stack) > 0:
        tmp = stack.pop(len(stack) - 1)
        if(os.path.isdir(tmp)):
            ret.append(tmp)
            for item in os.listdir(tmp):
                stack.append(os.path.join(tmp, item))
            if dirCallback:
                dirCallback(tmp)
        elif(os.path.isfile(tmp)):
            ret.append(tmp)
            if fileCallback:
                fileCallback(tmp)
    return ret

def printDir(path):
    print "dir: " + path

def printFile(path):
    print "file: " + path

b = BFS_Dir(u'C:\Templenovo', printDir, printFile)
print "-----------------------------------------------"
d = DFS_Dir(u'C:\Templenovo', printDir, printFile)
