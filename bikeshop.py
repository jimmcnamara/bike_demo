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
			num_sold=10-self.get_inv_model(i.name)
			subtotal_prof=((price-i.cost)*num_sold)
			total_profit=total_profit+subtotal_prof
		self.profit=total_profit
		print ("total profit is: ",total_profit)


	def set_inv(self):
		#create bike models
		new_bikes=self.make_bikes()
		#sets all models to base value of 10
		self.inv = {x.name:10 for x in new_bikes}
		
	def print_inv(self):
		print("the current inventory is: ")
		for i in self.inv:
			print(i, " ",self.inv[i])

	def set_cust(self):
		cust1=Customer("jim",200)
		cust2=Customer("john", 500)
		cust3=Customer("jacob",1000)
		cust_list=[cust1,cust2,cust3]
		self.customers=cust_list


	def print_cust(self):
		print("The customers are: ")
		for x in self.customers:
			print(x.name," ",x.fund)
		for x in self.customers:
			can_afford=[]
			for i in self.bike_list:
				if x.fund>i.getprice():
					can_afford.append(i.name) 
			print(x.name, "can afford: ", can_afford)


	def make_bikes(self):
	#creates bike objects, sets bikes' prices in a dictionary
		bike1=Bike("model1",75,12)
		bike2=Bike("model2",150,10)
		bike3=Bike("model3",250,8)
		bike4=Bike("model4",450,6)
		bike5=Bike("model5",900,4)
		bike6=Bike("model6",2000,2)
		self.bike_list=[bike1,bike2,bike3,bike4,bike5,bike6]
		return (self.bike_list)

	def get_inv(self):
		#returns inventory for all models
		return(self.inv)

	def get_inv_model(self,model):
		#returns inventory for specific models
		return(self.inv[model])

	def funds_check(self,cust, model):
		for x in self.bike_list:
			if cust.fund>x.getprice():
				return True
			else:
				return False

	def sale(self,cust,model):
		for bike in self.bike_list:
			if bike.name==model:
				local_bike=bike
		for i in self.customers:
			if i.name==cust:
				local_cust=i
		local_price=local_bike.getprice()
		check=False
		if local_cust.get_funds()>local_price:
			check=True
		if check == True:
			local_cust.make_purchase(local_price)
			self.inv[model]=self.inv[model]-1
			print(cust, "bought ",model," and has ",local_cust.fund," remaining" )
		else:
			print("not enough funds")
			
##	def sale(self,cust,model):
##		check=True
##		if check==True:
##			self.inv[model]=self.inv[model]-1
##			print("remaining bikes left: ",self.inv[model])
##			cust.make_purchase(model.getprice())
##			print(cust.name,"'s remaining funds are: ", cust.fund)
##		else:
##			print("not enough funds")

class Customer(object):
	def __init__(self,name,fund):
		self.name=name
		self.fund=fund
		self.owner=False

	def get_name(self):
		return (self.name)
	def get_funds(self):
		return (self.fund)

	def make_purchase(self,price):
		self.fund=self.fund-price
		#makes owner True because they just bought a bike
		self.owner=True




