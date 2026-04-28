import random
def rolar_dados(dados):
    dados_r = []
    for i in range(dados):
        dados_r.append(random.randint(1,6))
    return dados_r

def guardar_dado(dados_rolados,dados_no_estoque,dado_para_guardar):
    lista = []
    dados_restantes = lista[0]
    dados_armazenados = lista[1]
    
    for dado_para_guardar in range(len(dados_rolados)):
        dados_restantes = dados_rolados.pop(dado_para_guardar)
        dados_armazenados = dados_no_estoque.append(dados_rolados[dado_para_guardar])
        dados_restantes = lista[0]
        dados_armazenados = lista[1]
    return lista


    

