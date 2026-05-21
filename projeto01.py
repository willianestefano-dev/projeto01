livros = []
funcionarios = {}

#---------------------------------------------------
#class professor------------------------------------
class Professor:
    def __init__(self, login, senha, nome, email):

        self.login = login
        self.senha = senha
        self.nome = nome
        self.email = email

#metodo senha

    def verificar_senha(self, login_senha):

        return self.senha == login_senha
    
#metodo to dict

    def to_dict(self):
        return {

            'login': self.login,
            'senha': self.senha,
            'nome': self.nome,
            'email': self.email
            
        }

#class aluno----------------------------------------

class Aluno:
    def __init__(self, nome, nota1, nota2, nota3):

        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

#metodo media

    def aluno_media(self):

        return (self.nota1 + self.nota2 + self.nota3) / 3
    
#metodo situacao
    
    def situacao_aluno(self):

        media = self.aluno_media()

        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperacao"
        else:
            return "Reprovado"
        
#metodo alterar notas

    def alterar_nota(self, n1, n2, n3):

        self.nota1 = n1
        self.nota2 = n2
        self.nota3 = n3

    def to_dict(self):
        return {

            'nome': self.nome,
            'nota1': self.nota1,
            'nota2': self.nota2,
            'nota3': self.nota3
        }

#carregamento prof------------------------------------

def carregamento_professor():
    try:
        with open("professor.txt", "r") as arquivo:
            lista = []
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    login, senha, nome, email = linha.split(",")
                    lista.append(Professor(login, senha, nome, email))

            return lista

    except FileNotFoundError:
        return []
    
#salvar professor--------------------------------------

def salvar_professor(lista):

    with open("professor.txt", "w") as arquivo:
        for professor in lista:
            arquivo.write(f"{professor.login},{professor.senha},{professor.nome},{professor.email}\n")

#carregamento aluno-------------------------------------

def carregamento_aluno():

    try:
        with open("aluno.txt", "r") as arquivo:
            lista = []
            for linha in arquivo:
                linha = linha.strip()
                if linha:
                    nome, nota1, nota2, nota3 = linha.split(",")
                    lista.append(Aluno(nome, float(nota1), float(nota2), float(nota3)))
            
            return lista
    
    except FileNotFoundError:
        return []
    
#salvar aluno---------------------------------------------

def salvar_aluno(lista):

    with open("aluno.txt", "w") as arquivo:
        for aluno in lista:
            arquivo.write(f"{aluno.nome},{aluno.nota1},{aluno.nota2},{aluno.nota3}\n")

#carregamento livros--------------------------------------

