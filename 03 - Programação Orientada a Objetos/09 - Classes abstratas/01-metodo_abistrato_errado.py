# E python não temos a palavra reservada interface como no java, o java não permite enrança múltiplas
# Mais o python sim então criamos uma classe e herdamos todos os seu methods , que é um conceito de contrato 

class ControleRemoto:
    
    def ligar(self):
        pass
    
    def desligar(self):
        pass
    
# Jeito errado de usar a interface aqui estou apenas herdando sem a interface 
class ControleTv(ControleRemoto):
    pass

control = ControleTv()
control.ligar()
control.desligar()