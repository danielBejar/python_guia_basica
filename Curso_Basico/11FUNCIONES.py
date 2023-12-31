#las funciones en py primero deben definirse, para que el compilador sepa que se trata de una funcion, para eso usamos el comando def

def SUMA(num1,num2): #"Acordarse siempre de poner :"
    """Documentacion de la funciona(explica que hace la funcion, que valores necesita y que valores recibe) cuando le apoyamos el cursor"""
    s= num1 + num2
    return s

#Aca ya salimos de la funcion.
A=int(input("Ingrese el numero1:"))
B=int(input("Ingrese el numero2:"))
s=SUMA(A,B)
print("1-------")
print("La suma total es:",s)

#Tambien se puede pasar valores en la misma linea donde llamamos a la funcion. EJ
s=SUMA(num2=50,num1=50) #Vemos que en este caso da igual el orden de como pasemos las variables
                        #Si ponemos el nombre de las variables correctamente, ese valor sera asignado a esa variable,
                        # sin importar si era la primera o la segunda.

print("2-------")
print("La suma total es:",s)
#Si necesitamos podemos regresar todos los valores o datos que necesitamos

#---------------------------------------------------------------------------------------------

# Podes devolver mas de un valor si es necesario. EJ return s,true,"suma realizada" , etc como se muestra en la funcion SUMANUEVA
def SUMANUEVA(num1:int,num2:float): #Aca definimos los tipos de variables que vamos a recibir
    s= num1 + num2
    return s, True, "Suma realizada con exito"
    

s=SUMANUEVA(num2=50,num1=50)  
print("3-------")
print("La suma total es:",s) #Aca va a mostrar 3 parametros debido a que la funcion SUMANUEVA, devuelve 3 parametros.

#si quiero separar estos valores, para mostrarlos uno a uno, hariamos lo siguiente
s,boll,string=SUMANUEVA(num2=50,num1=50) #Devuelve lo multiples valores de return, por orden de devolucion
print("4-------")
print("La suma total es:",s)
print("El estado de la suma es",boll)
print(string)

#---------------------------------------------------------------------------------
#Podemos enviar mas de un valor a un funcion, para eso ponemos un * a la variable
def imprimir_nombres(*nombres): #Cuando le ponemos un asterisco, podemos pasar mas de un valor, la variable *numeros ahora tiene infinitas dimesiones.
    print("Los nombres recibidos son:",nombres)

imprimir_nombres("Daniel", "Dario","Diego")

#Se puede realizar un for para recorrer las multiples variables enviadas a una funcion
def numeros(*numeros): #numeros es una TUPLA, es decir que los valores enviados a la funcion no se pueden modificar.
    print(type(numeros))#muestra el tipo de datos que es numero (una tupla).
    for valores in numeros:
        print(valores,end=" ")

numeros(1,2,3,4,5,6,7,8,9)