class Paciente:

    def __init__(self, nombre, edad, fecha_nacimiento, genero, documento,
                 numero, fecha_visita, estado_civil, direccion, seguro, especialidad):

        self._nombre = nombre
        self._edad = edad
        self._fecha_nacimiento = fecha_nacimiento
        self._genero = genero
        self._documento = documento
        self._numero = numero
        self._fecha_visita = fecha_visita
        self._estado_civil = estado_civil
        self._direccion = direccion
        self._seguro = seguro
        self._especialidad = especialidad

    # GETTERS

    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento

    def get_genero(self):
        return self._genero

    def get_documento(self):
        return self._documento

    def get_numero(self):
        return self._numero

    def get_fecha_visita(self):
        return self._fecha_visita

    def get_estado_civil(self):
        return self._estado_civil

    def get_direccion(self):
        return self._direccion

    def get_seguro(self):
        return self._seguro

    def get_especialidad(self):
        return self._especialidad

    # SETTERS

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_edad(self, edad):
        self._edad = edad

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento

    def set_genero(self, genero):
        self._genero = genero

    def set_documento(self, documento):
        self._documento = documento

    def set_numero(self, numero):
        self._numero = numero

    def set_fecha_visita(self, fecha_visita):
        self._fecha_visita = fecha_visita

    def set_estado_civil(self, estado_civil):
        self._estado_civil = estado_civil

    def set_direccion(self, direccion):
        self._direccion = direccion

    def set_seguro(self, seguro):
        self._seguro = seguro

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def mostrar_datos(self):

        print("\n" + "=" * 50)
        print("              DATOS DEL PACIENTE")
        print("=" * 50)

        print("Nombre:", self.get_nombre())
        print("Edad:", self.get_edad())
        print("Fecha de nacimiento:", self.get_fecha_nacimiento())
        print("Género:", self.get_genero())
        print("Documento:", self.get_documento())
        print("Número:", self.get_numero())
        print("Fecha de visita:", self.get_fecha_visita())
        print("Estado civil:", self.get_estado_civil())
        print("Dirección:", self.get_direccion())
        print("Tipo de seguro:", self.get_seguro())
        print("Especialidad:", self.get_especialidad())

        print("=" * 50)


def registrar_paciente():

    print("\n" + "=" * 50)
    print("              REGISTRANDO PACIENTE")
    print("=" * 50)

    nombre = input("Nombre completo: ")
    edad = input("Edad: ")
    fecha_nacimiento = input("Fecha de nacimiento (DD/MM/AA): ")

    print("\nGÉNERO")
    print("1. Masculino")
    print("2. Femenino")
    print("3. Otro")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        genero = "Masculino"
    elif opcion == "2":
        genero = "Femenino"
    else:
        genero = "Otro"

    print("\nTIPO DE DOCUMENTO")
    print("1. DNI")
    print("2. Carnet de Extranjería")
    print("3. Pasaporte")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        documento = "DNI"
    elif opcion == "2":
        documento = "Carnet de Extranjería"
    else:
        documento = "Pasaporte"

    numero = input("Número de documento: ")
    fecha_visita = input("Fecha de visita (DD/MM/AA): ")

    print("\nESTADO CIVIL")
    print("1. Soltero(a)")
    print("2. Casado(a)")
    print("3. Viudo(a)")
    print("4. Divorciado(a)")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        estado_civil = "Soltero(a)"
    elif opcion == "2":
        estado_civil = "Casado(a)"
    elif opcion == "3":
        estado_civil = "Viudo(a)"
    else:
        estado_civil = "Divorciado(a)"

    direccion = input("Dirección: ")

    print("\nTIPO DE SEGURO")
    print("1. EsSalud")
    print("2. SIS")
    print("3. Privado")
    print("4. Particular")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        seguro = "EsSalud"
    elif opcion == "2":
        seguro = "SIS"
    elif opcion == "3":
        seguro = "Privado"
    else:
        seguro = "Particular"

    print("\nESPECIALIDADES")
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
    else:
        especialidad = "Odontología"

    paciente = Paciente(
        nombre, edad, fecha_nacimiento, genero, documento,
        numero, fecha_visita, estado_civil, direccion,
        seguro, especialidad
    )

    print("\n¡PACIENTE REGISTRADO CORRECTAMENTE!")

    paciente.mostrar_datos()

    return paciente 