#Part I
# Cree una lista de consumidores llamada: first_names
# Ingrese los siguientes valores a la lista: Ainsley, Ben, Chani y Depak.
# Cree una lista vacia llamada age.
# Use append para añadir la edad 42 a la lista creada
# Cree una nueva lista llamada all_ages que combina la lista age con la siguiente lista: 32, 41, 29.
# Cree una nueva variable llamada: name_and_age que combina las dos listas anteriores
# Cree un rango llamado ids que va de 0 a 3.

first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
all_ages = age + [32, 41, 29]
name_and_age = all_ages + first_names
ids = list(range(4))


#Part II
# Cree una lista llamada subjects y llenela con las clases que usted esta tomando: "physics", "calculus", "poetry", "history"
# Cree una lista llamada grades y llenela con los siguientes puntajes: 98, 97, 85, 88
# Use la funcion zip para combinar ambas listas. Guarde ese objeto como una list dentro de una variable llamada: gradebook
# Imprima gradebook. es el resultado que esperabamos?
# Su clase de Computer Science ya tiene score, y sacaste un perfecto 100
# Despues de las definiciones de subjects y grades, pero antes de que creara la variable gradebook, use append para añadir "computer science" a subjects y 100 a grades
# Estas son sus calificaciones del semestre anterior: last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
# Cree una nueva variable llamada full_gradebook con los items de ambos semestres: gradebook y last_semester_gradebook

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
subjects.append("computer science")
grades.append(100)
gradebook = zip(subjects, grades)
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
full_gradebook = list(gradebook) + last_semester_gradebook
print(full_gradebook)


#Part III
# Usted trabaja en una pizzeria, y para mantener en control que tipo de pizzas usted vende, crea una lista llamada toppings que contenga lo siguiente: pepperoni, pineapple, cheese, sausage, olives, anchovies, mushrooms
# Para mantener un control sobre cuanto cuesta cada trozo de pizza cree una lista llamada prices que contenga: 2, 6, 1, 3, 2, 7, 2.
# Encuentre el largo de la lista toppings y guardelo en una variable llamada: num_pizzas
# Imprima el string "We sell X different kinds of pizza!" donde la X es num_pizzas
# Use zip para combinar las dos listas dentro de una lista llamada: pizzas que tiene la siguiente estructura: [(price_0, topping_0), (price_1, topping_1), (price_2, topping_2), ...]
# Recuerde que debe tener el resultado en una lista, asi: list(zip(____, ____))
# Imprima pizzas se ve como se espera que este?
# Organice la lista pizzas de forma que las pizzas con el menor precio estan al principio de la lista
# Guarde el primer elemento de pizzas en una variable llamada: cheapest_pizza
# Un tipo de traje y corbata llega a la pizzeria gritando: "Deme la pizza mas cara que tenga!". Obtenga el ultimo elemento de la lista pizzas y guardelo en una variable llamada: priciest_pizza
# Otro grupo de personas quiere las mas economicas, asi que de la lista pizzas guarde las 3 pizzas mas economicas en una variable llamada three_cheapest e imprima esta nueva lista three_cheapest
# Tu jefe quiere hacer una investigacion sobre las pizzas de $2. Cuente el numero de ocurrencias del numero 2 en la lista prices y guarde el resultado en una nueva variable llamada: num_two_dollar_slices e imprimala

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_pizzas = len(toppings)
print(num_pizzas)
print(f"We sell {num_pizzas} different kinds of pizza!")
pizzas = list(zip(toppings, prices))
print(pizzas)
pizzas_sorted = sorted(zip(prices, toppings))
print(pizzas_sorted)
cheapest_pizza = pizzas_sorted[0]
print(cheapest_pizza)
priciest_pizza = pizzas_sorted[-1]
print(priciest_pizza)
three_cheapest = pizzas_sorted[:3]
print(three_cheapest)
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Resultado Parte III
# 7
# We sell 7 different kinds of pizza!
# [('pepperoni', 2), ('pineapple', 6), ('cheese', 1), ('sausage', 3), ('olives', 2), ('anchovies', 7), ('mushrooms', 2)]
# [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives'), (2, 'pepperoni'), (3, 'sausage'), (6, 'pineapple'), (7, 'anchovies')]
# (1, 'cheese')
# (7, 'anchovies')
# [(1, 'cheese'), (2, 'mushrooms'), (2, 'olives')]
# 3