        


# Components of another_year add up to exactly 365 days
# from datetime import timedelta
# year = timedelta(days=365)
# another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
# resultado = year.total_seconds() == another_year.total_seconds()
# resultado2 = year == another_year

# print(resultado,"---",resultado2)  

fu = input( 'digite = ')
s = fu.split(',')
var = []
for i in s:
    if i.strip():
        var.append(i.strip())
print('Vs linhas = ',var)


vary = [nome.strip() for nome in s if nome.strip()]
print('Uma linha = ',vary)