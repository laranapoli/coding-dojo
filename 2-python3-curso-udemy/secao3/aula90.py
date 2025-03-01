"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de 
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de
índices inexistentes na lista
"""
import os

lista_compras = []

while True:
    print('Selecione uma opção:')
    operacao = input('[i]nserir [a]pagar [l]istar: ').lower()

    if operacao == 'l':
        if len(lista_compras) == 0:
            print('Nenhum item para lista')
    
        for i, value in enumerate(lista_compras):
            print(i, value)
    elif operacao == 'i':
        os.system('clear')
        novo_item = input('Item a inserir: ').title()
        lista_compras.append(novo_item)
    elif operacao == 'a':
        i_apagar = input('Escolha o índice para apagar: ')
        try:
            del lista_compras[int(i_apagar)]
        except ValueError:
            print('Por favor, digite um número inteiro!')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro desconhecido.')