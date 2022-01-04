# Two dimensional array
products = []
while True:
	name = input('Please input products name:')
	if name == 'q': # input 'q' for quit 
		break
	price = input('Please input product price:')
	p = []
	p.append(name)
	p.append(price) # equal to p = [name, price]
	products.append(p) # equal to products.append([name, price])
print(products)

print(products[0][0])