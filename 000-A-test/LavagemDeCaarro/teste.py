array = ['nao','sim','nao','sim','ok','bem']
une = []

[une.append(item) for item in array  if not item in une ]
        
une.sort()
print(une)


lista_com_duplicatas = ["maçã", "banana", "maçã", "laranja", "banana"]
lista_sem_duplicatas = list(set(lista_com_duplicatas))

print(lista_sem_duplicatas)  # A ordem pode não ser preservada


lista_com_duplicatas = ["maçã", "banana", "maçã", "laranja", "banana"]
lista_sem_duplicatas = list(dict.fromkeys(lista_com_duplicatas))

print(lista_sem_duplicatas)