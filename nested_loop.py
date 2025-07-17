products = ["iphone","ipad","Macbook"]
regions = ["USA","China","India"]
revenue = [20,23,45,17,12,12,9,5]
i = 0
for product in products:
    for region in regions:
        rev = revenue[i]
        i += 1
        print(f"{product} {region} revenue: {rev}")