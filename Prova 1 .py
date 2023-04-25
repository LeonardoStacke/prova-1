from datetime import datetime

dataAtual = datetime.now()
mesAtual = dataAtual.month
anoAtual = dataAtual.year
comando = 0


while comando != 10:
    comando = int(input("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n1 - Informar rendimento;\n2 - Alterar rendimento;\n3 - Excluir rendimento;\n4 - Listar rendimento"
                    "\n5 - Informar despesa;\n6 - Alterar despesa;\n7 - Remover despesa;\n8 - Listar despesa;\n9 - Mostrar resultado;\n10 - Sair.\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"))
    if comando < 0 or comando >10:
        print("\033[31mEste comando não existe!\033[0m")
    if comando == 1:

        while True:
            try:
                ano = int(input('Informe o ano: '))
                if ano <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes = int(input('Informe o mês: (1 a 12) '))

                if ano == anoAtual:
                    if mes <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano != anoAtual:
                    if (mes > 0) and (mes <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:
            try:
                descricao = str(input('Informe uma descrição: '))
                break
            except ValueError:
                print("\033[31mEntrada inválida!\033[0m")

        while True:
            try:
                rendimento = float(input('Informe o rendimento: '))
                arquivo = open("dadosTotais.txt", "a")
                arquivo.write(f"{mes},{ano},{descricao},{rendimento},{rendimento},x,0\n")
                arquivo.close()
                print("\n\033[32mRendimento adicionado com sucesso!\033[0m\n")
                break

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um valor válido.\033[0m")

    if comando == 2:
        # Define o mês e ano que deseja buscar e o novo valor do rendimento
        print("\nAlterando rendimento...\n")
        while True:
            try:
                ano_busca = int(input('Informe o ano: '))
                if ano_busca <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes_busca = int(input('Informe o mês: (1 a 12) '))

                if ano_busca == anoAtual:
                    if mes_busca <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano_busca != anoAtual:
                    if (mes_busca > 0) and (mes_busca <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:
            try:
                novo_rendimento = float(input('Informe o novo rendimento: '))
                registros = []
                with open("dadosTotais.txt", "r") as arquivo:
                    for linha in arquivo:
                        mes, ano, rendimento, despesa, saldo, montante = linha.split(",")
                        registro = {"mes": int(mes), "ano": int(ano), "rendimento": float(rendimento)}
                        registros.append(registro)

                for registro in registros:
                    if registro["mes"] == mes_busca and registro["ano"] == ano_busca:
                        registro["rendimento"] = novo_rendimento

                with open("dadosTotais.txt", "w") as arquivo:
                    for registro in registros:
                        arquivo.write(f"{registro['mes']},{registro['ano']},{registro['rendimento']:.2f},{registro['despesa']:.2f},{registro['montante']:.2f}\n")
                print("\n\033[32mRendimento alterado com sucesso!\033[0m\n")
                break

            except ValueError:
                print("\033[31mEntrada inválida!\033[0m")

    if comando == 3:

        print("\nExcluindo rendimento...\n")
        while True:
            try:
                ano_delete = int(input('Informe o ano: '))
                if ano_delete <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes_delete = int(input('Informe o mês: (1 a 12) '))

                if ano_delete == anoAtual:
                    if mes_delete <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano_delete != anoAtual:
                    if (mes_delete > 0) and (mes_delete <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:
            try:

                linhas = []
                with open("dadosTotais.txt", "r") as arquivo:
                    for linha in arquivo:
                        mes, ano, descricao, rendimento, despesa, saldo, montante = linha.split(",")

                        if int(mes) == mes_delete and int(ano) == ano_delete:
                            continue
                        linhas.append(linha)

                    with open("dadosTotais.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

                print("\n\033[32mRendimento deletado com sucesso!\033[0m\n")
                break

            except ValueError:
                print("\033[31mEntrada inválida!\033[0m")

    if comando == 4:

                formato = '%m/%Y'

                lista = []
                linhaFinal = []

                with open('dadosTotais.txt', 'r') as arquivo:

                    rendimentoTotal = float(0)
                    valorTotal = float(0)
                    for linha in arquivo:
                        mes1, ano1, descricao1, rendimento1, despesa1, saldo1, montante1 = linha.split(",")

                        dataRendimento = datetime(int(ano1), int(mes1), 1)
                        diferenca = dataAtual - dataRendimento
                        tempoDeRendimento = diferenca.days // 30

                        saldo1 = float(float(rendimento1)-float(despesa1))
                        montante = round(float(float(saldo1) * ((1+0.01) ** int(tempoDeRendimento))), 2)

                        linha = (f'{mes1},{ano1},{descricao1},{rendimento1},{despesa1},{saldo1},{montante}\n')

                        lista.append(linha)

                        valorTotal = round(float(valorTotal) + float(rendimento1))
                        rendimentoTotal = round(rendimentoTotal + float(montante),2)
                    with open("dadosTotais.txt", "w") as arquivo:
                        arquivo.writelines(lista)


                with open('dadosTotais.txt', 'r') as arquivo:

                    linhas = [linha.strip().split(',') for linha in arquivo]


                for linha in linhas:
                     linha[0] = datetime.strptime(linha[0] + '/' + linha[1], formato)

                linhas_ordenadas = sorted(linhas, key=lambda x: x[0], reverse=True)

                with open('dadosTotaisOrdenado.txt', 'w') as arquivo:
                    for linha in linhas_ordenadas:
                         data = linha[0].strftime('%m/%Y')
                         descricao = linha[2]
                         valor = linha[3]
                         montante = linha[4]
                         arquivo.write(f'Data: {data} - Descrição: {descricao} - Valor aplicado: R${valor} \n')
                    arquivo.write(f'\033[32mTotal: R${valorTotal}\033[0m\n')

                print('Seus investimentos:\n')
                with open('dadosTotaisOrdenado.txt', 'r') as arquivo:
                    for linha in arquivo:
                        print(linha.strip())

    if comando == 5:
        print("\nAdicionando despesa...\n")

        while True:
            try:
                ano_busca = int(input('Informe o ano: '))
                if ano_busca <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes_busca = int(input('Informe o mês: (1 a 12) '))

                if ano_busca == anoAtual:
                    if mes_busca <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano_busca != anoAtual:
                    if (mes_busca > 0) and (mes_busca <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:
            try:
                descricaoDespesa = str(input('Descrição: '))
                despesaNovas = float(input('Valor da despesa: '))
                registros = []
                with open("dadosTotais.txt", "r") as arquivo:
                    for linha in arquivo:
                        mes, ano, descricao, rendimento, saldo, despesa, montante = linha.split(",")
                        registro = {"mes": int(mes), "ano": int(ano), "descricao": descricao,
                                    "rendimento": float(rendimento), "saldo": float(saldo), "despesa": despesa,
                                    "montante": float(montante)}

                        registros.append(registro)

                for registro in registros:
                    if registro["mes"] == mes_busca and registro["ano"] == ano_busca:
                        if registro["saldo"] >= despesaNovas:
                            registro["despesa"] = f"DadosDespesa_{mes_busca}-{ano_busca}.txt"
                            with open(f"DadosDespesa_{mes_busca}-{ano_busca}.txt", "a") as arquivo:
                                arquivo.write(f"{mes_busca},{ano_busca},{descricao},{despesaNovas}\n")
                        else:
                            print("\033[31mSaldo insuficiente.\033[0m")


                with open("dadosTotais.txt", "w") as arquivo:
                    for registro in registros:
                        arquivo.write(f"{registro['mes']},{registro['ano']},{registro['descricao']},{registro['rendimento']},{registro['saldo']},{registro['despesa']},{registro['montante']}\n")
                print("\n\033[32mDespesa registrada com sucesso!\033[0m\n")
                break

            except ValueError:
                print("\033[31mEntrada inválida!\033[0m")

    if comando == 6:

        print("\nAlterando despesa...\n")
        despesaNovas = 0
        while True:
            try:
                ano_busca = int(input('Informe o ano: '))
                if ano_busca <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes_busca = int(input('Informe o mês: (1 a 12) '))

                if ano_busca == anoAtual:
                    if mes_busca <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano_busca != anoAtual:
                    if (mes_busca > 0) and (mes_busca <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:


                registros = []
                with open("dadosTotais.txt", "r") as arquivo:
                    for linha in arquivo:
                        mes, ano, descricao, rendimento, saldo, despesa, montante = linha.split(",")
                        registro = {"mes": int(mes), "ano": int(ano), "descricao": descricao,
                                    "rendimento": float(rendimento), "saldo": float(saldo), "despesa": despesa,
                                    "montante": float(montante)}

                        registros.append(registro)

                for registro in registros:
                    if registro["despesa"]==(f"DadosDespesa_{mes_busca}-{ano_busca}.txt"):
                        with open(f"DadosDespesa_{mes_busca}-{ano_busca}.txt", "r") as arquivo:
                                contador = 1
                                selecionado = 0
                                for linha in arquivo:
                                    mes, ano, descricaoDesp, valor= linha.split(",")
                                    salvo = {"mes": int(mes), "ano": int(ano), "descricao": descricaoDesp,
                                                "valor": float(valor)}
                                    print(f"{contador} - Descrição: {descricaoDesp} / Valor da despesa: {valor}")
                                    contador = contador + 1
                                selecionado = int(input('Selecione qual despesa alterar: '))
                                if selecionado >=contador or selecionado < 1:
                                    print("Opção inválida!")

                                contador = 1
                                registroDesps = []
                                with open(f"DadosDespesa_{mes_busca}-{ano_busca}.txt", "r") as arquivo:

                                    print("-=-=-=-= Substituindo despesa =-=-=-=-\n")
                                    descricaoDespesaNova = str(input('Descrição: '))
                                    despesaNovas = float(input('Valor da despesa: '))

                                    for linha in arquivo:
                                        mesDespesa, anoDespesa, descricaoDespesa, valorDespesa = linha.split(",")
                                        registroDesp = {"mesDesp": int(mesDespesa), "anoDesp": int(anoDespesa),
                                                        "descriçãoDesp": descricaoDespesa,
                                                        "valorDesp": float(valorDespesa)}

                                        contador = contador + 1
                                        if selecionado == contador:
                                            if registro["saldo"] >= despesaNovas:
                                                registroDesp = {"mesDesp": int(mesDespesa), "anoDesp": int(anoDespesa),
                                                                "descriçãoDesp": descricaoDespesaNova,
                                                                "valorDesp": float(despesaNovas)}
                                                registroDesps.append(registroDesp)
                                                contador = contador + 1
                                            else:
                                                print("\033[31mSaldo insuficiente.\033[0m")
                                        else:
                                            registroDesp = {"mesDesp": int(mesDespesa), "anoDesp": int(anoDespesa),"descriçãoDesp": descricaoDespesa,"valorDesp": float(valorDespesa)}
                                        registroDesps.append(registroDesp)
                                        contador = contador + 1

                                    with open(f"DadosDespesa_{mes_busca}-{ano_busca}.txt",
                                                                    "w") as arquivo:
                                        for registroDesp in registroDesps:
                                            arquivo.write(f'{mes_busca},{ano_busca},{registroDesp["descriçãoDesp"]},{registroDesp["valorDesp"]}\n')

                with open("dadosTotais.txt", "w") as arquivo:
                    for registro in registros:
                        arquivo.write(
                            f"{registro['mes']},{registro['ano']},{registro['descricao']},{registro['rendimento']},{registro['saldo']},{registro['despesa']},{registro['montante']}\n")
                print("\n\033[32mDespesa registrada com sucesso!\033[0m\n")


                break

    if comando == 7:

        print("\nExcluindo rendimento...\n")
        while True:
            try:
                ano_delete = int(input('Informe o ano: '))
                if ano_delete <= anoAtual:
                    break
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um ano válido.\033[0m")
            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um ano existente.\033[0m")

        while True:
            try:
                mes_delete = int(input('Informe o mês: (1 a 12) '))

                if ano_delete == anoAtual:
                    if mes_delete <= mesAtual:
                        break
                    else:
                        print(f"\033[31mEntrada inválida! Por favor, digite um igual ou anterior a {mesAtual}.\033[0m")
                elif ano_delete != anoAtual:
                    if (mes_delete > 0) and (mes_delete <= 12):
                        break
                    else:
                        print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")
                else:
                    print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

            except ValueError:
                print("\033[31mEntrada inválida! Por favor, digite um mês existente.\033[0m")

        while True:


                linhas = []
                with open("dadosTotais.txt", "r") as arquivo:
                    contador = 1
                    for linha in arquivo:
                        mes, ano, descricao, rendimento, despesa, saldo, montante = linha.split(",")
                        with open(f"DadosDespesa_{mes_delete}-{ano_delete}.txt", "r") as arquivo:
                                contador = 1
                                selecionado = 0
                                for linha in arquivo:
                                    mes, ano, descricaoDesp, valor= linha.split(",")
                                    salvo = {"mes": int(mes), "ano": int(ano), "descricao": descricaoDesp,
                                                "valor": float(valor)}
                                    print(f"{contador} - Descrição: {descricaoDesp} / Valor da despesa: {valor}")
                                    contador = contador + 1
                                selecionado = int(input('Selecione qual despesa alterar: '))

                                if selecionado >=contador or selecionado < 1:
                                    print("Opção inválida!")
                                contador = 1
                                for linha in arquivo:
                                    mes, ano, descricaoDesp, valor= linha.split(",")
                                    salvo = {"mes": int(mes), "ano": int(ano), "descricao": descricaoDesp,
                                                "valor": float(valor)}
                                    if selecionado == contador:
                                        continue
                                    contador = contador + 1

                        linhas.append(salvo)

                    with open("dadosTotais.txt", "w") as arquivo:
                        arquivo.writelines(linhas)

                print("\n\033[32mRendimento deletado com sucesso!\033[0m\n")
                break

    if comando == 8:

                formato = '%m/%Y'

                lista = []
                linhaFinal = []

                with open('dadosTotais.txt', 'r') as arquivo:

                    rendimentoTotal = float(0)
                    valorTotal = float(0)

                    for linha in arquivo:
                        mes1, ano1, descricao1, rendimento1, despesa1, saldo1, montante1 = linha.split(",")

                        with open(f'{despesa1}', 'r') as arquivo:
                            alista = []
                            mes, ano, descricao, valor = linha.split(",")
                            alista = (f'{mes},{ano},{descricao},{valor}\n')
                            lista.append(alista)

                        dataRendimento = datetime(int(ano1), int(mes1), 1)
                        diferenca = dataAtual - dataRendimento
                        tempoDeRendimento = diferenca.days // 30

                        valorTotal = round(float(valorTotal) + float(rendimento1))
                        rendimentoTotal = round(rendimentoTotal + float(montante),2)
                    with open("dadosTotais.txt", "w") as arquivo:
                        arquivo.writelines(lista)


                with open('dadosTotais.txt', 'r') as arquivo:

                    linhas = [linha.strip().split(',') for linha in arquivo]


                for linha in linhas:
                     linha[0] = datetime.strptime(linha[0] + '/' + linha[1], formato)

                alista_ordenadas = sorted(linhas, key=lambda x: x[0], reverse=True)

                with open('despesasTotaisOrdenado.txt', 'w') as arquivo:
                    for linha in alista_ordenadas:
                         data = linha[0].strftime('%m/%Y')
                         descricao = linha[2]
                         valor = linha[3]
                         arquivo.write(f'Data: {data} - Descrição: {descricao} - Valor gasto: R${valor} \n')
                    arquivo.write(f'\033[32mTotal: R${valorTotal}\033[0m\n')

                print('Suas despesas:\n')
                with open('despesasTotaisOrdenado.txt', 'r') as arquivo:
                    for linha in arquivo:
                        print(linha.strip())

    if comando == 9:

                formato = '%m/%Y'

                lista = []
                linhaFinal = []

                with open('dadosTotais.txt', 'r') as arquivo:

                    rendimentoTotal = float(0)
                    valorTotal = float(0)
                    for linha in arquivo:
                        mes1, ano1, descricao1, rendimento1, despesa1, saldo1, montante1 = linha.split(",")

                        dataRendimento = datetime(int(ano1), int(mes1), 1)
                        diferenca = dataAtual - dataRendimento
                        tempoDeRendimento = diferenca.days // 30

                        saldo1 = float(float(rendimento1)-float(despesa1))
                        montante = round(float(float(saldo1) * ((1+0.01) ** int(tempoDeRendimento))), 2)

                        linha = (f'{mes1},{ano1},{descricao1},{rendimento1},{despesa1},{saldo1},{montante}\n')

                        lista.append(linha)

                        valorTotal = round(float(valorTotal) + float(rendimento1))
                        rendimentoTotal = round(rendimentoTotal + float(montante),2)
                    with open("dadosTotais.txt", "w") as arquivo:
                        arquivo.writelines(lista)


                with open('dadosTotais.txt', 'r') as arquivo:

                    linhas = [linha.strip().split(',') for linha in arquivo]


                for linha in linhas:
                     linha[0] = datetime.strptime(linha[0] + '/' + linha[1], formato)

                linhas_ordenadas = sorted(linhas, key=lambda x: x[0], reverse=True)

                with open('dadosTotaisOrdenado.txt', 'w') as arquivo:
                    for linha in linhas_ordenadas:
                         data = linha[0].strftime('%m/%Y')
                         descricao = linha[2]
                         valor = linha[3]
                         montante = linha[4]
                         arquivo.write(f'Data: {data} - Descrição: {descricao} - Valor aplicado: R${valor} \n')
                    arquivo.write(f'\033[32mTotal: R${valorTotal}\033[0m\n')

                print('Seus investimentos:\n')
                with open('dadosTotaisOrdenado.txt', 'r') as arquivo:
                    for linha in arquivo:
                        print(linha.strip())






