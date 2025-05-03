# The conversion prices might vary!!

CO = int(input("What do you have left in pesos? ")) # 1 COP 0.00024 USD
PE = int(input("What do you have left in soles? ")) # 1 PEN 0.27 USD
BR = int(input("What do you have left in reais? ")) # 1 R$ 0.18 USD

peso = CO * 0.00024
soles = PE * 0.27
reais = BR * 0.18

print(peso + soles + reais)