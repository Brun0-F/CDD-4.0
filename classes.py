class Pessoa():
    def __init__(self,nomeAluno,pesoAluno,idadeAluno,comando):
        self.nome = nomeAluno
        self.peso = pesoAluno
        self.idade = idadeAluno
        self.comando = comando
    def falar(self,falando):
        self.comando = 1
        print(f'{self.nome} está falando : {falando} ')
        if self.comando != 0 and self.comando != 1:
            print(f'{self.nome} não pode falar enquanto faz outra coisa ...')
    def pararDeFalar(self,calarBoca):
        self.comando = 0
        print(f'{self.nome} parou de falar finalmente!')
    def comer(self,alimento,bebida):
        self.comando = 2
        print(f'{self.nome} foi comer {alimento} e bebeu {bebida} ...')
        if self.comando != 0 and self.comando != 2:
            print(f'{self.nome} não pode comer enquanto faz outra coisa ...')
    def pararDeComer(self,parouDeComer):
        self.comando = 0
        print(f'{self.nome} parou de comer!')
    def dormir(self,dormir):
        self.comando = 3
        print(f'{self.nome} está dormindo...')
        if self.comando != 0 and self.comando != 3:
            print(f'{self.nome} não pode dormir enquanto faz outra coisa ...')
    def acordar(self,acordar):
        self.comando = 0
        print(f'{self.nome} acordou!')