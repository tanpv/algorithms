# Defenition

# LinkedList is a data structure consisting of a group of nodes which together represent a sequence. 
# Under the simplest form, each node is composed of data and a reference (in other words, a link) 
# to the next node in the sequence. This structure allows for efficient insertion or removal of elements 
# from any position

# Compare linked list with array

# Advancetage
# The principal benefit of a linked list over a conventional array is that the list elements can easily 
# be inserted or removed without reallocation or reorganization of the entire structure because the data
# items need not be stored contiguously in memory --> it is good for program which use a lot of insert
# or remove data from sequent

# Disadvancetage
# On the other hand, simple linked lists by themselves do not allow random access to the data, or any form 
# of efficient indexing. So this kind of data structure not good for program which require alot of access
# to data


# implement linked_list by python

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():
	
	def __init__(self):
		self.head = None

	# add node to head of the list
	def add_node_at_head(self, data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head = new_node

	# add node at pos
	def add_node_at_pos(self, pos):
		pass

	# add node at tail or ending
	def add_node_at_end():
		pass


	def print_list(self):
		# need to travel all element inside list
		node = self.head
		while node != None:
			print node.data
			node = node.next #help to travel in the list


	
	def search(self, data):
		# return pointer to node
		node = self.head

		while node != None:
			if node.data == data:
				# get the result
				return node
			else:
				node = node.next

		if node == None:
			return None
	
	def remove_head_node(self):
		if self.head != None:
			self.head = self.head.next


	def remove_at_pos(self, pos):
		pass
			


# init a list
list1 = LinkedList()

# add value to list
for value in range(10):
	list1.add_node_at_head(value)

# print list value
list1.print_list()

# search a node
print list1.search(5).data

# delete a node
