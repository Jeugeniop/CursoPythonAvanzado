from datetime import datetime


#my_time = datetime.now()
#my_day = datetime.date.today()

#print(my_time)
#print(my_day)
#
#print(f"Year: {my_day.year}")
#print(f"Month: {my_day.month}")
#print(f"Day: {my_day.day}")
#
#Formateo de fechas
#%Y año
#%M mes
#%d dia
#%H hora
#%M minuto
#%S segundo

my_datetime = datetime.now()

my_str = my_datetime.strftime("%d/%m/%Y")
print(f"Formato LATAM {my_str}" )