# Open(file, mode, textEncoding)
import sys
print(sys.getdefaultencoding())

# https://docs.python.org/3/library/codecs.html
# Standard Encodings

# https://docs.python.org/3/library/functions.html#open
# File Open modes
############################
def fileTextWrite():
    f = open('wasteland.txt', mode='wt', encoding = 'utf-8')
    charsWritten = f.write('What are the roots that clutch, ')
    print("Characters/CodePoints written:", charsWritten)
    # f.write() returns the chars/codepoints written to file, NOT bytes
    # Python doesn't have a writeline. So newlines need to be explicitly given

    f.write('what branches grow\n')
    f.write('Out of this stony rubbish? ')
    f.close()
    # Creates a file of 79 bytes on Windows and 78 bytes on Linux
    # This is because Python's universal newline behaviour is translated
    # to the platform's native newline, "\r\n" for windows, and "\n" for Linux
    # This means the value returned by f.write() is the codepoints 
    # written by the program, not accounting for the native endpoint translation.

def fileTextRead():
    f = open('wasteland.txt', mode = 'rt', encoding = 'utf-8')
    s1 = f.read(32) # 32 characters, NOT bytes
    print(s1)
    s1 = f.read()   # Read to end of the file
    print(s1) 

    s1 = f.read()   # Will return an empty string as file has been read to the end
    if s1 == str(''):
        print("File has been already read to the end.")
    else:
        print(s1)
    
    pos = f.seek(0) 
    print("\n Read with f.readline()")
    s1 = f.readline()
    print(s1)
    s1 = f.readline()
    print(s1) 
    s1 = f.readline()
    if s1 == str(''):
        print("File has been already read to the end.")
    else:
        print(s1)

    # Rewind
    pos = f.seek(0)
    s1 = f.readlines()  # When we are sure that we have enough memory
                        # to read all lines from file into memory.
    print("\nRead with f.readlines()\n", s1, sep="")
    f.close()

def fileTextAppend():
    fileTextWrite()
    f = open("wasteland.txt", mode="at", encoding='utf-8')
    # Python has no 'writeline()' function but,
    # it has a 'writelines()' function that accepts an iterable
    # list of lines to write to the file.
    # It doesn't ad newlines. HAve to explicitly provide in the strings
    f.writelines(
        ['Son of man \n', 
         'You cannot say, or guess, ',
         'for you know only,\n',
         'A heap of broken images, ',
         'where the sun beats\n'])
    f.close()

def fileTextReadAll():
    f = open("wasteland.txt", mode="rt", encoding='utf-8')
    # Starting with ver 3.8, ":=" allows var assignment withing expressions
    while (s1 := f.readline()) != str():
        print(s1)
    f.close()

print("\n\n\tfileTextWrite() -->\n")
fileTextWrite()
print("\n\n\tfileTextRead() -->\n")
fileTextRead()
 
print("\n\n\tfileTextAppend() -->\n")
fileTextAppend() 
print("\n\n\tfileTextReadAll() -->\n")
fileTextReadAll()