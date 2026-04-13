print("-" * 20)
print("Cálculo do IRRF")
print("-" * 20)

resposta = True

while resposta == True:
    try:
        sal_bruto = float(input("Digite seu salário bruto: "))

       
        if sal_bruto <= 2428.80:
            irrf = 0.0  # Isento
        elif 2428.81 <= sal_bruto <= 2826.65:
            irrf = 0.075
        elif 2826.66 <= sal_bruto <= 3751.05:
            irrf = 0.15
        elif 3751.06 <= sal_bruto <= 4664.68:
            irrf = 0.225
        else:
            irrf = 0.275

    
        valor_imposto = sal_bruto * irrf
        sal_liquido = sal_bruto - valor_imposto
        
        print(f"{sal_bruto} com {irrf * 100}% = R$ {sal_liquido:.2f}")

    except ValueError:
        print("Valor do salário inválido!")

   
    continuar = input("Deseja realizar outro cálculo (S/N): ")
    if resposta == 'S' or resposta == 's':
        resposta = True
    else:
        resposta = False

    