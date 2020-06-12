# 1- Tenemos un listado de estudiantes con el puntaje de sus exámenes guardado en un array 2-d llamado student_scores. La primera fila guarda el puntaje del primer examen, la segunda fila guarda el segundo examen, luce como la siguiente tabla
# 2- Cree el array de 2-d de forma manual
# 3- Tania quiere saber cómo le fue en el tercer examen. Selecciona su puntaje desde el array y guárdalo en una variable llamada tanya_test_3
# 4- El profesor tiene una reunión con los padres de Cody y el quiere tener el resultado de sus exámenes a la mano. Seleccione todos los puntajes de Cody y guardelos en un nuevo array llamado cody_test_scores


student_scores = np.array([
    [92,94,88,91,87],
    [79,100,86,93,91],
    [87,85,72,90,92]
])

tanya_test_3 = student_scores[2,0]
cody_test_scores = student_scores[:, 4]
print(cody_test_scores)

