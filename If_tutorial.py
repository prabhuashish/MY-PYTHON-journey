indian = ["jarrgy","cotton seends", "chia seeds"]
chinese = ["noddles","fired rice","spring roll"]
italian = ["pizza","pasta","chesses"]

dish = input("enter for dish to find the menu \n ")
print(f"{dish}--name of the dish")
if dish in indian:
    print(f"{dish}-- =is in indian")
elif dish in chinese:
    print(f"{dish}-- is in chinese")
elif dish in italian:
    print(f"{dish}-- is in italian")
else:
    print("find it in world menu")