# 1- Average
#
# Escriba una función llamada average()que recibe dos parametros llamados num1 y num2
# La Función debe retornar el valor promedio de esos dos numeros
# 2- Exponencial
#
# Escriba una funcion llamada tenth_power() que reciba un parametro llamado num
# La función debe retornar num a la 10ma potencia

# 3- Bond
#
# Escriba una funcion llamada introduction() que reciba dos parametros first_name y last_name
# La funcion debe retornar el last_name seguido por una coma, un espacio, first_name, otro espacio y finalmente last_name


# 4- Raiz cuadrada
#
# Escriba una funcion llamada square_root() que toma un parametro llamado num
# Use los exponentes (**)para retornar la raiz cuadrada de num
# 5- Propina
#
# Cree una funcion llamada tip() que reibe dos parametros llamados total y percentage
# Esta funcion deberia retornar el monto que usted deberia dar de propina dado un total y un porcentaje que usted quiera.
# 6- Porcentaje de ganancias
#
# Cree una funcion llamada win_percentage() que toma dos parametros llamados wins y losses
# La funcion debe retornar el porcentaje total de juegos ganados por un equipo dados esos dos datos.


# 7- Primeros tres multiples
#
# Escriba una funcion llamada first_three_multiples() que toma un parametro llamado num
# Esta funcion debe imprimir los primeros tres multiplos de num, luego deberia retornar el tercer multiplo.
# Por ejemplo, first_three_multiples(7) deberia retornar 7, 14 y 21 en tres lineas diferentes y retornar 21

# 8- Año Perruno
#
# Dicen que un año en un humano es equivalente a 7 años en la vida de los perros.
# Escriba una funcion llamada dog_years() que toma dos parametros name y age
# La funcion debe computar a age en años de perro y retornar el siguiente string: {name}, tu tienes {age} años en años de perro


def average(num1,num2):
    return (num1+num2) / 2

print(average(4,2))

def tenth_power(num):
    return num**10

print(tenth_power(5))

def introduction(first, last):
    return last + ', ' + first + ' ' + last

print(introduction("axel", "simon"))

def square_root(num):
    return num**1/2

print(square_root(4))

def tip(total, precentage):
    propina = (total * precentage)/100
    amount = total + propina
    return amount, precentage

print(tip(100, 10))

def win_percentage(wins, losses):
    total = wins + losses
    ganados = (total/100) * wins
    return ganados

print(win_percentage(10, 5))

def first_three_multiples(num):
    print(num)
    print(num*2)
    print(num * 3)
    return num*3

print(first_three_multiples(7))

def dog_years(name, age):
    dog_years = age * 7
    return f"{name}, tu tienes {dog_years} años en años de perro"

print(dog_years("Axel", 5))