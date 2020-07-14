import sys

burger_menu=[]
beverage_menu=[]

for i in range(3):
    burger_price=int(sys.stdin.readline())
    burger_menu.append(burger_price)
min_burger=min(burger_menu)

for j in range(2):
    beverage_price=int(sys.stdin.readline())
    beverage_menu.append(beverage_price)
min_beverage=min(beverage_menu)

set_price=min_burger+min_beverage-50
print(set_price)