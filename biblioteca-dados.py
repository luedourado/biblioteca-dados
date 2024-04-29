class Livro:
    def __init__(self, titulo, autor, ano_pub, num_copias):
        #Atribui valores à classe Livros
        self.titulo = titulo
        self.autor = autor
        self.ano_pub = ano_pub
        self.num_copias = num_copias

    def emprestar(self):
        #Empresta um livro
        if self.num_copias > 0:
            self.num_copias -= 1
            return True
        else:
            return False

    def devolver(self):
        #Devolve um livro
        self.num_copias += 1


class Usuario:
    def __init__(self, nome, identificacao, contato):
        #Atribui valores à classe Usuários
        self.nome = nome
        self.identificacao = identificacao
        self.contato = contato


class Biblioteca:
    def __init__(self):
        #Biblioteca com listas vazias de livros e usuários
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        #Adiciona um livro
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        #Adiciona um usuário
        self.usuarios.append(usuario)

    def emprestar_livro(self, titulo_livro, usuario):
        #Empresta um livro para um usuário específico e cadastrado
        for livro in self.livros:
            if livro.titulo == titulo_livro:
                if livro.emprestar():
                    print(f"Livro '{titulo_livro}' emprestado para {usuario.nome}.")
                    return
                else:
                    print(f"Desculpe, o livro '{titulo_livro}' não está disponível para empréstimo.")
                    return
        print("Livro não encontrado.")

    def devolver_livro(self, titulo_livro):
        #Devolve um livro
        for livro in self.livros:
            if livro.titulo == titulo_livro:
                livro.devolver()
                print(f"Livro '{titulo_livro}' devolvido com sucesso.")
                return
        print("Livro não encontrado.")

    def consultar_livros(self, termo):
        #Consulta os livros por título, autor ou ano de publicação
        encontrados = False
        for livro in self.livros:
            if termo.lower() in livro.titulo.lower() or termo.lower() in livro.autor.lower() or str(livro.ano_pub) == termo:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de publicação: {livro.ano_pub}, Cópias disponíveis: {livro.num_copias}")
                encontrados = True
        if not encontrados:
            print("Nenhum livro encontrado.")

    def gerar_relatorio(self):
        #Gera um relatório da biblioteca mostrando os livros disponíveis e os usuários cadastrados
        print("===== Relatório da Biblioteca =====")
        print("Livros Disponíveis:")
        for livro in self.livros:
            print(f"Título: {livro.titulo}, Autor: {livro.autor}, Ano de publicação: {livro.ano_pub}, Cópias disponíveis: {livro.num_copias}")

        print("Usuários Cadastrados:")
        for usuario in self.usuarios:
            print(f"Nome: {usuario.nome}, Identificação: {usuario.identificacao}, Contato: {usuario.contato}")


#Interface do menu
def menu():
    # Exibe o menu de opções
    print("\n===== Menu =====")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Consultar livros")
    print("6. Gerar relatório")
    print("0. Sair")


biblioteca = Biblioteca()

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        #Cadastra um novo livro na biblioteca
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação do livro: "))
        copias = int(input("Digite o número de cópias disponíveis: "))
        livro = Livro(titulo, autor, ano, copias)
        biblioteca.cadastrar_livro(livro)
        print("\nLivro cadastrado com sucesso.")

    elif opcao == "2":
        #Cadastra um novo usuário na biblioteca
        nome = input("Digite o nome do usuário: ")
        identificacao = input("Digite o número de identificação do usuário: ")
        contato = input("Digite o contato do usuário: ")
        usuario = Usuario(nome, identificacao, contato)
        biblioteca.cadastrar_usuario(usuario)
        print("\nUsuário cadastrado com sucesso.")

    elif opcao == "3":
        #Empresta um livro para um usuário
        titulo = input("Digite o título do livro que deseja emprestar: ")
        usuario_nome = input("Digite o nome do usuário: ")
        usuario = next((u for u in biblioteca.usuarios if u.nome == usuario_nome), None)
        if usuario:
            biblioteca.emprestar_livro(titulo, usuario)
        else:
            print("Usuário não encontrado.")

    elif opcao == "4":
        #Devolve um livro à biblioteca
        titulo = input("Digite o título do livro que deseja devolver: ")
        biblioteca.devolver_livro(titulo)

    elif opcao == "5":
        #Consulta livros por título, autor ou ano de publicação
        termo = input("Digite o título, autor ou ano de publicação do livro que deseja consultar: ")
        biblioteca.consultar_livros(termo)

    elif opcao == "6":
        #Gera um relatório da biblioteca
        biblioteca.gerar_relatorio()

    elif opcao == "0":
        #Opção para ebcerrar o programa
        print("Encerrando o programa.")
        break

    else:
        #Mensagem de erro para opção inválida
        print("Opção inválida. Por favor, escolha uma opção válida.")
