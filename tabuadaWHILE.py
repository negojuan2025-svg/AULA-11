numero = int(input("Digite o número da tabuada: "))
i = 1
print("---Tabuada do número: {numero} ---")

while i <= 10:
    print(f"{i} x {numero} = ({i * numero })")
    i+=1

print("Fim")