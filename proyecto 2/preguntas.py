sis = []
usuarios_no_infectados = []
usuario_en_revision = []
posibles = []
infectados = []
cant_de_sis = 0

class users():
    def __init__(self,nombre_completo,edad):
        self.nombre_completo = nombre_completo
        self.edad = edad
class no_infectado(users):
    def __init__(self,nombre_completo,edad,telefono):
        super.__init__(nombre_completo,edad)
        self.telefono = telefono
class posible_inf(users):
    def __init__(self,nombre_completo,edad,telefono,estado,ciudad,residencia):
        super.__init__(nombre_completo,edad)
        self.telefono = telefono
        self.estado = estado 
        self.ciudad = ciudad 
        self.residencia = residencia
class infect(users):
    def __init__(self,nombre_completo,edad,telefono,estado,ciudad,residencia,nombre_doctor):
        super.__init__(nombre_completo,edad)
        self.telefono = telefono
        self.estado = estado 
        self.ciudad = ciudad 
        self.residencia = residencia
        self.nombre_doctor = nombre_doctor
def preguntas():
  
        nombre = input("Nombre: ")      
        vali_nombre = nombre.isalpha()
        while vali_nombre== False:
            print("--- Solo pueden ser letras ---")
            nombre = input("Nombre: ")      
            vali_nombre = nombre.isalpha()
        apellido = input("Apellido:")
        vali_apell = apellido.isalpha()
        while vali_apell == False:
            print("--- Solo pueden ser letras ---")
            apellildo = input("Apellido: ")
            vali_apell = apellido.isalpha()
        nombre = nombre.title()
        apellildo = apellido.title()
        nombre_completo = nombre +" "+apellido
        edad = input("edad: ")
        vali_edad = edad.isdigit()
        while vali_edad == False:
            print("--- Solo pueden ser numeros ---")
            edad = input("Edad: ")
            vali_edad = edad.isdigit() 

        print("Hola {}, vamos a ver si moriras\n".format(nombre_completo))

        preg1 = input("\n¿Tiene secreciones nasales?\nSi ---> (S)\nNo ---> (N)\n ")
        while preg1!="S" and preg1!="s" and preg1!="N" and preg1!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ")
            preg1 = input("\n¿Tiene secreciones nasales?\nSi ---> (S)\nNo ---> (N)\n ")
        if preg1=="s" or preg1=="S":
            sis.append(1)


        preg2 = input("\n¿Tiene dolor de garganta?\nSi ---> (S)\nNo ---> (N)\n ")
        while preg2!="S" and preg2!="s" and preg2!="N" and preg2!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ")
            preg2 = input("¿Tiene dolor de garganta?\nSi ---> (S)\nNo ---> (N)\n ")
        if preg2=="s" or preg2=="S":
            sis.append(1)


        preg3 = input("\n¿Tiene tos?\nSi ---> (S)\nNo ---> (N)\n ")
        while preg3!="S" and preg3!="s" and preg3!="N" and preg3!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ")
            preg3 = input("\n¿Tiene tos?\nSi ---> (S)\nNo ---> (N)\n ")
        if preg3=="s" or preg3=="S":
            sis.append(1)


        preg4 = input("\n¿Tienes fiebre?\nSi ---> (S)\nNo ---> (N)\n ")
        while preg4!="S" and preg4!="s" and preg4!="N" and preg4!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ")
            preg4 = input("¿Tienes fiebre?\nSi ---> (S)\nNo ---> (N)\n ")
        if preg4=="s" or preg4=="S":
            sis.append(1)


        preg5 = input("\n¿dificultad para respirar?\nSi ---> (S)\nNo ---> (N)\n ")
        while preg5!="S" and preg5!="s" and preg5!="N" and preg5!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ")
            preg5 = input("\n¿dificultad para respirar?\nSi ---> (S)\nNo ---> (N)\n ")
        if preg5=="s" or preg5=="S":
            sis.append(1)

            
        if len(sis)<=2:
            estatus = "No infectado"
        elif len(sis)>2 and len(sis)<5:
            estatus = "Posible infectado"
        elif len(sis)==5:
            estatus = "Infectado"
        print('hola {}, su estatus es: {}'.format(nombre_completo,estatus))
        sis.clear()
        
        usuario_en_revision.append(nombre_completo)
        usuario_en_revision.append(edad)
        usuario_en_revision.append(estatus)

        return nombre_completo,edad


        

