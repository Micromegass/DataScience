# 1- Imprima su nombre usando el comando print().
#

print("Axel")


# 2- Si su impresion uso comillas dobles " cambieles a comillas simples. Si usted uso comillas ' cambielas por comillas dobles.

print('Axel')
#
# 3- Escriba la variable meal y asignele el valor de breakfast e imprimalo. Luego cambie el valor asignado por launch e imprimalo.
#

meal = "breakfast"
meal = "lunch"

# 4- Donde se encuentra el error de la siguiente linea de codigo? meal = "launch, breakfast and "tea". Guarde en un string su respuesta y asignela a una variable llamada error_encontrado. Ahora en una nueva variabla llamada tipo_de_error asignele un string con el tipo de error: "sintax error" o "name error".
#
error_encontrado = "launch, breakfast and tea"

tipo_de_error = "sintax error"

# 5- Escriba en diferentes variables las ultimas 3 peliculas que vio y asigneles su propio rating (puede ser flotante) segun su criterio.

the_dark_knight = 7.9
interstellar = 8.4
german_movie = 5

# 6- Imprima el resultado de la siguiente ecuacion: 25 * 68 + 13 / 28

print(25 * 68 + 13 / 28)

#1700.4642857142858
# 7- Imprima el resultado de la siguiente operacion: 80 / 0
#

print(80 / 0)
#ZeroDivisionError: division by zero

# 8- ¡Has decidido meterte en el mundo de tejer edredones! Para calcular el número de cuadrados que necesitarás para tu primera colcha, vamos a crear dos variables: quilt_width y quilt_length. Hagamos este primer edredón de 8 cuadrados de ancho y 12 de largo. Imprime el número de cuadrados que necesitarás para crear el edredón!
#

quilt_width = 8
quilt_length = 12
print(quilt_width * quilt_length)
#96


precio_total = 0
zapatillas_nuevas = 50.00
nice_sweater = 39.00
fun_books = 20.00

# 9- Concatenar las cadenas siguientes y guardar el mensaje que forman en la variable mensaje.
#
# string1 = "The wind, "
# string2 = "which had hitherto carried us along with amazing rapidity, "
# string3 = "sank at sunset to a light breeze; "
# string4 = "the soft air just ruffled the water and "
# string5 = "caused a pleasant motion among the trees as we approached the shore, "
# string6 = "from which it wafted the most delightful scent of flowers and hay."
# 10- Estamos haciendo compras en línea y encontramos un par de zapatillas nuevas. Justo antes de que nos vayamos, encontramos un bonito suéter y algunos libros que también queremos comprar! Utilice el operador += para actualizar el precio_total e incluir los precios de nice_sweater y fun_books.
#

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

mensaje = string1 + string2 + string3 + string4 + string5 + string6


# El producto y el precio que ya tienes en el carrito de compras es: zapatillas_nuevas = 50.00. Los precios de los nuevos articulos agregados al carrito son: nice_sweater = 39.00 y fun_books = 20.00.
#

precio_total+=zapatillas_nuevas
precio_total+=nice_sweater
precio_total+=fun_books

print(precio_total)


# 11- Asigne el string: "Stranger, if you passing meet me and desire to speak to me, why should you not speak to me? And why should I not speak to you?" a la variable to_you


to_you = "Stranger, if you passing meet me and desire to speak to me, why should you not speak to me? And why should I not speak to you?"