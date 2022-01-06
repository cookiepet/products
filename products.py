# Read previous records
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if 'Products name,price' in line:
			continue # skip below process then continue in next loop. (Equal to break one times.)
		name, price = line.strip().split(',') # Strip will remove change line mark (\n).
		products.append([name, price])
print(products)

# User input area
# Two dimensional array
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

# Print out all records.
for p in products:
	print('Product:', p[0],'price is', p[1] )

# String operation
# 'abc' + '123' = 'abc123'
# 'abc' * 3 = 'abcabcabc'

with open('products.csv', 'w', encoding = 'utf-8') as f: # Just open file. # utf-8 is general coding type.
	f.write('Products name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #\n change line

# 'with' will automatically close the file once the program run out of with.