cars = {"BMW" : {"Model" : "220i", "Year": "2016"}, "Mercedes":{"Model" : "G-Wagon", "Year" : "2018"}}
print(cars)
print("*" * 10)
# car_year = cars["Mercedes"]["Year"]
# print(f"The model is of the year {car_year}")
# print(cars["BMW"].keys())
#print(cars.values())
car_copy = cars.copy()
print(car_copy)
print("*" * 20)
car_copy.clear()
print(car_copy)