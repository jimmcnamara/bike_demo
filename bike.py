class Bike(object):
	def __init__(self,name,cost,weight):
		self.name=name
		self.cost=cost
		self.weight=weight

	def getprice(self):
		return (self.cost*1.15)
		

