import random
def rolar_dados(dados):
    dados_r = []
    for i in range(dados):
        dados_r.append(random.randint(1,6))
    return dados_r

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
	dado_novo = dados_rolados[dado_para_guardar]
	dados_no_estoque.append(dado_novo)
	dados_rolados.pop(dado_para_guardar)
	return[dados_rolados, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
     dados_rolados.append(dados_no_estoque[dado_para_remover])
     dados_no_estoque.pop(dados_no_estoque[dado_para_remover])
     return[dados_rolados, dados_no_estoque]