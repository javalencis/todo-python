import sqlite3
con = sqlite3.connect("todo.db")
cur = con.cursor()

def pedirDatos():
    datos =[];
    datos.append(input("Nombre: "))
    datos.append(input("Prioridad: "))
    datos.append( input("Estado: "))
    datos.append(input("Fecha estimada(YYYY-MM-DD): "))
    return (','.join(datos))

def mensajes():
    return print("""
-------------------------------------------------
Para un nuevo registro ingrese la opcion 1: 
Para imprimir todos los registros ingrese 2: 
Para terminar ingrese 0: 
    """)


print("Hola, Bienvenido\n")
mensajes()

opcion = int(input("=> "))

while(opcion != 0):
    
    if(opcion == 1):
        datos = pedirDatos()
        cur.execute(f"INSERT INTO tareas VALUES (${datos[0]},${datos[1]}, ${datos[2]},${datos[3]})")
    elif(opcion == 2):
        pass
        #Imprimir todos los registros
    mensajes()
    opcion = int(input("=>"))
print("Gracias por usar nuestro programa")

con.commit()    
con.close()

