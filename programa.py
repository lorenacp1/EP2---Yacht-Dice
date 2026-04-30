```python
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
            print("Digite o índice do dado a ser guardado (0 a 4):")
            indice = int(input())
            resultado = guardar_dado(dados_rolados[:], dados_guardados[:], indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == '2':
            print("Digite o índice do dado a ser removido (0 a 4):")
            indice = int(input())
            resultado = remover_dado(dados_rolados[:], dados_guardados[:], indice)
            dados_rolados = resultado[0]
            dados_guardados = resultado[1]

        elif opcao == '3':
            if rolagens >= 2:
                print("Você já usou todas as rerrolagens.")
            elif len(dados_rolados) == 0:
                print("Você já usou todas as rerrolagens.")
            else:
                dados_rolados = rolar_dados(len(dados_rolados))
                rolagens += 1

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
                    ja_usada = cartela['regra_avancada'][combinacao] != -1
                else:
                    ja_usada = cartela['regra_simples'][int(combinacao)] != -1

                if ja_usada:
                    print("Essa combinação já foi utilizada.")
                else:
                    faz_jogada(dados_t, combinacao, cartela)
                    rodada += 1

        else:
            print("Opção inválida. Tente novamente.")

        jogadas_2 = 0
        for valor in cartela['regra_simples'].values():
            if valor != -1:
                jogadas_2 += 1
        for valor in cartela['regra_avancada'].values():
            if valor != -1:
                jogadas_2 += 1

        if jogadas_2 == jogadas_1:
            print(f"Dados rolados: {dados_rolados}")
            print(f"Dados guardados: {dados_guardados}")

imprime_cartela(cartela)

pontos_simples = 0
for valor in cartela['regra_simples'].values():
    if valor != -1:
        pontos_simples += valor

pontos_avancada = 0
for valor in cartela['regra_avancada'].values():
    if valor != -1:
        pontos_avancada += valor

bonus = 35 if pontos_simples >= 63 else 0
pontuacao = pontos_simples + pontos_avancada + bonus
print(f"Pontuação total: {pontuacao}")
