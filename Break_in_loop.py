Monthly_sales = [42,38,33,38,40,45]
month_list = ["jan","fed","mar","apr","may","jun"]
thresold = 35
for sales_amount , month in zip(Monthly_sales,month_list):
    if sales_amount< thresold:
        print(f"sales amount {sales_amount} is less than thresold in this {month}")

    else:
        print(f"sales amount {sales_amount} is greater than thresold in this {month}")