prices = [238.11, 237.81, 238.91]
prices.sort()
print(prices)
fam = ["liz", 1.73, "emma", 1.68, "mom", 1.71, "dad", 1.89]
print(type(fam))

months = ['January', 'February', 'March']
months.append('April',)
print(months)

x = [1, 2, 3]
x.extend([4, 5])
print(x)

stream=["Lisalab","LoveLace","AnitaB"]
print(stream.index("AnitaB"))

prices = [1000, 20198, 1209]
price_max = max(prices)
print(price_max)

Food_price_1 = [100,200,1300]
Food_price_2 = [1000, 30, 2500,500,490,780]

print('Food_price_1 length is ', len(Food_price_1))
print('Food_price_2 length is ', len(Food_price_2))

stock_price_1 = [50.23]
stock_price_2 = [75.14, 85.64, 11.28]

print('stock_price_1 length is ', len(stock_price_1))
print('stock_price_2 length is ', len(stock_price_2))

Estates = ('Komarock', 'Upperhill', 'Kilimani')
print(list(Estates))

car_price_1 = [200000]
car_price_2 = [12000000]

print(car_price_1==car_price_2)
print(car_price_1==car_price_1)
print(car_price_2==car_price_1)