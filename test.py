
# menu = """

# [d] Depositar
# [s] Sacar
# [e] Extrato
# [q] Sair

# => """

# saldo = 0
# limite = 500
# extrato = ""
# numero_saques = 0
# LIMITE_SAQUES = 3

# while True:
#     op = input(menu)
    
#     # Depositar
#     if op == "d":
#         pass
            
#     # Sacar        
#     elif op == "s":
#         pass
    
#     elif op == "e":
#         pass
    
#     else:
#         print("Opção invalida")
        
        


# Components of another_year add up to exactly 365 days
from datetime import timedelta
year = timedelta(days=365)
another_year = timedelta(weeks=40, days=84, hours=23,minutes=50, seconds=600)
resultado = year.total_seconds() == another_year.total_seconds()
resultado2 = year == another_year

print(resultado,"---",resultado2)  