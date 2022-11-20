print("********Conversor de Temperaturas********")

Fahrenheit = print("Digite 1 para Fahrenheit")
Kelvin = print("Digite 2 para Kelvin")
Rankine = print("Digite 3 para Rankine")
Reaumur = print("Digite 4 para Reaumur")
Romer = print("Digite 5 para Romer")
Newton = print("Digite 6 para Newton")
Delisle = print("Digite 7 para Delisle")
continuar = 1
while continuar == 1:

    escala_termomtricas = float(input("O que deseja converter? "))
    valor_celsius = float(input("Digite a temperatura em celsius: \n"))
    resultado = 0
    if escala_termomtricas == 1:
        resultado = valor_celsius * 1.8 + 32
        print(f"O valor em Fahrenheit é {resultado} °F")
    elif escala_termomtricas == 2:
        resultado = valor_celsius + 273
        print(f"O valor em Kelvin é {resultado} ºC")
    elif escala_termomtricas == 3:
        resultado = (valor_celsius + 273.15) * 1.8
        print(f"O valor em Rankine é {resultado} ºRa")
    elif escala_termomtricas == 4:
        resultado = valor_celsius * 0.8
        print(f"O valor em Reaumur é {resultado} ºRe")
    elif escala_termomtricas == 5:
        resultado = (valor_celsius) * 0.525 + 7.5
        print(f"O valor em Romer é {resultado} ºRO")
    elif escala_termomtricas == 6:
        resultado = (valor_celsius) * 0.33
        print(f"O valor em Newton é {resultado} ºN")
    elif escala_termomtricas == 7:
        resultado = (100 - valor_celsius) * 1.5
        print(f"O valor em Delisle é {resultado} ºDE")
    else:
        print("Opção invalida, tente novamente:")
        continue

    print("Desenja fazer outra conta?")
    print("1 - SIM")
    print("2 - Não")
    continuar = int(input())