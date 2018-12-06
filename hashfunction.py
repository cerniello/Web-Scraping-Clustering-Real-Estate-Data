
def hashFunction(string, seed):
    # Il numero l'ho preso da un generatore online di numeri primi
    prime = 1099511628211
    offset_basis = 14695981039346656037

    vhash = offset_basis + seed
    for char in string:
        vhash = vhash^ord(char)
        vhash = vhash*prime
    return vhash
