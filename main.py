from paciente import registrar_paciente
from medico import registrar_medico
from cita import registrar_cita
from atencion import registrar_atencion


pacientes = []
medicos = []
citas = []
atenciones = []


# ==========================================
# MOSTRAR REGISTROS
# ==========================================

def mostrar_registros(lista):

    if len(lista) == 0:
        print("\nNo existen registros.")
    else:
        for elemento in lista:
            elemento.mostrar_datos()


# ==========================================
# BUSCAR PACIENTE
# ==========================================

def buscar_paciente():

    numero = input("\nIngrese el número de documento: ")

    for paciente in pacientes:
        if paciente.get_numero() == numero:
            paciente.mostrar_datos()
            return paciente

    print("\nPaciente no encontrado.")
    return None


# ==========================================
# BUSCAR MÉDICO
# ==========================================

def buscar_medico():

    codigo = input("\nIngrese el código del médico: ")

    for medico in medicos:
        if medico.get_codigo() == codigo:
            medico.mostrar_datos()
            return medico

    print("\nMédico no encontrado.")
    return None


# ==========================================
# FILTRAR MÉDICOS
# ==========================================

def filtrar_medicos():

    print("\n" + "=" * 50)
    print("        BÚSQUEDA POR ESPECIALIDAD")
    print("=" * 50)

    print("1. Medicina General")
    print("2. Pediatría")
    print("3. Obstetricia")
    print("4. Ginecología")
    print("5. Urología")
    print("6. Cirugía General")
    print("7. Nutrición")
    print("8. Odontología")

    opcion = input("Seleccione una especialidad: ")

    if opcion == "1":
        especialidad = "Medicina General"
    elif opcion == "2":
        especialidad = "Pediatría"
    elif opcion == "3":
        especialidad = "Obstetricia"
    elif opcion == "4":
        especialidad = "Ginecología"
    elif opcion == "5":
        especialidad = "Urología"
    elif opcion == "6":
        especialidad = "Cirugía General"
    elif opcion == "7":
        especialidad = "Nutrición"
    elif opcion == "8":
        especialidad = "Odontología"
    else:
        print("Opción no válida.")
        return

    resultado = filter(
        lambda medico: medico.get_especialidad() == especialidad,
        medicos
    )

    encontrados = list(resultado)

    if len(encontrados) == 0:
        print("\nNo se encontraron médicos.")
    else:
        for medico in encontrados:
            medico.mostrar_datos()


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def menu():

    while True:

        print("\n" + "=" * 60)
        print("                  CLÍNICA KAWSAY")
        print("          SISTEMA DE GESTIÓN DE ATENCIÓN")
        print("=" * 60)

        print("1. Registrar paciente")
        print("2. Registrar médico")
        print("3. Registrar cita")
        print("4. Registrar atención")
        print("5. Mostrar pacientes")
        print("6. Mostrar médicos")
        print("7. Mostrar citas")
        print("8. Mostrar atenciones")
        print("9. Buscar paciente")
        print("10. Buscar médico")
        print("11. Buscar médico por especialidad")
        print("12. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":

            paciente = registrar_paciente()

            if paciente is not None:
                pacientes.append(paciente)

        elif opcion == "2":

            medico = registrar_medico()

            if medico is not None:
                medicos.append(medico)

        elif opcion == "3":

            cita = registrar_cita(pacientes, medicos)

            if cita is not None:
                citas.append(cita)

        elif opcion == "4":

            atencion = registrar_atencion(citas)

            if atencion is not None:
                atenciones.append(atencion)

        elif opcion == "5":
            mostrar_registros(pacientes)

        elif opcion == "6":
            mostrar_registros(medicos)

        elif opcion == "7":
            mostrar_registros(citas)

        elif opcion == "8":
            mostrar_registros(atenciones)

        elif opcion == "9":
            buscar_paciente()

        elif opcion == "10":
            buscar_medico()

        elif opcion == "11":
            filtrar_medicos()

        elif opcion == "12":

            print("\nPrograma finalizado.")
            break

        else:
            print("\nOpción no válida.")


menu()