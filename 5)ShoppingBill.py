n = int(input())

items = []
discounts = []

for _ in range(n):
    data = input().split(",")
    name = data[0]
    price = float(data[1])
    discount_percent = float(data[2])

    discount_amount = (price * discount_percent) / 100
    items.append(name)
    discounts.append(discount_amount)

# Find minimum discount
min_discount = min(discounts)

# Print all items having minimum discount
for i in range(n):
    if discounts[i] == min_discount:
        print(items[i])



# Input Example
'''
4
mobile,10000,20
shoe,5000,10
watch,6000,15
laptop,35000,5

'''