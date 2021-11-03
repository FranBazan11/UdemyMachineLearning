import os

os.system("clear")
print("------------------------------------------------")
print("Bienvenidos al historial clinica del Hospital 🏥")
print("------------------------------------------------")

# GLOBAL PROPERTIES
flag = True
database = list()
# database = [{'Name': 'Juan', 'Clinic': 'resfrio'}, {'Name': 'PEDRO', 'Clinic': 'asma'}]


#FUNCTIONS
def showMenu():
    print("QUE QUIERE HACER? \n")
    print("Opcion 1 -> Cargar paciente")
    print("Opcion 2 -> Buscar paciente")
    print("Opcion 3 -> Listar paciente")
    print("Opcion 4 -> Salir\n")
    option = input("INGRESE UNA OPCION: ")
    os.system("clear")
    return option

def createPatient():
    name = input("NOMBRE: ")
    clinic = input("HISTORIAL CLINICA DEL PACIENTE: ")
    patient = {"Name": name, "Clinic" : clinic}
    database.append(patient)
    

def searchPatient(name):
    isFinded = True
    while isFinded:
        for patient in range(len(database)):
            if name.lower() == database[patient]["Name"].lower():
                print("PACIENTE ENCONTRADO Y SU HISTORIA CLINA ES: " + database[patient]["Clinic"])
            else:
                isFinded = False
        if not isFinded:
            print("Paciente no encontrado")

def listPatient():
    print("INICIO LISTADO PACIENTES")
    for patient in range(len(database)):
        print("Nombre ".ljust(5) + database[patient]["Name"].upper(), " \t Historia clinica: ".ljust(5) + database[patient]["Clinic"] )
    print("FIN LISTADO PACIENTES")

def switchOptions(intOption):

    if intOption.isdigit():

        intOption = int(intOption)
        
        if intOption >= 1 and intOption <= 4:
            if intOption == 1:
                print("INGRESE PACIENTE\n")
                createPatient()
                print(database)
            elif intOption == 2:
                name = input("INGRESE NOMBRE DEL PACIENTE: ")
                searchPatient(name)
            elif  intOption == 3:
                print("LISTANDO PACIENTES\n")
                listPatient()
            elif intOption == 4:
                print("NOS VEMOS PRONTO\n")
                
        else:
            print("Fuera de rango")

        return intOption
    else:
        print("Entrada incorrecta")

#LOOP GENERAL
while flag: 

    option = showMenu()
    intOption = switchOptions(option)

    if intOption == 4:
        flag = False