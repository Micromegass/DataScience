##List comprehension
# 1- Tenemos la siguiente lista de temperaturas celsius: celsius = [0, 10, 15, 32, -5, 27, 3]
# 2- Usando un list comprenhension, cree una nueva lista llamada fahrenheit que convierta cada elemento de la lista celsius a fahrenheit.
# 3- La fórmula para hacer la conversión es la siguiente: temperture_in_fahrenheit = temperture_in_celsius * 9/5 + 32

celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [elem * 9/5 + 32 for elem in celsius]
print(fahrenheit)



hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]


total_price = 0

for price in prices:
    total_price += price


average_price = total_price / len(prices)

print(f"Average Haircut Price: {average_price}")

new_prices = [price - 5 for price in prices]

print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]


print(f"Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue / 7











