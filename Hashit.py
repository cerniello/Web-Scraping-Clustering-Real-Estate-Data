def check_prime(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def find_next_prime(n):
    if check_prime(n):
        return n
    low = n - 1
    high = n + 1
    while True:
        if check_prime(low):
            return low
        elif check_prime(high):
            return high
        else:
            low -= 1
            high += 1


def load_passwords(file):
    array=[]
    with open(file) as passwords:
        for line in passwords:
            array.append(line.strip())


def create_prime_dict():
    array = load_passwords('passwords2.txt')
    wdict = {}
    c = 0
    for word in array:
        for char in word:
            if char not in wdict:
                while c < 2000:
                    wdict[char] = find_next_prime(ord(char))
                    c += 1
                    print(str(c) + "char found")


def hash_it(item,seed):
    #prime = 123456791
    base = seed
    for char in item:
        n = wdict.get(char)
        base *= n
    return base