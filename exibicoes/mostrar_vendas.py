import time


def exibir_vendas(vendas):
    for venda in vendas:
        time.sleep(0.7)
        print("------------------")
        print(f"Identificador: {venda[0]} - Data: {venda[2]}\nCliente: {venda[1]} - Valor Total: {venda[3]}")
        print("------------------")