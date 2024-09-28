from abc import ABC, abstractmethod
from datetime import date,datetime
from time import strftime


class Transacao(ABC):
    
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self,conta:Conta):
        pass
    
    
class Cliente:
    def __init__(self,endereco:str):
        self._endereco = endereco
        self.contas = []
        
    def realizar_transacao(self,conta:Conta,transacao:Transacao):
        transacao.registrar(transacao)
      
    
    def adicionar_conta(self,conta:Conta):
        self.contas.append(conta)
         
    
class PessoaFisica(Cliente):
    def __init__(self, endereco:str, conta:str, cpf:str, nome:str, data_nascimento:date):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        
        
class Conta:
    def __init__(self, numero:int, cliente:Cliente) :
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()
        
    @classmethod    
    def nova_conta(cls,cliente:Cliente, numero:int) -> Cliente:
        return cls(numero,cliente)
    
    @property
    def saldo(self):
       return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
  
    
    def sacar(self,valor:float) -> bool:
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        
        if excedeu_saldo:
            print("\n@@@ Operação falhou voce nao tem saldo suficiente. @@@")
            
        elif valor > 0:
            self.saldo -= valor
            print('\n### Saque realizado com sucesso!! ####')
            return True
        
        else:
            print("\n@@@ Operação falhou ou o valor informado é invalido. @@@")   
            
        return False
    
    def depositar(self,valor:float) -> bool:
        if valor > 0:
            self.saldo += valor
            print("\n### Deposito realizado com sucesso!! ###")
        else:
            print("\n@@@ Operação Falhou o valor informado é invalido @@@ ")
            return False
        
        return True


class ContaCorrente(Conta):
    def __init__(self, numero: int, cliente: Cliente, limite=500, limite_saques=3):
        super().__init__( numero,  cliente)
        self.limite = limite
        self.limite_saque = limite_saques
        

    def sacar(self, valor: float) :
        numero_de_saques = len(
            [transacoes for trnsacoes in self.historico.transacoes if transacoes['tipo'] == Saque.__name__ ]
        )
        
        excedeu_limite = valor > self.limite 
        excedeu_saque = numero_de_saques >= self.limite_saque
        
        if excedeu_limite:
            print('\n@@@ Operação falhou o valor de saque excedeu o limite. @@@')
            
        elif excedeu_saque:
            print('\n@@@ Operação falhou numero máximo de saque excedeu o limite. @@@  ')
            
        else:
            # Chamando sacar do método pai 
            return super().sacar(valor)
        
        return False  
  
    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C\C:\t\t{self.numero}
            Titular:{self.cliente.name}        
        """

          
class Historico:
    def __init__(self) -> None:
        self._transacoes = []
        
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data":datetime.now().strftime('%d-%m-%Y %H:%M:%s' ),
            }
            
        )
            

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
