"""
Conhecendo métodos úteis par manipular abjetos do tipo string
como interpolar valores de variáveis e entender como
funciona o fatiamento 

"""

nome = "pYtHon"
#  método par transforma a primeira letra em maiúsculo
print("###### inicio ######")
print(nome.title())

nome = "    pYtHon Espaço    "
print("..."  +  nome  + '....')

#  removendo espaço em branco dos 2 lados 
print("..."  + nome.strip() + '....')

#  removendo espaço em branco do lado esquerdo  
print("..."  +  nome.lstrip() + '....')

#  removendo espaço em branco do lado  direito
print("..."  +  nome.rstrip() + '....')


# Junção e centralização 
nome = "python"
# centralização
print(nome.center(10,"#"))

# junção
print(".".join(nome))
 