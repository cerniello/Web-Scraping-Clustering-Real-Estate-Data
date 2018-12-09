import random

def loadPw():
	#loading the password set from the txt file
	filename = 'passwords2.txt'
	passwords = []

	with open(filename) as file:
	    for line in file:
	        passwords.append(line.strip())

	return passwords

def ciao():
	print('ciaCi')
	return
#defining a function that check if a number is prime or not
def check_prime(p):
    for i in range(2, p):
        if p % i == 0:
            return False
    return True

'''
defining a function to get the closest prime number of a given integer
basically check if the numper given in input is prime or not. If it is not,
it checks the primality of the previous and the next number. It continues until 
a prime number is found
'''
def find_next_prime(n):
    if check_prime(n):
        return n
    _previous = n - 1
    _next = n + 1
    while True:
        if check_prime(_previous):
            return _previous
        elif check_prime(_next):
            return _next
        else:
            _previous -= 1
            _next += 1

'''
Extracting each different character that occurs in the passwords set.
'''
def extractChar(pw):
	l = []
	for word in pw[:1000]:
		for char in word:
			if char not in l:
				l.append(char)
	return l

''' function that will create a dictionary setting each character found
	previously to a prime number
'''
def createDict(_list):
	'''
	First of all reating a list of all prime numbers between 0 and 10'000
	'''
	minPrime = 0
	maxPrime = 10000
	cached_primes = [i for i in range(minPrime,maxPrime) if check_prime(i)]
	'''
	Creating a dictionary with all the characters present in the passwords file as keys and a prime number as value.
	While inserting in the dictionary new values, if the value is already present in the dictionary, we will multiply it 
	with a random prime number taken from the list of prime numbers created before.
	The prime number is obtained starting from the unicode value of the character and then
	finding the closest prime number to that value that is not already added to the dictionary.
	'''
	wdict = {}
	for elem in range(0, len(_list)):
		v = find_next_prime(ord(_list[elem]))
		if v not in wdict.values():
			wdict[_list[elem]] = v
			n = random.choice([i for i in cached_primes])
			v = v * n
			wdict[_list[elem]] = v
	return wdict

def checkDuplicateKeys(dic):
	'''
	Checking if there are duplicate values in the dictionary. Due to the fact that in some cases we use random
	prime numbers, ther is a low probability that a prime number has been picked twice. If this function returns an empty
	list it means that no duplicate values are stored in our dictionary.
	'''
	rev_multidict = {}
	for key, value in dic.items():
	    rev_multidict.setdefault(value, set()).add(key)

	return [key for key, values in rev_multidict.items() if len(values) > 1]
