x = ["Manish", "Abhijeet", "rakesh", "vinayak", "shankar"]

# Map #########################################
resMap = list(map(str.capitalize, x))
print("\nresMap: ", resMap, end="\n\n")


# Filter ######################################
def HasR(word):
    if 'r' in str.lower(word):
        return True
    else:
        return False
    
resFil = list(filter(HasR, x))
print("\nresFil: ", resFil, end="\n\n")


# Reduce #####################################
from functools import reduce

def Add(a, b):
    return a+b

resRed = reduce(Add, x)
print("\nresRed: ", resRed, end="\n\n")

