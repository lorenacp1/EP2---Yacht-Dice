import random
def rolar_dados(dados):
    dados_r = []
    for i in range(dados):
        dados_r.append(random.randint(1,6))
    return dados_r

