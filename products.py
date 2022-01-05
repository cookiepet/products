# Two dimensional array
products = []
while True:
	name = input('Please input products name:')
	if name == 'q': # input 'q' for quit 
		break
	price = input('Please input product price:')
	price = int(price) # Transfer price type from string to integer
	p = []
	p.append(name)
	p.append(price) # equal to p = [name, price]
	products.append(p) # equal to products.append([name, price])
print(products)

for p in products:
	print('Product:', p[0],'price is', p[1] )

# String operation
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding='utf-8') as f: # Just open file. # utf-8 is general coding type.
	f.write('Producsts name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n change line

# 'with' will automatically close the file once the program run out of with.