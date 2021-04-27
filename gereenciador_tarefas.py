
if __name__ == '__main__':
    lista = []
    excluidos_lista = []
    refazendo_lista = []

def int_selecao(selecao):
    try:
        selecao = int(selecao)
        selecao <= 5
        return selecao
    except ValueError:
        pass

while True:
    print()
    print('1 - Adicionar uma nova tarefa')
    print('2 - Listar as minhas tarefas')
    print('3 - Remover uma das minhas tarefas')
    print('4 - Re-colocar uma tarefa')
    print('5 - Desejo sair do meu organizador')
    print()
    selecao = int_selecao(input('Bem vindo ao organizador de tarefas, escolha uma das opções acima: '))

    if selecao is None:
        print('Insira apenas um número de 1 a 5')
        print()
        print('-' * 169)
        pass

    if selecao == 1:
        while True:
            print()
            nova_tarefa = input('Qual é a sua nova tarefa?: ')
            lista.append(nova_tarefa)
            print()
            print('Sua tarefa foi adicionada ao gerenciador')
            print()
            print('-' * 169)
            break

    elif selecao == 2:
        while True:
            listador = 'Suas tarefas atuais são:'
            print()
            print(listador)
            print(lista)
            print()
            print('-' * 169)
            break

    elif selecao == 3:
        while True:
            print()
            last_tarefa = input('Em ordem numérica (1a, 2a...), qual a tarefa que você deseja remover?: ')
            if not last_tarefa.isdigit():
                print()
                print('Digite apenas um valor numérico!')
                print()
                print('Tente novamente...')
                print()
                print('-' * 169)
                break
            else:
                excluidos_lista.append(nova_tarefa)
                last_tarefa = len(lista.pop())
                print()
                print('Ok... Sua tarefa foi removida!')
                print()
                print('-' * 169)
            break

    elif selecao == 4:
        while True:
            print()
            print('Sua última tarefa excluida será recuperada...')
            lista.append((excluidos_lista[-1]))
            print()
            print('Tarefa recuperada com sucesso!')
            excluidos_lista.pop()
            print()
            print('-' * 169)
            break

    elif selecao == 5:
        print()
        print('Até logo... =)')
        break
