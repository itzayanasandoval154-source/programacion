 #python usa la sangría (espacios al inicio de la linea)  para delimitar bloques de codigo.{}, python usa 4 espacios por nivel. Esta es la diferencia viasual mas importante entre python y otros lenguajes.

 #if condicion:
#    instruccion1
#else:
#    instruccion2

#Toda estructura de control termina de control termina su primera linea con dos puntos ":". Los dps puntos le dicen a python : el bloque de estructura comienza en la siguiente linea. Si se omiten, python genera SintaxisError: expect ':'

#= asignar un valor
#== comparar dos valores iguales que
#!= diferente de
#> mayor que/ >= mayor o igual que
#< menor que / <= menor o igual
# and ambas condiciones true/ or al manos una es true/ not negacion logica

#IF ejecuta un bloque unicamente si la condicion es true. si la condicion es false, el bloque se salta por completo y el programa continua. solo tiene una rama posible. 

#Si condicion ENTONCES
#    instrcuccion
#FIN SI
#     SI FALSE-> se omite el bloque

#condicon simple
nota = 8.5
if nota >=6.0:
    print("El alumno aprobo")

    print("Fin del programa")

 
 #condicion doble - IF/ELSE
 #El else garantiza que SIEMPRE se ejecuta algo. Sin importar si la condicon es true o false, el programa toma uno de los dos caminos. nuna queda casos sin respuesta.

# ejercicio 2

CALIFICACION_MINIMA = 7.0
nota = float(input("ingresa tu calificacion"))

if nota >=CALIFICACION_MINIMA :
    print(f"aprobado con{nota:.1f}")
else:
    print(f"reprobado con {nota:.1f}")
    faltaron = CALIFICACION_MINIMA - nota
    print(f"te faltaron {faltaron:.1f} puntos para aprobar")




    #condiciones compuestas: and / or en accion

    edad = int(input("tu edad: "))
    tiene_ine = input("¿Tienes INE (si/no): ")
 
    if edad >= 18 and tiene_ine == "si":
        print("puedes votar")
    else:
        print("no puedes votar aún")


        #validacion de rango con 'and'y 'or'
        calificacion = float(input("calificacion (0-10)"))
        

        if calificacion <0 or calificacion >10:
         print("calificacion fuera de rango")
        else:
         print(f"calificacion registrada: {calificacion:.1f}") 


#Tu turno: 
# Crea una condición que verifique si un año es bisiesto. 
# Un año es bisiesto si es divisible entre 4, Y si es divisible entre 100,
#  también debe ser divisible entre 400. Pista: usa el operador % (módulo).

año = int(input("Ingresa un año: "))

if (año % 4 == 0) and (año % 100 != 0 or año % 400 == 0):
    print("El año es bisiesto.")
else:
    print("El año no es bisiesto.")