print("------------------------------------------------")
print("Bienvenidos al historial clinica del Hospital 🏥")
print("------------------------------------------------")

# GLOBAL PROPERTIES
flag = True
database = list()


#FUNCTIONS
def showMenu():
    print("QUE QUIERE HACER? \n")
    print("Opcion 1 -> Cargar paciente")
    print("Opcion 2 -> Buscar paciente")
    print("Opcion 3 -> Listar paciente")
    print("Opcion 4 -> Salir\n")
    option = input("INGRESE UNA OPCION: ")
    return option

def createPatient():
    name = input("NOMBRE: ")
    clinic = input("HISTORIAL CLINICA DEL PACIENTE: ")
    patient = {"Name": name, "Clinic" : clinic}
    database.append(patient)
    

def searchPatient(name):
    for patient in range(len(database)):
        if database[patient]["Name"] == name:
            print("PACIENTE ENCONTRADO Y SU HISTORIA CLINA ES:" + database[patient]["Clinic"])

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
            elif intOption == 4:
                print("NOS VEMOS PRONTO\n")
        else:
            print("Fuera de rango")
            message = "Fuera de rango"

        return intOption
    else:
        print("Entrada incorrecta")

        return 0, "Entrada incorrecta"


#LOOP GENERAL
while flag: 

    option = showMenu()
    intOption = switchOptions(option)
    
