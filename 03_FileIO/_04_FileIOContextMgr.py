import sys

def fileTextWrite(fileName):
    f = open(fileName, mode="wt", encoding='utf-8')
    f.writelines(
        ["{0}\n".format(x) for x in range(100)])
    f.close()

def fileTextRead(fileName):
    with open(fileName, mode='rt', encoding='utf-8') as f:
        sqSeq = [int(line.strip()) ** 2 for line in f]
    print(sqSeq)

if __name__ == '__main__':
    fileName = "SeqData.txt"
    #fileTextWrite(fileName)
    fileTextRead(fileName)
    