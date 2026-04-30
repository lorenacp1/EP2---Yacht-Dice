from funcoes import *

cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'sem_combinacao': -1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1,
    }
}

combinacoes_possiveis = [
    '1','2','3','4','5','6',
    'sem_combinacao', 'quadra', 'full_house',
    'sequencia_baixa', 'sequencia_alta', 'cinco_iguais'
]

rodada = 1
while rodada <= 12:
    acabou = True
    for valor in cartela['regra_simples'].values():
        if valor == -1:
            acabou = False
    for valor in cartela['regra_avancada'].values():
        if valor == -1:
            acabou = False
    if acabou:
        break

    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rolagens = 0
    jogadas_1 = 0
    for ponto in cartela['regra_simples'].values():
        if ponto != -1:
            jogadas_1 += 1
    for ponto in cartela['regra_avancada'].values():
        if ponto != -1:
            jogadas_1 += 1

    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")

    jogadas_2 = jogadas_1
    while jogadas_2 == jogadas_1:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índ