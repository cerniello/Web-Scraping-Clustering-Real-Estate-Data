from bitarray import bitarray

class FindDuplicates:

	def __init__(self, size, mlist, arr, dictionary):

		#setting the lenght of the bitarray, the bigger it is, the less false positive will be detected
		self.size = size
		#setting a list of simple prime numbers that will be used as seeds for the hash function
		self.list = mlist
		#initializing the bitarray
		self.bit_array = bitarray(self.size)
		#initializing all bits to 0 (empty)
		self.bit_array.setall(0)
		#the array with all the passwords
		self.passwords = arr
		#dictionary, assigning to each different character present in our password set a unique prime number
		self.wdict = dictionary
		

	''' hash function that takes in input a string and a seed (int) that will assure the uniqueness
		to the hash function. Incrementing the base which is a big prime number, we moltiply it each time 
		for the value of the relative character in our dictionary '''
	def hash_it(self, item, seed):
		base = 1099511628211 * seed
		for char in item:
			n = self.wdict.get(char)
			base *= n
		return base


	'''
	This second hash function is used for tackling the second part of the task. Instead of usic arithmetical operations, concatenating
	the character values as strings assures that the position of each character is registered.
	'''
	def hash_it2(self, item, seed):
		base = str(1099511628211) + str(seed)
		for char in item:
			n = self.wdict.get(char)
			base = base + str(n)
		return int(base)

	'''
	The check() function will compute the hash_it() function over the password exactly 3 times with 
	different seeds. This function is also responsible of computing the modulo operation returning a value 
	between 0 and the size of our bitarray. This value rapresents the index of the bitarray in which we'll check 
	if the password is present or not. If the value of the bittarry is already set to 1 (False), it means that the word
	has been already processed in a passed iteration and registered in the bitarry. Oterwise it means that no such word has been
	found yet.'''

	def check(self, item):
		for i in range(0, len(self.list)):
			position = self.hash_it(item, self.list[i]) % self.size
			if self.bit_array[position] == False:
				return False
		return True

	'''
	This second check() function does exactly the same as above but using the second hash function, this function is used to check whether
	a password has already been processed considering also the order of the characters in the password. i.e.: 'ABBA' != 'BAAB'
	'''
	def check2(self, item):
		for i in range(0, len(self.list)):
			position = self.hash_it2(item, self.list[i]) % self.size
			if self.bit_array[position] == False:
				return False
		return True

	'''
	This function will be used only in the case that the check() function has returned True. This means that we want to register in
	the bitarray the word that has been found and that we are sure doesn't have duplicates. Similarly to what happens in the check()
	function, we need to compute the hash value and the modulo operation to obtain the index in which we'll store the word.'''
	def add(self, item):
		pos = []
		for i in range(0, len(self.list)):
			d = self.hash_it2(item, self.list[i]) % self.size
			pos.append(d)
			self.bit_array[d] = True


	'''
	Second add() function to be used for the second part of the task. It involves the usage of the second hash function hash_it2()
	'''
	def add2(self, item):
		pos = []
		for i in range(0, len(self.list)):
			d = self.hash_it2(item, self.list[i]) % self.size
			pos.append(d)
			self.bit_array[d] = True