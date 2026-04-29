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
     dados_no_estoque.pop(dado_para_remover)
     return[dados_rolados, dados_no_estoque]

def calcula_pontos_regra_simples(numeros_inteiros):
    resultado = {}
    for numero in range(1, 7):
        quantidade = 0
        for item in numeros_inteiros:
              if item == numero:
                  quantidade +=1
        resultado[numero] = numero * quantidade
    return resultado

def calcula_pontos_soma(dados):
    soma = 0
    for i in range(len(dados)):
        soma+=dados[i]
    return soma

def calcula_pontos_sequencia_baixa(faces):
    for numero in faces:
        if (numero + 1 in faces and
            numero + 2 in faces and
            numero + 3 in faces):
            return 15
    return 0
          
def calcula_pontos_sequencia_alta(faces):
    for numero in faces:
        if (numero + 1 in faces and
            numero + 2 in faces and
            numero + 3 in faces and
            numero + 4 in faces):
            return 30
    return 0

def calcula_pontos_full_house(faces):
    contagens = []
    for i in range(1,7):
        quantidade = 0
        for numero in faces:
            if numero == i:
                quantidade += 1
        if quantidade > 0:
            contagens.append(quantidade)
    if 3 in contagens and 2 in contagens:
        soma = 0
        for numero in faces:
            soma += numero
        return soma
    return 0

def calcula_pontos_quadra(faces):
    contagens = []
    for i in range(1,7):
        quantidade = 0
        for numero in faces:
            if numero == i:
                quantidade += 1
        if quantidade >= 4:
            soma = 0
            for numero in faces:
                soma += numero
            return soma
    return 0

def calcula_pontos_quina(faces):
    contagens = []
    for i in range(1,7):
        quantidade = 0
        for numero in faces:
            if numero == i:
                quantidade += 1
        if quantidade >= 5:
            return 50
    return 0

def calcula_pontos_regra_avancada(faces):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(faces)
    dic['full_house'] = calcula_pontos_full_house(faces)
    dic['quadra'] = calcula_pontos_quadra(faces)
    dic['sem_combinacao'] = calcula_pontos_soma(faces)
    dic['sequencia_alta'] = calcula_pontos_sequencia_alta(faces)
    dic['sequencia_baixa'] = calcula_pontos_sequencia_baixa(faces)

    return dic

def faz_jogada(dados,categoria,cartela_de_pontos):

    if categoria in cartela_de_pontos['regra_avancada']:
        pontos_a = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_a[categoria]

    else:
        categoria_int = int(categoria)
        pontos_s = calcula_pontos_regra_simples(dados)
        categoria_int = int(categoria)
        cartela_de_pontos['regra_simples'][categoria_int] =pontos_s[categoria_int]

    return cartela_de_pontos




    
