# for // repite un bloque para cada elemento de una secuencia. 
#se usa cuando sabes de antemano cúantas veces repetir o 
#cuando quieres recorrer los elementos de una lista, rango o cadena.

#ejercicio: variante de range()
#range(fin) - empieza en 0, termina antes del fin
print("range(5)")
for i in range(5):
     print (i, end= "") # 1 2 3 4
print()
#range(inicio, fin)
print("range(1, 6)")
for i in range(1, 6):
     print(i, end=" ") #12345
print()
#range(inicio, fin, paso) - paso personalizado
print("pares del 0 al 10")
for i in range(0, 11, 2):
     print(i, end=" ")
     print()
     #cuenta regresiva con paso negativo
     print("cuenta regresiva")
     for i in range(5, 0, -1):
         print(i, end=" ")
print("despegue")
         
#Tu turno: Escribe un for que imprima solo los múltiplos de 3 
# entre 3 y 30 usando range() con los argumentos correctos. No uses if 
# dentro del for para filtrar — usa el paso de range().
print("rango de 3 a 30")
for i in range(3, 31, 3):
      print(i, end= "")
print()

#ejercicio - for recorriendo una lista: promedio y conteo
#el for no solo funciona con numeros.
#puede recorrer  cualquier y acumular resulstados.

calificaciones = [8.5, 9.0, 6.5, 10.0, 7.5, 5.0, 8.0]
for calificacion in calificaciones: 
     print(f"Calificación: {calificacion:.1f}")

total = 0
aprobados = 0

max_cal = calificaciones[0]
min_cal = calificaciones[0]

for calificacion in calificaciones:
    total = total + calificacion
    if calificacion >= 6.0:
        aprobados = aprobados + 1
    if calificacion> max_cal:
        max_cal = calificacion
    if calificacion < min_cal:
        min_cal = calificacion


promedio = total / len(calificaciones)
reprobados = len(calificaciones) - aprobados

print(f"\nPromedio del grupo: {promedio:.2f}")
print(f"Aprobados: {aprobados}")
print(f"Reprobados: {reprobados}")
print(f"Calificación más alta: {max_cal}")
print(f"Calificación más baja: {min_cal}")

#Turno: encuentra e imprime la calificación más alta y la más baja. Necesitarás dos variables que guarden el máximo y 
# el mínimo mientras recorres la lista.
notas =[9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 5.5]
# iniciar con las variables de el primer valor de la lista 
max_cal = notas[0]
min_cal = notas[0]

#recorre la lista 
for nota in notas:
     if nota > max_cal:
          max_cal= nota
          if nota < min_cal:
               min_cal = nota
               print(f"nota mas alta:{max_cal}") 
               print(f"nota mas baja: {min_cal}")



#----------------------------------
#Ejercicio: for con enumarate(): índice y valor juntos.
#enumerate() te da la posición y el valor en cada iteración. Múy útil para reportes numerados.

alumnos = ["Iran", "Povedano", "Gissel", "Susana", "Zeus", "Carlos", "Sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 5.5]

#encabezado de la tabla
print(f"{'No.':<5} {'Alumno':<12} {'Nota':>6} {'Estado':<10}")
print("-"*37)

for i, alumno in enumerate(alumnos):
    nota = notas[i]
    estado = "Aprobado" if nota >= 7.0 else "Reprobado"
    print(f"{i+1:<5} {alumno:<12} {nota:>6.1f} {estado:<10}")

#Turno: Agrega al ejercicio un resumen al final del reporte: promedio del grupo y cantidad de aprobados, calculados 
# dentro del mismo for que genera el reporte.  
alumnos = ["iran", "povedano", "gissel", "susana", "zeus",  "carlos", "sulub"]
notas = [9.0, 7.5, 8.0, 9.5, 6.0, 10.0, 5.5 ]

#encabezado de la tabla
print(f"{'no.':<5} {'alumno':<12} {'nota':>6} {'estado':<10}")
print("-*37")
#variables para el resumen
suma= 0
aprobados = 0
reprobados = 0

for i, alumno in enumerate (alumnos):
     nota = notas[i]
     estado ="aprobado" if nota >= 7.0 else "reprobado"
     print(f"{i+1:<5} {alumno:<12} {nota:6.1f} {estado:<10}")

#datos del resumen
     suma += nota
if estado == "aprobado":
     aprobados += 1
else:
     reprobados += 1

     #resumen
     promedio = suma /len(notas)
     print("-"*37)
     print(f"promedio del grupo: {promedio:.2f}")
     print(f"aprobados: {aprobados}")
     print(f"reprobados: {reprobados}")
     