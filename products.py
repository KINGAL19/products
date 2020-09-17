# while loop 通常使用在我們不知道會執行幾次的形況下
products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