def txt():
    if usuario_en_revision[2]=="No infectado":
        telefono = input("Numero telefonico: ")
        vali_telefono = telefono.isdigit()
        while vali_telefono == False:
            print("--- Solo pueden ser numeros ---")
            telefono = input("Numero telefonico: ")
            vali_telefono = telefono.isdigit()       
        usuario_en_revision.append(telefono)           
        with open ('no_infectado.txt','r') as fh:
            datos = fh.readlines()
            for x in datos:
                usuario = x[:-1].split(',')
                usuarios_no_infectados.append(usuario)
        with open ('no_infectado.txt','w') as fh:
            fh.write('{},{},{},{}\n'.format(usuario_en_revision[0],usuario_en_revision[1],usuario_en_revision[2],usuario_en_revision[3]))
        for x in usuarios_no_infectados:
            with open ('no_infectado.txt','a') as fh:
                fh.write('{},{},{},{}\n'.format(x[0],x[1],x[2],x[3]))
        return telefono


    elif usuario_en_revision[2]=="Posible infectado":
        telefono = input("Numero telefonico: ")
        vali_telefono = telefono.isdigit()
        while vali_telefono == False:
            print("--- Solo pueden ser numeros ---")
            telefono = input("Numero telefonico: ")
            vali_telefono = telefono.isdigit()
        estado = input("En que estado va a estar usted en cuarentena: ")
        vali_estado = estado.isalpha()
        while vali_estado == False:
            print("--- Solo pueden ser letras ---")
            estado = input("En que estado va a estar usted en cuarentena: ")
            vali_estado = estado.isalpha()
        ciudad = input("En que ciudad se va a encontrar: ")
        vali_ciudad = ciudad.isalpha()
        while vali_ciudad == False:
            print("--- Solo pueden ser letras ---")
            ciudad = input("En que ciudad se va a encontrar: ")
            vali_ciudad = ciudad.isalpha() 
        residencia = input("Su residencia: ")
        vali_resi = residencia.isalpha()
        while vali_resi == False:
            print("--- Solon pueden ser letras ---")
            residencia = input("Su residencia: ")
            vali_resi = residencia.isalpha()   
        usuario_en_revision.append(telefono)
        usuario_en_revision.append(estado)
        usuario_en_revision.append(ciudad)
        usuario_en_revision.append(residencia)
        with open ('posible.txt','r') as fh:
            lineas = fh.readlines()
            for x in lineas:
                usuario = x[:-1].split(',')
                posibles.append(usuario)
        with open ('posible.txt','w') as fh:
            fh.write('{},{},{},{},{},{},{}\n'.format(usuario_en_revision[0],usuario_en_revision[1],usuario_en_revision[2],usuario_en_revision[3],usuario_en_revision[4],usuario_en_revision[5],usuario_en_revision[6]))
        for x in posibles:
            with open ('posible.txt','a') as fh:
                fh.write('{},{},{},{},{},{},{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))
        return telefono,estado,ciudad,residencia
    
    elif usuario_en_revision[2]=="Infectado":
        telefono = input("Numero telefonico: ")
        vali_telefono = telefono.isdigit()
        while vali_telefono == False:
            print("--- Solo pueden ser numeros ---")
            telefono = input("Numero telefonico: ")
            vali_telefono = telefono.isdigit()
        estado = input("En que estado va a estar usted en cuarentena: ")
        vali_estado = estado.isalpha()
        while vali_estado == False:
            print("--- Solo pueden ser letras ---")
            estado = input("En que estado va a estar usted en cuarentena: ")
            vali_estado = estado.isalpha()
        ciudad = input("En que ciudad se va a encontrar: ")
        vali_ciudad = ciudad.isalpha()
        while vali_ciudad == False:
            print("--- Solo pueden ser letras ---")
            ciudad = input("En que ciudad se va a encontrar: ")
            vali_ciudad = ciudad.isalpha() 
        residencia = input("Su residencia: ")
        vali_resi = residencia.isalpha()
        while vali_resi == False:
            print("--- Solon pueden ser letras ---")
            residencia = input("Su residencia: ")
            vali_resi = residencia.isalpha()       
        nombre = input("Nombre de su doctor: ")
        vali_nombre = nombre.isalpha()
        while vali_nombre== False:
            print("--- Solo pueden ser letras ---")
            nombre = input("Nombre: ")      
            vali_nombre = nombre.isalpha()
        apellido = input("Apellido de su doctor: ")
        vali_apell = apellido.isalpha()
        while vali_apell == False:
            print("--- Solo pueden ser letras ---")
            apellido = input("Apellido: ")
            vali_apell = apellido.isalpha()
        nombre = nombre.title()
        apellido = apellido.title()
        nombre_doctor = nombre+" "+apellido
        usuario_en_revision.append(telefono)
        usuario_en_revision.append(estado)
        usuario_en_revision.append(ciudad)
        usuario_en_revision.append(residencia)
        usuario_en_revision.append(nombre_doctor)
        with open ('infectados.txt','r') as fh:
            lineas = fh.readlines()
            for x in lineas:
                usuario = x[:-1].split(',')
                infectados.append(usuario)
        with open ('infectados.txt','w') as fh:
            fh.write('{},{},{},{},{},{},{},{}\n'.format(usuario_en_revision[0],usuario_en_revision[1],usuario_en_revision[2],usuario_en_revision[3],usuario_en_revision[4],usuario_en_revision[5],usuario_en_revision[6],usuario_en_revision[7]))
        for x in infectados:
            with open ('infectados.txt','a') as fh:
                fh.write('{},{},{},{},{},{},{},{}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))
        return telefono,estado,ciudad,residencia,nombre_doctor
    usuario_en_revision.clear()

def ver_no_inf():
    no_infe = []
    with open ('no_infectado.txt','r') as fh:
        lineas = fh.readlines()
        for x in lineas:
            todos = x[:-1].split(',')
            no_infe.append(todos)

    for x in no_infe:
        print('Nombre: {}...Edad: {}...Estatus: {}...Telefono: {}\n'.format(x[0],x[1],x[2],x[3]))


def ver_posi():
    no_infe = []
    with open ('posible.txt','r') as fh:
        lineas = fh.readlines()
        for x in lineas:
            todos = x[:-1].split(',')
            no_infe.append(todos)
    for x in no_infe:
        print('Nombre: {}...Edad: {}...Estado: {}...Telefono: {}...\n...Estado: {}...Ciudad: {}...Residencia: {}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6]))



def ver_inf():
    no_infe = []
    with open ('infectados.txt','r') as fh:
        lineas = fh.readlines()
        for x in lineas:
            todos = x[:-1].split(',')
            no_infe.append(todos)
    for x in no_infe:
        print('Nombre: {}...Edad: {}...Estado: {}...Telefono: {}...\n...Estado: {}...Ciudad: {}...Residencia: {}...Doctor: {}\n'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7]))



def buscador():

    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}
    print('Coloque paises con una sola palabra, ej.: Spain, Venezuela, France.\nY disculpe las molestias')
    country = input("Que pais desea buscar: ")
    # vali_country = country.istitle()
    # while vali_country == False:
    #     print("--- Solo pueden ser letras ---")
    #     country = input("Que pais desea buscar: ")
    #     vali_country = country.istitle()
    country = country.title()
    querystring['country'] = country

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "599a4c8ca9msh7a16cede31260c1p125f76jsnddcaf4aae878"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    dic = response.json()

    todos = []
    canada = []
    canada.append(dic['data']['covid19Stats'])
    confirmed = []
    recovered = []
    muertes = []
    pais = []
    for x in canada:
        todos.append(x)
        for y in x:
            pais.append(y['country'])
            muertes.append(y['deaths'])
            confirmed.append(y['confirmed'])
            recovered.append(y['recovered'])
    total_muertes = sum(muertes)
    total_conf = sum(confirmed)
    total_recov = sum(recovered)
    if country in pais:
        print('\n-- {} --\nConfirmed: {}...Muertes: {}...Recovered: {}'.format(country,total_conf,total_muertes,total_recov))
    elif country not in pais:
        print("\n-- Ese pais no existe --")
        print('\n-- Mundial --\nConfirmed: {}...Muertes: {}...Recovered: {}'.format(total_conf,total_muertes,total_recov))



