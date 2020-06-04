# 1- Tenemos la siguiente lista: sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
# 2- Defina una variable llamada: scoops_sold
# 3- Itere sobre la lista sales_data, llame a cada lista interna location e imprima cada location
# 4- Dentro del ciclo sales_data itere sobre cada location y añada el elemento a la variable scoops_sold
# 5- Imprima la variable scoop_sold

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = []

for location in sales_data:
    print(location)

for location in sales_data:
    for elem in location:
        scoops_sold.append(elem)


print(scoops_sold)

