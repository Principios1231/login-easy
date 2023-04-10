#definimos users
users = {}

#llamamos a users.txt
with open("users.txt") as us:
    for linea in us:
        if ":" not in linea:
            continue
        name, password = linea.strip().split(":")
        users[name] = password

#definimos login    
def login():
    print("+-------------------------------------+")
    print("     Ingresa tu nombre de usuario      ")
    print("+-------------------------------------+")
    n_u = input("")
    
    #si el nombre esta en users.txt pedir contraseña
    if n_u in users:
        print("+-------------------------------------+")
        print("         Ingresa tu contraseña         ")
        print("+-------------------------------------+")
        pwd_u = input()
        #si es la contraseña del nombre en users, inicia la aplicacion
        if users[n_u] == pwd_u:
            print("Bienvenidos")#Añade modulos de otras funciones o escribe tu codigo.
        #si no, reinicia el proceso de login
        else:
            print("+-------------------------------------------------------+")
            print("La contraseña ingresada es incorrecta, Intenta nuevamente")
            print("+-------------------------------------------------------+")
            login()
            
    #si no esta en users.txt, pregunta si quiere registrarse
    else:
        print("+-------------------------------------+")
        print("         Usuario no registrado         ")
        print("          deseas registrarte?          ")
        print("                 (S/N)                 ")
        print("+-------------------------------------+")
        pwd_u = input("")
        #si la respuesta es s sin importar mayusculas, lleva a cabo el proceso de registro
        if pwd_u == "s".lower():
            reg()
        
        #si no, reinicia el logeo
        else: login()


#definimos reg
def reg():
    print("+-------------------------------------+")
    print("     Ingresa tu nombre de usuario      ")
    print("+-------------------------------------+")
    ureg = input("")

    if reg in users:
        print("Este nombre de usuario ya existe, intenta con otro")
        reg()
    else: 
        print("+-------------------------------------+")
        print("Introduce tu contraseña:")
        print("+-------------------------------------+")
        pwd = input("")
        users[reg] = pwd
        with open("users.txt", "a") as r:
            r.write("{}:{}\n".format(ureg, pwd))
            print("registrado correctamente")

login()