def muertes():
    
    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}


    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "599a4c8ca9msh7a16cede31260c1p125f76jsnddcaf4aae878"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # todos = dic['data']['covid19Stats']
    todo=[]
    dic= response.json()
    muer={}
    posci = []
    print('\t----------- Paises con mas muertes -----------')
    for x in dic['data']['covid19Stats']:
        if x['country'] in muer:
            muer[x['country']]= muer[x['country']]+ x['deaths']
        else:
            muer[x['country']]= x['deaths']
    for x in muer.items():
        todo.append((x[0],x[1]))
        todo.sort(key=lambda todo: int(todo[1]), reverse=True)    
    for x in todo:
        print('\t{}......{}'.format(x[0],x[1]))
        posci.append(1)
        if len(posci)==10:
            break


def recuperados():
    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}


    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "599a4c8ca9msh7a16cede31260c1p125f76jsnddcaf4aae878"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # todos = dic['data']['covid19Stats']
    todo=[]
    dic= response.json()
    muer={}
    posci = []
    print('\t----------- Paises con mas recuperados -----------')
    for x in dic['data']['covid19Stats']:
        if x['country'] in muer:
            muer[x['country']]= muer[x['country']]+ x['recovered']
        else:
            muer[x['country']]= x['recovered']
    for x in muer.items():
        todo.append((x[0],x[1]))
        todo.sort(key=lambda todo: int(todo[1]), reverse=True)    
    for x in todo:
        print('\t{}......{}'.format(x[0],x[1]))
        posci.append(1)
        if len(posci)==10:
            break

