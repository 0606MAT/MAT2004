from erprimtall import ErPrimtall
def nesteprimtall(n):
    q=n+1
    while not(ErPrimtall(q)):
        q=q+1
    return q
print(nesteprimtall(11))