def custo_carro(dias):
    custo = dias * 40

    if dias >= 7:
        custo -= 50
    elif dias >= 3:
        custo -= 20

    return custo

custo = custo_carro(10)
print(custo)
