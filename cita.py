class Cita:

    def __init__(self, codigo, paciente, medico, fecha, hora, motivo, estado):

        self._codigo = codigo
        self._paciente = paciente
        self._medico = medico
        self._fecha = fecha
        self._hora = hora
        self._motivo = motivo
        self._estado = estado

    # GETTERS

    def get_codigo(self):
        return self._codigo

    def get_paciente(self):
        return self._paciente

    def get_medico(self):
        return self._medico

    def get_fecha(self):
        return self._fecha

    def get_hora(self):
        return self._hora

    def get_motivo(self):
        return self._motivo

    def get_estado(self):
        return self._estado

    # SETTERS

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_paciente(self, paciente):
        self._paciente = paciente

    def set_medico(self, medico):
        self._medico = medico

    def set_fecha(self, fecha):
        self._fecha = fecha

    def set_hora(self, hora):
        self._hora = hora

    def set_motivo(self, motivo):
        self._motivo = motivo

    def set_estado(self, estado):
        self._estado = estado

    def mostrar_datos(self):

        print("\n" + "=" * 50)
        print("                 DATOS DE LA CITA")
        print("=" * 50)

        print("Código:", self.get_codigo())
        print("Paciente:", self.get_paciente().get_nombre())
        print("Documento:", self.get_paciente().get_numero())
        print("Médico:", self.get_medico().get_nombre())
        print("Especialidad:", self.get_medico().get_especialidad())
        print("Fecha:", self.get_fecha())
        print("Hora:", self.get_hora())
        print("Motivo:", self.get_motivo())
        print("Estado:", self.get_estado())

        print("=" * 50)


def registrar_cita(pacientes, medicos):

    print("\n" + "=" * 50)
    print("                REGISTRANDO CITA")
    print("=" * 50)

    codigo = input("Código de la cita: ")

    print("\nPACIENTES REGISTRADOS")

    if len(pacientes) == 0:
        print("No existen pacientes registrados.")
        return None

    for paciente in pacientes:
        print(
            paciente.get_numero(),
            "-",
            paciente.get_nombre()
        )

    numero = input("\nIngrese el número de documento del paciente: ")

    paciente_encontrado = None

    for paciente in pacientes:
        if paciente.get_numero() == numero:
            paciente_encontrado = paciente
            break

    if paciente_encontrado is None:
        print("Paciente no encontrado.")
        return None

    print("\nMÉDICOS REGISTRADOS")

    if len(medicos) == 0:
        print("No existen médicos registrados.")
        return None

    for medico in medicos:
        print(
            medico.get_codigo(),
            "-",
            medico.get_nombre(),
            "-",
            medico.get_especialidad()
        )

    codigo_medico = input("\nIngrese el código del médico: ")

    medico_encontrado = None

    for medico in medicos:
        if medico.get_codigo() == codigo_medico:
            medico_encontrado = medico
            break

    if medico_encontrado is None:
        print("Médico no encontrado.")
        return None

    fecha = input("Fecha de la cita (DD/MM/AA): ")
    hora = input("Hora de la cita: ")
    motivo = input("Motivo de la cita: ")

    print("\nESTADO DE LA CITA")
    print("1. Pendiente")
    print("2. Confirmada")
    print("3. Atendida")
    print("4. Cancelada")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        estado = "Pendiente"
    elif opcion == "2":
        estado = "Confirmada"
    elif opcion == "3":
        estado = "Atendida"
    else:
        estado = "Cancelada"

    cita = Cita(
        codigo,
        paciente_encontrado,
        medico_encontrado,
        fecha,
        hora,
        motivo,
        estado
    )

    print("\n¡CITA REGISTRADA CORRECTAMENTE!")

    cita.mostrar_datos()

    return cita