def fileBinWriteList():
    lst = [1.7, 2.4, 3.9]
    f = open("BinaryFile.bin", mode = 'wb')
    for x in lst:
        s = str(x)+'\n'
        bt = s.encode()
        f.write(bt)
    f.close()

def fileBinReadList():
    lst = []
    f = open("BinaryFile.bin", 'rb')
    for line in f:
        x = float(line)
        lst.append(x)
        print("lst ->", lst)
    f.close()

def fileBinWriteTuple():
    tup = ('abc', 'def', 'ghi', 'jk lm')
    f = open("BinaryFileTuple.bin", mode = 'wb')
    for x in tup:
        bt = (x + '\n').encode()
        f.write(bt)
    f.close()

def fileBinReadTuple():
    tup = ()
    f = open("BinaryFileTuple.bin", 'rb')
    for line in f:
        s = line.decode()
        #print("Before [{0}]".format(s), end="\t")
        s = s[:-1]
        #print("After [{0}]".format(s))
        tup = tup + (s,)
        print("tup ->", tup)
    f.close()

import struct
def fileBinWriteList2():
    lst = [1.7, 2.4, 3.9]
    print("Packing list -->", lst)
    st = struct.pack('f'*len(lst), *lst)
    f = open("BinaryFilePacked.bin", mode = 'wb')
    f.write(st)
    f.close()

def fileBinReadList2():
    upLst = []
    f = open("BinaryFilePacked.bin", 'rb')
    data = f.read()
    upLst = struct.unpack('f'*3, data)
    f.close()
    print("Unpacked list ->", upLst)

# fileBinWriteList()
# fileBinReadList()

# fileBinWriteTuple()
# fileBinReadTuple()

fileBinWriteList2()
fileBinReadList2()