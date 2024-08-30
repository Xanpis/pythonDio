"""
Conhecendo métodos úteis par manipular abjetos do tipo string
como interpolar valores de variáveis e entender como
funciona o fatiamento 

"""



from shlex import join


nome = "pYtHon"
#  metodo par transforma a primeira letra em maiusculo
print("###### inicio ######")
print(nome.title())

nome = "    pYtHon Espaco    "
print("..."  +  nome  + '....')

#  removendo espaco em branco dos 2 lados 
print("..."  + nome.strip() + '....')

#  removendo espaco em branco do lado esquerdo  
print("..."  +  nome.lstrip() + '....')

#  removendo espaco em branco do lado  direito
print("..."  +  nome.rstrip() + '....')


# Junção e centralização 
nome = "python"
# centralização
print(nome.center(10,"#"))
# junção
print(".".join(nome))
 