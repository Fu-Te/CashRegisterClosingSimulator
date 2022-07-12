N = int(input())

price = []

for i in range (N):
    s = input()
    price.append(s)

print(price)

max_price = int(max(price))
max_index = int(price.index(max_price))


print(max_index)
print(price)

del price[max_index]

discount_price = max_price/2


print((discount_price)+(sum(price)))


