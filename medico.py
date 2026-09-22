class Medico:

    def __init__(self, codigo, nombre, documento, numero, telefono,
                 correo, especialidad, cmp, consultorio):

        self._codigo = codigo
        self._nombre = nombre
        self._documento = documento
        self._numero = numero
        self._telefono = telefono
        self._correo = correo
        self._especialidad = especialidad
        self._cmp = cmp
        self._consultorio = consultorio

    # GETTERS

    def get_codigo(self):
        return self._codigo

    def get_nombre(self):
        return self._nombre

    def get_documento(self):
        return self._documento

    def get_numero(self):
        return self._numero

    def get_telefono(self):
        return self._telefono

    def get_correo(self):
        return self._correo

    def get_especialidad(self):
        return self._especialidad

    def get_cmp(self):
        return self._cmp

    def get_consultorio(self):
        return self._consultorio

    # SETTERS

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_documento(self, documento):
        self._documento = documento

    def set_numero(self, numero):
        self._numero = numero

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_correo(self, correo):
        self._correo = correo

    def set_especialidad(self, especialidad):
        self._especialidad = especialidad

    def set_cmp(self, cmp):
        self._cmp = cmp

    def set_consultorio(self, consultorio):
        self._consultorio = consultorio

    def mostrar_datos(self):

        print("\n" + "=" * 50)
        print("                DATOS DEL MÉDICO")
        print("=" * 50)

        print("Código:", self.get_codigo())
        print("Nombre:", self.get_nombre())
        print("Documento:", self.get_documento())
        print("Número:", self.get_numero())
        print("Teléfono:", self.get_telefono())
        print("Correo:", self.get_correo())
        print("Especialidad:", self.get_especialidad())
        print("CMP:", self.get_cmp())
        print("Consultorio:", self.get_consultorio())

        print("=" * 50)


def registrar_medico():

    print("\n" + "=" * 50)
    print("                REGISTRANDO MÉDICO")
    print("=" * 50)

    codigo = input("Código del médico: ")
    nombre = input("Nombre completo: ")

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
    telefono = input("Teléfono: ")
    correo = input("Correo: ")

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

    cmp = input("CMP: ")
    consultorio = input("Consultorio: ")

    medico = Medico(
        codigo, nombre, documento, numero, telefono,
        correo, especialidad, cmp, consultorio
    )

    print("\n¡MÉDICO REGISTRADO CORRECTAMENTE!")

    medico.mostrar_datos()

    return medico