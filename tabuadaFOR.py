numero = int(input("Digite o número da tabuada: "))

print("---Tabuada do número: {numero} ---")
for i in range (1, 11):
    print(f"{i} x {numero} = ({i * numero })")

print("Fim")