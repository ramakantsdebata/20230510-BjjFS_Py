import sys

def fileTextWrite(fileName):
    f = open(fileName, mode="wt", encoding='utf-8')
    f.writelines(
        ['What are the roots that clutch, ',
         'what branches grow\n',
         'Out of this stony rubbish? ',
         'Son of man \n', 
         'You cannot say, or guess, ',
         'for you know only,\n',
         'A heap of broken images, ',
         'where the sun beats\n'])
    f.close()

def main(fileName):
    f = None
    try:
        f = open(fileName, mode='rt', encoding='utf-8')
        for line in f:
            #print(line)
            #print(line, end="")
            #print(line.strip())
            sys.stdout.write(line)
        # f.close()
    except BaseException as e:
        print("Exception Occured [" + str(type(e)) + str(e) + "]")
        # f.close()
    finally:
        if f != None:
            f.close()

if __name__ == '__main__':
    # fileTextWrite(sys.argv[1])
    # main(sys.argv[1])
    # fileTextWrite("SomeFile.txt")
    main("SomeFile.txt")