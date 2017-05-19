def main():
	from bikeshop import Shop
	from bikeshop import Bike
	from bikeshop import Customer
	Shop1=Shop()
	Shop1.set_inv()
	Shop1.set_cust()
	Shop1.print_cust()
	Shop1.get_inv()
	Shop1.sale('jim','model1')
	Shop1.sale('john','model3')
	Shop1.sale('jacob','model4')
	Shop1.print_inv()
	Shop1.get_profit()

