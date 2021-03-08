products = []
while True:
	product = input('請輸入商品名稱')
	if product == 'q':
		break
	price = input('請輸入價格')
	products.append([product,price])

print(products)

with open('商品價格及名稱目錄.csv', 'w') as f:
	for d in products:
		f.write(d[0]+','+d[1]+'\n')
