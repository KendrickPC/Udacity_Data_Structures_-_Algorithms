'''
Task 03: 
Add functions to set and get the value of the node.
Add functions get_value and set_value.
'''

class Node(object):
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def get_value(self):
		return self.value

	def set_value(self, value):
		self.value = value
	

