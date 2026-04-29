from funcoes import *
cartela = {
    'regra_simples': {i: -1 for i in range(1, 7)},
    'regra_avancada': {
        'cinco_iguais': -1,
        'full_house': -1,
        'quadra': -1,
        'sem_combinacao': -1,
        'sequencia_alta': -1,
        'sequencia_baixa': -1,
    }
}

combinacoes_possiveis = ['1','2','3','4','5',6]

for rodada in range(1,13):
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

    print(f'Dados rolados: {dados_rolados}')
    print(f'Dados guardados: {dados_guardados}')

    jogadas_2 = jogadas_1
    while jogadas_2 == jogadas_1:
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados,dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado [1]
        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados,dados_guardados,indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == '3':
            if rolagens >=2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rolagens+=1
        elif opcao == '4':
            imprime_cartela(cartela)
        elif opcao == '0':
            print("Digite a combinação desejada:")
            combinacao = input()
            dados_t = dados_rolados + dados_guardados

            if combinacao not in combinacoes_possiveis:
                print("Combinação inválida. Tente novamente.")
            else:
                if combinacao in cartela['regra_avancada']:
                    


