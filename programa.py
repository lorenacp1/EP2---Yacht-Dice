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

combinacoes_possiveis = ['1','2','3','4','5','6','cinco_iguais','full_house','quadra','sem_combinacao','sequencia_alta','sequencia_baixa']

imprime_cartela(cartela)

for rodada in range(1, 13):
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rolagens = 0

    # Mostra dados e menu no início da rodada
    print(f"Dados rolados: {dados_rolados}")
    print(f"Dados guardados: {dados_guardados}")
    print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

    rodada_terminada = False
    while not rodada_terminada:
        opcao = input()

        if opcao == '1':
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados, dados_guardados, indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '3':
            if rolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rolagens += 1
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '4':
            imprime_cartela(cartela)
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")
            print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        elif opcao == '0':
            print("Digite a combinação desejada:")
            while True:
                combinacao = input()
                if combinacao not in combinacoes_possiveis:
                    print("Combinação inválida. Tente novamente.")
                    continue
                if combinacao in cartela['regra_avancada']:
                    ja_usada = cartela['regra_avancada'][combinacao] != -1
                else:
                    ja_usada = cartela['regra_simples'][int(combinacao)] != -1
                if ja_usada:
                    print("Essa combinação já foi utilizada.")
                    continue
                dados_t = dados_rolados + dados_guardados
                faz_jogada(dados_t, combinacao, cartela)
                break
            rodada_terminada = True

        else:
            print("Opção inválida. Tente novamente.")

imprime_cartela(cartela)
pontos_simples = sum(v for v in cartela['regra_simples'].values() if v != -1)
pontos_avancada = sum(v for v in cartela['regra_avancada'].values() if v != -1)
bonus = 35 if pontos_simples >= 63 else 0
pontuacao = pontos_simples + pontos_avancada + bonus
print(f"Pontuação total: {pontuacao}")