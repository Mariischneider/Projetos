class Policial:
    def __init__(self, nome, matricula, cargo):
        self.nome = nome
        self.matricula = matricula
        self.cargo = cargo
        self.viatura = None

    def trabalha_em(self, viatura):
        self.viatura = viatura

    def __str__(self):
        return f"Policial {self.nome} ({self.matricula}) - {self.cargo}"

class Ocorrencia:
    def __init__(self, id, data, local, descricao):
        self.id = id
        self.data = data
        self.local = local
        self.descricao = descricao
        self.policiais_envolvidos = []

    def envolve(self, policial):
        self.policiais_envolvidos.append(policial)

    def __str__(self):
        return f"Ocorrência {self.id} - {self.data} - {self.local} - {self.descricao}"

class Viatura:
    def __init__(self, placa, modelo, ano):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.policiais = []

    def tem(self, policial):
        self.policiais.append(policial)

    def __str__(self):
        return f"Viatura {self.placa} - {self.modelo} - {self.ano}"

class Prisao:
    def __init__(self, id, data, local, descricao, ocorrencia):
        self.id = id
        self.data = data
        self.local = local
        self.descricao = descricao
        self.ocorrencia = ocorrencia

    def __str__(self):
        return f"Prisão {self.id} - {self.data} - {self.local} - {self.descricao} - Ocorrência {self.ocorrencia.id}"

# Exemplo:
policial1 = Policial("João", "1234", "Inspetor")
policial2 = Policial("Maria", "5678", "Agente")

viatura1 = Viatura("ABC-1234", "Ford", 2015)
viatura1.tem(policial1)

ocorrencia1 = Ocorrencia(1, "2022-01-01", "Rua 1", "Furto")
ocorrencia1.envolve(policial1)
ocorrencia1.envolve(policial2)

prisao1 = Prisao(1, "2022-01-02", "Rua 2", "Prisão em flagrante", ocorrencia1)

print(policial1)
print(viatura1)
print(ocorrencia1)
print(prisao1)