try:
    with open("livros.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                livro, quantidade = linha.split(",")
                livros.append([livro, quantidade])
        
except FileNotFoundError:
    print("Carregando livros em estoque.......")

#salvar livros---------------------------------------------

def salvar_livros():

    with open("livros.txt", "w") as arquivo:
        for livro in livros:            
            arquivo.write(f"{livro[0]},{livro[1]}\n")

#carremanto funcionarios--------------------------------------

try: 
    with open("funcionarios.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                nome , senha, funcao = linha.split(",")
                funcionarios[nome] = {'senha': senha, 'funcao': funcao}

except FileNotFoundError:
    print("Carregando funcionarios.........")

#salvar funcionarios-------------------------------------------

def salvar_funcionarios():

    with open("funcionarios.txt", "w") as arquivo:
        for nome, dados in funcionarios.items():
            arquivo.write(f"{nome},{dados['senha']},{dados['funcao']}\n")            

#--------------------------------------------------------
#validação login ----------------------------------------

def validar_login(login):

    if not login.strip():
        return "Campo nome vazio"
    
    if not login.isalpha():
        return "Apenas letras"
    
    for professor in lista:
        if professor.login != login:
            return "professor não cadastrado"
    
    return "ok"

#validação login senha

def validar_senha(senha):

    if not senha.strip():
        return "Campo senha vazio"
    
    if not senha.isdigit():
        return "Apenas numeros"
    
    return "ok"

#----------------------------------------------------------
#validar cadastro de professores login---------------------

def validar_cadastro_login(login):

    if not login.strip():
        return "Campo nome vazio"
    
    if not login.isalpha():
        return "Apenas letras"
    
    return "ok"

#validar senha

def validar_cadastro_senha(senha):

    if not senha.strip():
        return "Campo senha vazio"
    
    if not senha.isdigit():
        return "Apenas numeros"
    
    return "ok"

#validar nome

def validar_cadastro_nome(nome):

    if not nome.strip():
        return "campo vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar email

def validar_cadastro_email(email):

    if "@" not in email or ".com" not in email:
        return "Email invalido"
    
    return "ok"
    
#-----------------------------------------------------------------
#validação alterar dados professor login--------------------------

def validar_alterar_login(novo_login):

    if not novo_login.strip():
        return "Campo nome vazio"
    
    if not novo_login.isalpha():
        return "Apenas letras"
    
    return "ok"

#validar senha

def validar_alterar_senha(nova_senha):

    if not nova_senha.strip():
        return "Campo senha vazio"
    
    if not nova_senha.isdigit():
        return "Apenas numeros"
    
    return "ok"

#validar nome

def validar_alterar_nome(novo_nome):

    if not novo_nome.strip():
        return "campo vazio"
    
    if not novo_nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar email

def validar_alterar_email(novo_email):

    if "@" not in novo_email or ".com" not in novo_email:
        return "Email invalido"
    
#-----------------------------------------------------------------
#validação aluno nome---------------------------------------------

def validar_aluno_nome(nome):

    if not nome.strip():
        return "campo vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#---------------------------------------------------------------
#validar livros-----------------------------

def validar_livros_nome(livro):

    if not livro.strip():
        return "Campo livro vazio"
    
    if not livro.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar livros quantidade

def validar_livros_quantidade(quantidade):

    if not quantidade.strip():
        return "Campo quantidade vazio"
    
    if not quantidade.isdigit():
        return "Apenas numeros"
    
    return "ok"

#cadastro

def adicionar_livro(livros, livro, quantidade):

    for item in livros:
        if item[0] == livro:
            return False
    
    livros.append([livro, quantidade])
    salvar_livros()
    return True   

  

#remover livros--------------------------------------------------

def remover_livro(livros, livro):

    for item in livros:
        if item[0] == livro:
            livros.remove(item)
            salvar_livros()
            return "livro_removido"
    return "livro_nao_existe"
    
#verificar livros ------------------------------------------------

def verificar_livros(livros):

    return livros   

#------------------------------------------------------------------
#funcionarios - Dicionario-----------------------------------------

#validar nome

def validar_login_nome(nome):

    if not nome.strip():
        return "Campos nome vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas letras"
    
    return "ok"

#validar senha

def validar_login_senha(senha):

    if not senha.strip():
        return "Campo senha vazio"
    
    if not senha.isdigit():
        return "Apenas numeros"
    
    return "ok"

#login

def login_funcionarios(funcionarios, nome, senha):

    if nome in funcionarios and funcionarios[nome]['senha'] == senha:        
        return True
    return False

#validar cadastro nome--------------------------------------------

def validar_cadastro_nome(nome):

    if not nome.strip():
        return "Campo cadastro vazio"
    
    if not nome.replace(" ","").isalpha():
        return "Apenas nomes"
    
    return "ok"

#validar cadastro senha

def validar_cadastro_senha(senha):

    if not senha.strip():
        return "Campo senha vazio"
    
    if not senha.isdigit():
        return "Apenas numeros"
    
    return "ok"

#velidar cadastro funcao

def validar_cadastro_funcao(funcao):

    if not funcao.strip():
        return "Campo cadastro vazio"
    
    if not funcao.replace(" ","").isalpha():
        return "Apenas nomes"
    
    return "ok"

#cadastro funcionarios

def cadastro_funcionarios(funcionarios, nome, senha, funcao):

    if nome not in funcionarios:
        funcionarios[nome] = {'senha': senha, 'funcao': funcao}
        salvar_funcionarios()
        return True
    return False

#lista de funcionarios--------------------------------------------

def lista_funcionarios(funcionarios):

    return list(funcionarios.keys())

#remover funcionarios---------------------------------------------

def remover_funcionarios(funcionarios, nome):

    if nome in funcionarios:
        del funcionarios[nome]
        salvar_funcionarios()
        return True
    return False

#menu--------------------------------------------------------------

while True:

    print("\n-----------Menu-----------")
    print("-------Professores--------")
    print("1 - Login")
    print("2 - Cadastro professor")
    print("3 - Alterar dados do professor")
    print("4 - Remover professor")
    print("5 - Verificar lista de professores")
    print()
    print("------- Menu alunos-------")
    print("6 - Cadastro alunos")
    print("7 - Verficar lista de alunos")
    print("8 - Buscar aluno")
    print("9 - Aprovados")
    print("10 - Reprovados - Recuperação")
    print("11 - Remover aluno")
    print()
    print("-------Menu livros---------")
    print("12 - Adicionar livros")
    print("13 - Remover livros")
    print("14 - Verificar estoque de livros")
    print()
    print("-------Menu funcionarios--------")
    print("15 - Login funcionarios")
    print("16 - Cadastro funcionarios")
    print("17 - Lista de funcionarios")
    print("18 - Remover funcionarios")
    print("19 - Sair")

    opcao = input("Digite sua escolha: ")

#--------------------------------------------------------------------------
#login professor-----------------------------------------------------------

    if opcao == "1":

        lista = carregamento_professor()
        #validar ---------------------------
        login = input("Digite seu login: ")
        validar = validar_login(login)
        if validar != "ok":
            print(validar)
            continue

        #validar----------------------------    
        senha = input("Digite sua senha: ")
        validar = validar_senha(senha)
        if validar != "ok":
            print(validar)
            continue

        #login------------------------------
        for professor in lista:
            if professor.login == login and professor.verificar_senha(senha):
                print("Login correto")
                break
        else:
            print("Login ou senha incorreto, Tente novamente")

#----------------------------------------------------------------------
#cadastro--------------------------------------------------------------

    elif opcao == "2":
        #validar----------------------------
        login = input("Digite seu login: ")
        validar = validar_cadastro_login(login)
        if validar != "ok":
            print(validar)
            continue

        #validar----------------------------
        senha = input("Digite sua senha: ")
        validar = validar_cadastro_senha(senha)
        if validar != "ok":
            print(validar)
            continue

        #validar-----------------------------
        nome = input("Digite seu nome: ")
        validar = validar_cadastro_nome(nome)
        if validar != "ok":
            print(validar)
            continue

        #validar-----------------------------
        email = input("Digite seu email ")
        validar = validar_cadastro_email(email)
        if validar != "ok":
            print(validar)
            continue

        #cadastro----------------------------
        professor = Professor(login, senha, nome, email)

        lista = carregamento_professor()

        lista.append(professor)
        salvar_professor(lista)
        print("Professor cadastrada")

#------------------------------------------------------------------
#alterar dados-----------------------------------------------------

    elif opcao == "3":

        lista = carregamento_professor()
        encontrou = False

        login = input("Digite seu login: ").lower()

        for professor in lista:
            if professor.login == login:
                encontrou = True
                print(f"Login: {professor.login} - Senha: {professor.senha} - Nome: {professor.nome} - Email: {professor.email}")

                confirmar = input("Realmente deseja alterar suas informações? (s/n): ").lower()
                
                if confirmar == "s":
                    alterar = input("Qual informação gostaria de alterar? Login(l) - Senha(s) - Nome(n) - Email(e)").lower()
                    #alterar login---------------------------------------
                    if alterar == "l":
                        confirmar = input("Realmente gostaria de alterar seu login? (s/n): ").lower()
                        if confirmar == "s":
                            #validar------------------------------------------
                            novo_login = input("Digite seu novo login: ").lower()
                            validar = validar_alterar_login(novo_login)
                            if validar != "ok":
                                print(validar)
                            #--------------------------------------------------
                            professor.login = novo_login
                            salvar_professor(lista)
                            print("Login alterado")
                            break
                        else:
                            print("Alterar login cancelado")
                    
                    #alterar senha-------------------------------------
                    elif alterar == "s":
                        confirmar = input("Realmente deseja alterar sua senha? (s/n): ").lower()
                        if confirmar == "s":
                            #validar-----------------------------------
                            nova_senha = input("Digite sua nova senha: ")
                            validar = validar_alterar_senha(nova_senha)
                            if validar != "ok":
                                print(validar)
                            #validar-----------------------------------
                            professor.senha = nova_senha
                            salvar_professor(lista)
                            print("Senha alterada")
                            break
                        else:
                            print("Alterar senha cancelado")

                    #alterar nome---------------------------------------
                    elif alterar == "n":
                        confirmar == input("Realmente deseja alterar seu nome? (s/n): ").lower()
                        if confirmar == "s":
                            #validar------------------------------------
                            novo_nome = input("Digite seu novo nome: ").lower()
                            validar = validar_alterar_nome(novo_nome)
                            if validar != "ok":
                                print(validar)
                            #-------------------------------------------
                            professor.nome = novo_nome
                            salvar_professor(lista)
                            print("Nome alterado")
                            break
                        else:
                            print("Aletar nome alterado")

                    #alterar email---------------------------------------
                    elif alterar == "e":
                        confirmar == input("Realmente deseja alterar seu email? (s/n): ").lower()
                        if confirmar == "s":
                            #validar-------------------------------------
                            novo_email = input("Digite seu novo email: ")
                            validar = validar_alterar_email(novo_email)
                            if validar != "ok":
                                print(validar)
                            #--------------------------------------------
                            professor.email = novo_email
                            salvar_professor(lista)
                            print("Email alterado")
                            break
                        else:
                            print("Aletar email cancelado")
        if not encontrou:
            print("Professor não cadastrado")    
            
#remover professor-------------------------------------------------

    elif opcao == "4":

        lista = carregamento_professor()
        encontrou = False

        login = input("Digite seu login: ").lower()
        if login.isalpha():

            for professor in lista:
                if professor.login == login:
                    encontrou = True

                    print(f"Login: {professor.login} - Nome: {professor.nome}")
                    confirmar = input("Realmente gostaria de remover este professor? (s/n): ").lower()

                    if confirmar == "s":
                        lista.remove(professor)
                        salvar_professor(lista)
                        print("Professor removido")
                        break
                    else:
                        print("Remover professor cancelado")

            if not encontrou:
                print("Professor não cadastrado")
        else:
            print("Apenas letras")

#lista de professores-----------------------------------------------

    elif opcao == "5":

        lista = carregamento_professor()        

        buscar = input("Lista completa (c) ou Pelo nome (n): ").lower()
        if buscar.isalpha():

            if buscar == "c":
                for professor in lista:
                    print(f"Login: {professor.login} - Senha: {professor.senha} - Nome: {professor.nome} - Email: {professor.email}")
                    
            elif buscar == "n":
                nome = input("Digite o nome do professor: ").lower()
                if nome.isalpha():         
                    for professor in lista:
                        if professor.nome == nome:                    
                            print(f"Login: {professor.login} - Senha: {professor.senha} - Nome: {professor.nome} - Email: {professor.email}")
                            break
                    else:   
                        print("Professor não cadastrado")
                else:
                    print("Apenas nomes")
        else:
            print("Apenas letras")

#--------------------------------------------------------------------
#cadastro aluno------------------------------------------------------

    elif opcao == "6":
        #validar-----------------------------------
        nome = input("Digite o nome do aluno: ")
        validar = validar_aluno_nome(nome)
        if validar != "ok":
            print(validar)
            continue

        #validar nota1------------------------------
        nota1 = float(input("Digite a primeira nota: "))  

        if nota1 < 0 or nota1 > 10:
            print("Nota invalida, cadastro cancelado")
            continue
        #validar nota2
        nota2 = float(input("Digite a segunda nota: "))

        if nota2 < 0 or nota2 > 10:
            print("Nota invalida, cadastro cancelado")
            continue
        #validar nota3
        nota3 = float(input("Digite sua terceira nota: "))

        if nota3 < 0 or nota3 > 10:
            print("Nota invalida, cadastro cancelado")
            continue
        #cadastro
        aluno = Aluno(nome, nota1, nota2, nota3)

        lista = carregamento_aluno()
        lista.append(aluno)
        salvar_aluno(lista)
        print("Aluno cadastrado")

#lista de alunos-----------------------------------------------------

    elif opcao == "7":

        lista = carregamento_aluno()

        if not lista:
            print("Lista de alunos vazia")
        else:
            for aluno in lista:
                print(f"Nome: {aluno.nome} - Nota: {aluno.nota1} - Nota: {aluno.nota2} - Nota: {aluno.nota3} - Media: {aluno.aluno_media():.1f} - Situação: {aluno.situacao_aluno()}")

#buscar alunos-----------------------------------------------------

    elif opcao == "8":       

        lista = carregamento_aluno()
        encontrou = False

        nome = input("Digite o aluno que deseja buscar: ").lower()
        if nome.isalpha():

            for aluno in lista:
                if aluno.nome == nome:
                    encontrou = True
                    print(f"Nome: {aluno.nome} - Media: {aluno.aluno_media():.1f} - Situação: {aluno.situacao_aluno()}")
            
            if not encontrou:
                print("Aluno não cadastrado")
        else:
            print("Apenas nomes")

#alunos aprovado----------------------------------------------------

    elif opcao == "9":

        lista = carregamento_aluno()

        if not lista:
            print("Lista de alunos vazia")
        else:
            for aluno in lista:
                if aluno.situacao_aluno() == "Aprovado":
                    print(f"Nome: {aluno.nome} - Media: {aluno.aluno_media():.1f} - Situação: {aluno.situacao_aluno()}")

#reprovados / recuperacao------------------------------------------
    
    elif opcao == "10":

        lista = carregamento_aluno()

        if not lista:
            print("Lista de alunos vazia")
        else:
            for aluno in lista:
                if aluno.situacao_aluno() == "Reprovado" or aluno.situacao_aluno() == "Recuperacao":
                    print(f"Nome: {aluno.nome} - Media: {aluno.aluno_media():.1f} - Situação: {aluno.situacao_aluno()}")

#remover aluno----------------------------------------------------

    elif opcao == "11":

        lista = carregamento_aluno()
        encontrou = False
        nome = input("Digite o nome do aluno que deseja remover: ").lower()
        if nome.isalpha():

            for aluno in lista:
                if aluno.nome == nome:
                    encontrou = True

                    print(f"Nome: {aluno.nome} - Media: {aluno.aluno_media():.1f} - Situação: {aluno.situacao_aluno()}")

                    confirmar = input("Realmente deseja remover este aluno? (s/n): ").lower()

                    if confirmar == "s":
                        lista.remove(aluno)
                        salvar_aluno(lista)
                        print("Aluno removido")
                        break
                    else:
                        print("Remover aluno cancelado")

            if not encontrou:
                print("Aluno não cadastrado")
        else:
            print("Apenas nomes")

#------------------------------------------------------------------
#adicionar livros--------------------------------------------------

    elif opcao == "12":
        #validar---------------------------------------------
        livro = input("Digite o livro que deseja adicionar: ").lower()
        validar = validar_livros_nome(livro)
        if validar != "ok":
            print(validar)
            continue

        #validar---------------------------------------------
        quantidade = input("Digite a quantidade: ")
        validar = validar_livros_quantidade(quantidade)
        if validar != "ok":
            print(validar)
            continue

        if adicionar_livro(livros, livro, quantidade):
            print("Livro adicionado")
        else:
            print("Livro já existe")

#remover livros----------------------------------------------------

    elif opcao == "13":

        livro = input("Digite o livro que deseja remover: ").lower()
        if livro.replace(" ","").isalpha():

            confirmar = input("Realmente deseja remover este livro? (s/n): ").lower()

            if confirmar == "s":
                remover = remover_livro(livros, livro)

                if remover == "livro_removido":
                    print("Livro removido")
                    break

                elif remover == "livro_nao_existe":
                    print("Livro não existe")
            
            else:
                print("Remover livro cancelado")
        else:
            print("Apenas letras")

#verificar livros---------------------------------------------------

    elif opcao == "14":

        verificar = verificar_livros(livros)

        if not verificar:
            print("Lista de livros vazia")
        else:
            for l in verificar:
                print(f"Nome: {l[0]} - Quantidade: {l[1]}")

#--------------------------------------------------------------------
#login funcionariosr-------------------------------------------------

    elif opcao == "15":
        #validar----------------------------------
        nome = input("Digite seu nome: ").lower()
        validar = validar_login_nome(nome)
        if validar != "ok":
            print(validar)
            continue

        #validar----------------------------------
        senha = input("Digite sua senha: ")
        validar = validar_login_senha(senha)
        if validar != "ok":
            print(validar)
            continue

        if login_funcionarios(funcionarios, nome, senha):
            print("Login correto")
        else:
            print("Login ou senha incorreto, tente novamente")

#cadastro funcionarios-----------------------------------------------

    elif opcao == "16":
        #validar----------------------------------
        nome = input("Digite seu nome: ").lower()
        validar = validar_cadastro_nome(nome)
        if validar != "ok":
            print(validar)
            continue

        #validar----------------------------------
        senha = input("Digite sua senha: ")
        validar = validar_cadastro_senha(senha)
        if validar != "ok":
            print(validar)
            continue

        #validar----------------------------------        
        funcao = input("Digite sua função: ").lower()
        validar = validar_cadastro_funcao(funcao)
        if validar != "ok":
            print(validar)
            continue
        
        if cadastro_funcionarios(funcionarios, nome, senha, funcao):
            print("Funcionario cadastrado")
        else:
            print("Funcionario já existe")

#lista de funcionarios-----------------------------------------------

    elif opcao == "17":

        lista = lista_funcionarios(funcionarios)

        if not lista:
            print("Lista de funcionarios vazia")
        else:
            for f in lista:
                print(f"Nome: " + f + " - Função: " + funcionarios[f]['funcao'])

#remover funcionarios-------------------------------------------------

    elif opcao == "18":

        nome = input("Remover funcionario: ").lower()
        if nome.replace(" ","").isalpha():

            confirmar = input("Relamente deseja remover este funcionario? (s/n): ").lower()

            if confirmar == "s":
                if remover_funcionarios(funcionarios, nome):
                    print("Funcionario removido")
                else:
                    print("Funcionario não cadastrado")

            else:
                print("Remover funcionario cancelado")
        else:
            print("Apenas letras")

#sair------------------------------------------------------------------

    elif opcao == "19":
        print("Sair do sistema.........")
        break







        
            
            














                            




    
    
    

