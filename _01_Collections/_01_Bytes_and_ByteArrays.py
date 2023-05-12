def Test1():
    # Program for converting bytes to string using decode()
    data = b'TestString'
    print(data)
    print(type(data))
    # converting
    output = data.decode()
    # display output
    print(output)
    print(type(output))

def Test2():
    # Program for converting bytes to string using str()
    data = b'TestString'
    print(data)
    print(type(data))
    # converting
    output = str(data, 'UTF-8')
    # display output
    print(output)
    print(type(output))


def Test3():
    # Program for converting bytes to string using codecs
    # import required module
    import codecs
    data = b'TestString'
    # display input
    print(data)
    print(type(data))
    # converting
    output = codecs.decode(data)
    # display output
    print(output)
    print(type(output))

def Test4():
    # Program for converting bytes to string using maps
    ascII = [103, 104, 105]
    string = ''.join(map(chr, ascII))
    print(string)

def Test5():
    # Program for converting bytes to string using pandas
    import pandas as pd
    dic = {'column' : [ b'Book', b'Pen', b'Laptop', b'CPU']}
    data = pd.DataFrame(data=dic)
    x = data['column'].str.decode("utf-8")
    print(x)

def Test6():
    str1 = "Python"
    print(type(str1), str1)

    # Encode the string to byteArray
    dataBytes = str1.encode(encoding = 'utf-8') 

    print(type(dataBytes))
    print(dataBytes)

    # Decode to String (str2)
    str2 = dataBytes.decode()

    # Print the type and value of the string
    print(type(str2), str2)

    # Compare the two strings for equivalence

Test3()