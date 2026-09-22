class Atencion:

    def __init__(self, codigo, cita, diagnostico, tratamiento,
                 observaciones, medicamentos):

        self._codigo = codigo
        self._cita = cita
        self._diagnostico = diagnostico
        self._tratamiento = tratamiento
        self._observaciones = observaciones
        self._medicamentos = medicamentos

    # GETTERS

    def get_codigo(self):
        return self._codigo

    def get_cita(self):
        return self._cita

    def get_diagnostico(self):
        return self._diagnostico

    def get_tratamiento(self):
        return self._tratamiento

    def get_observaciones(self):
        return self._observaciones

    def get_medicamentos(self):
        return self._medicamentos

    # SETTERS

    def set_codigo(self, codigo):
        self._codigo = codigo

    def set_cita(self, cita):
        self._cita = cita

    def set_diagnostico(self, diagnostico):
        self._diagnostico = diagnostico

    def set_tratamiento(self, tratamiento):
        self._tratamiento = tratamiento

    def set_observaciones(self, observaciones):
        self._observaciones = observaciones

    def set_medicamentos(self, medicamentos):
        self._medicamentos = medicamentos

    def mostrar_datos(self):

        print("\n" + "=" * 50)
        print("              DATOS DE LA ATENCIÓN")
        print("=" * 50)

        print("Código de atención:", self.get_codigo())
        print("Código de cita:", self.get_cita().get_codigo())
        print("Paciente:", self.get_cita().get_paciente().get_nombre())
        print("Médico:", self.get_cita().get_medico().get_nombre())
        print("Especialidad:",
              self.get_cita().get_medico().get_especialidad())
        print("Fecha:", self.get_cita().get_fecha())
        print("Diagnóstico:", self.get_diagnostico())
        print("Tratamiento:", self.get_tratamiento())
        print("Observaciones:", self.get_observaciones())
        print("Medicamentos:", self.get_medicamentos())

        print("=" * 50)


def registrar_atencion(citas):

    print("\n" + "=" * 50)
    print("              REGISTRANDO ATENCIÓN")
    print("=" * 50)

    if len(citas) == 0:
        print("No existen citas registradas.")
        return None

    print("\nCITAS DISPONIBLES")

    for cita in citas:
        print(
            cita.get_codigo(),
            "-",
            cita.get_paciente().get_nombre(),
            "-",
            cita.get_fecha()
        )

    codigo_cita = input("\nIngrese el código de la cita: ")

    cita_encontrada = None

    for cita in citas:
        if cita.get_codigo() == codigo_cita:
            cita_encontrada = cita
            break

    if cita_encontrada is None:
        print("Cita no encontrada.")
        return None

    codigo = input("Código de atención: ")
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")
    observaciones = input("Observaciones: ")
    medicamentos = input("Medicamentos indicados: ")

    atencion = Atencion(
        codigo,
        cita_encontrada,
        diagnostico,
        tratamiento,
        observaciones,
        medicamentos
    )

    print("\n¡ATENCIÓN REGISTRADA CORRECTAMENTE!")

    atencion.mostrar_datos()

    return atencion