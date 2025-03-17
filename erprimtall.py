from math import sqrt, floor

def ErPrimtall(n):
    if n==1:
        return False
    elif n>1:
        for i in range (2, floor(sqrt(n)+1)):
            if (n%i)==0:
                return False
    return True
if __name__== "__main__":
    print(ErPrimtall(17))