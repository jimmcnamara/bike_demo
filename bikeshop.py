
def main():
	Shop1=Shop()
	Shop1.set_inv()
	Shop1.sale("jim",bike_list[1])
	Shop1.get_profit()
	Shop1.set_cust()
	Shop1.print_cust()

class Bike(object):
	def __init__(self,name,cost,weight):
		self.name=name
		self.cost=cost
		self.weight=weight

	def getprice(self):
		return (self.cost*1.2)

class Shop(object):
	def __init__(self):
		#initialize bike shop object with empty attributes
		self.bike_list = []
		self.inv={}
		self.profit=0

	def get_profit(self):
		#initialize variable total_profit
		total_profit=0
		for i in self.bike_list:
			price=i.getprice()
			num_sold=10-self.get_inv(i.name)
			subtotal_prof=((price-i.cost)*num_sold)
			total_profit=total_profit+subtotal_prof
		self.profit=total_profit
		print (total_profit)


	def set_inv(self):
		#create bike models
		new_bikes=self.make_bikes()
		#sets all models to base value of 10
		self.inv = {x:10 for x in new_bikes}
		print (self.inv)

	def set_cust(self):
		cust1=Customer("jim",200)
		cust2=Customer("john", 500)
		cust3=Customer("jacob",1000)
		cust_list=[]
		self.customers=[cust1,cust2,cust3]


	def print_cust(self):
		for x in self.customers:
			print(x.name," ",x.fund)


	def make_bikes(self):
	#creates bike objects, sets bikes' prices in a dictionary
		bike1=Bike("model1",75,12)
		bike2=Bike("model2",100,10)
		bike3=Bike("model3",125,8)
		bike4=Bike("model4",150,6)
		bike5=Bike("model5",175,4)
		bike6=Bike("model6",200,2)
		self.bike_list=[bike1,bike2,bike3,bike4,bike5,bike6]
		return (self.bike_list)

	def get_inv(self,model):
		#returns inventory for specific model
		return(self.inv[model])

	def funds_check(self,cust, model):
		for x in self.bike_list:
			if cust.fund>x.getprice():
				return True
			else:
				return False
	def sale(self,cust,model):
		check=True
		if check==True:
			self.inv[model]=self.inv[model]-1
			print("remaining bikes left: ",self.inv[model])
			cust.make_purchase(model.getprice())
			print(cust.name,"'s remaining funds are: ", cust.fund)
		else:
			print("not enough funds")

class Customer(object):
	def __init__(self,name,fund):
		self.name=name
		self.fund=fund
		self.owner=False

	def get_name(self):
		return (self.name)
	def get_funds(self):
		return (self.funds)

	def make_purchase(self,price):
		self.fund=self.fund-price
		#makes owner True because they just bought a bike
		self.owner=True




