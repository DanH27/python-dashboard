import matplotlib.pyplot as plt
import json

sales = None
staff = None
sales_per_person = {}
total_profit = 0

with open('sales_staff.json', 'r') as staffFile:
    staff = json.loads(staffFile.read())
    #print(obj)

#id, salesperson, make, model, year, carvin, base_price, accessories, taxes, date
with open('sales.json', 'r') as salesFile:
    sales = json.loads(salesFile.read())
    #print(obj)
    #print()

#print(sales)
#print(staff)
#Number of sales
salesman_labels = []
cars_per_salesman = []
for i in range(len(staff)):
    sales_per_person[staff[i]['first_name']] = 0
    salesman_labels.append(staff[i]["first_name"])
    #cars_per_salesman.append(staff[i])
    #if staff[i]['id'] === sales[]
    #print(staff[i]['first_name'])

#print(salesman_labels)
for i in range(len(staff)):
    for k in range(len(sales)):
        if sales[k]['salesperson'] == staff[i]['id']:
            sales_per_person[staff[i]['first_name']] += 1

print(sales_per_person)

plt.bar(range(len(sales_per_person)), list(sales_per_person.values()))
plt.xticks(range(len(sales_per_person)), list(sales_per_person.keys()))
plt.ylabel("Number of Cars")
plt.xlabel("Salesman")
plt.show()


#Total profit
for i in range(len(sales)):
    base_price = float(sales[i]['base_price'].replace("$", ""))
    accessories = float(sales[i]['accessories'].replace("$", ""))
    taxes = float(sales[i]['taxes'].replace("$", ""))
    total_profit += (base_price + accessories) - taxes

print(str(total_profit) + "Total Profit")

#Cars sold by Car Manufacturer
#Number of sales
car_per_manufacturer = {}
for i in range(len(sales)):
    car_per_manufacturer[sales[i]['make']] = 0

for i in range(len(sales)):
    car_per_manufacturer[sales[i]['make']] += 1

print(car_per_manufacturer)
plt.bar(range(len(car_per_manufacturer)), list(car_per_manufacturer.values()))
plt.xticks(range(len(car_per_manufacturer)), list(car_per_manufacturer.keys()), rotation="vertical")
plt.title("Cars Sold By Make")
plt.ylabel("Amount Sold")
plt.xlabel("Car Make")
plt.show()
#Top 10 makes and models
makes_and_models = {}


for i in range(len(sales)):
    car_name = ""
    car_name = sales[i]['make'] + "_" + sales[i]['model']
    if car_name in makes_and_models:
        makes_and_models[car_name] += 1
    else:
        makes_and_models[car_name] = 1

top_values = list(makes_and_models.values())
top_values.sort(reverse=True)
top_values = top_values[:10]
top_companies = list(makes_and_models.keys())
top_companies.sort(reverse=True)
top_companies = top_companies[:10]

plt.bar(top_companies, top_values)
plt.xticks(top_companies, rotation="vertical")
plt.title("Top 10 Models Sold")
plt.ylabel("Amount Sold")
plt.xlabel("Car Model")
plt.show()


sales_information_person = {}
#Sales person table
for i in range(len(staff)):
    for k in range(len(sales)):
        if sales[i]['salesperson'] == staff[i]['id']:
            if sales[i]['salesperson'] not in sales_information_person:
                sales_information_person[staff[i]['first_name']] = 1
                sales_information_person[staff[i]['salesperson']] = 1
            else:
                sales_information_person[staff[i]['first_name']] += 1
