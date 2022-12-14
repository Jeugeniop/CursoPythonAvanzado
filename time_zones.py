#es necesario instalar el módulo pytz
#pip install pytz
from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ",bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))
mexico_timezone = pytz.timezone("America/Mexico_City")
mexico_date = datetime.now(bogota_timezone)
print("México: ",mexico_date.strftime("%d/%m/%Y, %H:%M:%S"))
caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(bogota_timezone)
print("Caracas: ",caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))