from bitarray import bitarray

class FindDuplicates:

	def __init__(self, size, mlist, arr, dictionary):

		#setting the lenght of the bitarray
		self.size = size
		#setting a list of simple prime numbers that will be used as seeds for the hash function
		self.list = mlist
		#initializing the bitarray
		self.bit_array = bitarray(self.size)
		#initializing all bits to 0
		self.bit_array.setall(0)
		#the array with all the passwords
		self.passwords = arr
		#dictionary, assigning to each different character present in our 
		self.wdict = dictionary
		

	def hash_it(self, item, seed):
		base = 1099511628211 * seed
		for char in item:
			n = self.wdict.get(char)
			base *= n
		return base

	def check(self, item):
		for i in range(0, len(self.list)):
			position = self.hash_it(item, self.list[i]) % self.size
			if self.bit_array[position] == False:
				return False
		return True

	def add(self, item):
		pos = []
		for i in range(0, len(self.list)):
			d = self.hash_it(item, self.list[i]) % self.size
			pos.append(d)
			self.bit_array[d] = True