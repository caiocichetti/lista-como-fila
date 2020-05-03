ultimo = 10

fila = list(range(1, ultimo + 1))

while True:
    print(f'\nExistem {len(fila)} clientes na fila')
    print(f'Fila atual: {fila}')
    print('Digite F para adicionar um cliente ao fim da fila,')
    print('ou A para realizar o atendimento. S para sair.')

    operacao = input('Operação (F, A ou S): ')

    if operacao == 'A':
        if len(fila) > 0:
            atendido = fila.pop(0)  # Retira o ticket que foi atendido
            print(f'Cliente {atendido} atendido')
        else:
            print('Fila vazia! Nínguem para atender.')

    elif operacao == 'F':
        ultimo += 1  # Incrementa o ticket do novo cliente
        fila.append(ultimo)  # Adiciona o novo ticket

    elif operacao == 'S':
        break

    else:
        print('Operação inválida! Digite apenas F, A ou S!')
