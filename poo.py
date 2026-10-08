class estudantes: 
    def estudantes(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def media(self):
        return (self.nota1 + self.nota2) / 2
    def situacao(self):
        if self.media() >= 6:
            return "Aprovado"
        elif self.media() >= 4:
            return "Recuperação"
        else:
            return "Reprovado"
    def descrever(self):
        return f"{self.nome:<16}{self.nota1:<7}{self.nota2:<7}{self.media():<8.1f}{self.situacao():<14}"
        
    def cadastrar_usuario():

        nome = input("Nome do estudante: ")
        nota1 = float(input("Nota 1: "))
        nota2 = float(input("Nota 2: "))
        estudantes.append(estudantes(nome, nota1, nota2))
        print("Estudante cadastrado")

    def listar():
        if len(estudantes) == 0:
            print("Nenhum estudante cadastrado.")
            return
        print(f"\n{'Nome':<16}{'Nota 1':<7}{'Nota 2':<7}{'Média':<8}{'Situação':<14}")

        for estudante in estudantes:
            print(estudante.descrever())    

   