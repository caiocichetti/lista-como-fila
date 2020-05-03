ultimo = 10

fila = list(range(1, ultimo + 1))

# Estilização do terminal
corHeader = '\033[95m'
corOk = '\033[94m'
corOkGreen = '\033[92m'
corFail = '\033[91m'
corWarning = '\033[93m'
bold = '\033[1m'
end = '\033[0m'

while True:
    print(f'\n{corHeader}Existem {len(fila)} clientes na fila{end}')
    print(f'\n{corWarning}Fila atual: {fila}{end}')
    print(f'\nDigite {bold}F{end} para adicionar um cliente ao fim da fila,')
    print(f'ou {bold}A{end} para realizar o atendimento. {bold}S{end} para sair.\n')

    operacao = input(f'{bold}Operação (F, A ou S): {end}')

    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)  # Retira o ticket que foi atendido
            print(f'{corOk}\nCliente {atendido} atendido{end}')
        else:
            print(f'\n{corOkGreen}Fila vazia! Nínguem para atender.{end}')

    elif operacao == 'F':
        ultimo += 1  # Incrementa o ticket do novo cliente
        fila.append(ultimo)  # Adiciona o novo ticket

    elif operacao == 'S':
        break

    else:
        print(f'\n{corFail}Operação inválida! Digite apenas F, A ou S!{end}')
