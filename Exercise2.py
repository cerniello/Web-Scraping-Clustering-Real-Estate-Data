from bitarray import bitarray

class FindDuplicates:

	def __init__(self, size, mlist):

		#setting the lenght of the bitarray
		self.size = size
		#setting a list of simple prime numbers that will be used as seeds for the hash function
		self.list = mlist
		#initializing the bitarray
		self.bit_array = bitarray(self.size)
		#initializing all bits to 0
		self.bit_array.setall(0)
		#loading the password set
		self.filename = 'passwords2.txt'
		self.passwords = load(self.filename)
		#creating a dictionary, assigning to each different character present in our 
		self.wdict = create_prime_dict()

	def load(self, name):
		self.passwords = []
		with open(name) as file:
			for line in file:
				self.passwords.append(line.strip())

	def create_prime_dict(self):
		self.wdict = {}
		c = 0
		for word in self.passwords:
			for char in word:
				if char not in wdict:
					while c<2000:
						self.wdict[char] = find_next_prime(ord(char))
						c += 1


	def check_prime(self, p):
		for i in range(2, p):
			if p % i == 0:
				return False
		return True


	def find_next_prime(self, n):
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


	def hash_it(self, item, seed):
		base = seed
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
	