def confir():
    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}


    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "599a4c8ca9msh7a16cede31260c1p125f76jsnddcaf4aae878"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    # todos = dic['data']['covid19Stats']
    todo=[]
    dic= response.json()
    muer={}
    posci = []
    print('\t-------- Paises con mas casos confirmados --------')
    for x in dic['data']['covid19Stats']:
        if x['country'] in muer:
            muer[x['country']]= muer[x['country']]+ x['confirmed']
        else:
            muer[x['country']]= x['confirmed']
    for x in muer.items():
        todo.append((x[0],x[1]))
        todo.sort(key=lambda todo: int(todo[1]), reverse=True)    
    for x in todo:
        print('\t{}......{}'.format(x[0],x[1]))
        posci.append(1)
        if len(posci)==10:
            break


def main():
    print('\t---------------- Bienvenido ----------------n')
    while True:
        que_desea = input('\nQue desea hacer:\nEvaluarse ---> (1)\nBuscar estadisticas de un pais ---> (2)\nPaises con mas muertes ---> (3)\nPaises con mas confirmados ---> (4)\nPaises con mas recuperados ---> (5)\nInformacion de usuarios ---> (6)\n ')
        while que_desea!="1" and que_desea!="2" and que_desea!="3" and que_desea!="4" and que_desea!="5" and que_desea!="6":
            print("--- Solo se puede colocar 1, 2, 3, 4, 5 o 6 ---")
            que_desea = input('Que desea hacer:\nEvaluarse ---> (1)\nBuscar estadisticas de un pais ---> (2)\nPaises con mas muertes ---> (3)\nPaises con mas confirmados ---> (4)\nPaises con mas recuperados ---> (5)\n ')
        if que_desea=="1":
            preguntas()
            txt()
        elif que_desea=="2":
            buscador()
        elif que_desea=="3":
            muertes()
        elif que_desea=="4":
            confir()
        elif que_desea=="5":
            recuperados()
        elif que_desea=="6":
            infor = input("Que usuarios necesita:\nNo infectados ---> (1)\nPosibles infectados ---> (2)\nInfectados ---> (3)\n ")
            while infor!="1" and infor!="2" and infor!="3":
                print("--- Solo pueden ser los numeros 1, 2 o 3")
                infor = input("Que usuarios necesita:\nNo infectados ---> (1)\nPosibles infectados ---> (2)\nInfectados ---> (3)\n ")
            if infor=="1":
                ver_no_inf()
            elif infor=="2":
                ver_posi()
            elif infor=="3":
                ver_inf()
        algo_mas = input("\nDesea hacer algo mas:\nSi ---> (S)\nNo ---> (N)\n ")
        while algo_mas!="S" and algo_mas!="s" and algo_mas!="N" and algo_mas!="n":
            print("--- Solo pueden ser las letras 'S' o 'N' ---")
            algo_mas = input("Desea hacer algo mas:\nSi ---> (S)\nNo ---> (N)\n ")
        if algo_mas=="N" or algo_mas=="n":
            break 
    print("\t--- Recuerde quedarse en su casa ---")
main()
