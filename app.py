import pandas as pd
from models.cliente import Cliente
from models.vendedora import Vendedora
from controllers.disparador import DisparadorController

def carregar_dados_excel(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    lista_clientes = []

    for _, linha in df.iterrows():
        novo_cliente = Cliente(
            nome= linha['Nome'],
            telefone=linha['WhatsApp'],
            mensagem=linha['Mensagem'],
            vendedora_responsavel=linha['Vendedora']
        )
        lista_clientes.append(novo_cliente)

    return lista_clientes

def main():
    print(f'{'-'*10} Iniciando Sistema de Disparos Automáticos v1.0 {'-'*10}')

    todos_clientes = carregar_dados_excel('./data/clientes.xlsx')

    nomes_vendedoras = set([c.vendedora_responsavel for c in todos_clientes])

    for nome_v in nomes_vendedoras:
        print(f'\n>>>>> Preparando disparos para: {nome_v}')

        vendedora_obj = Vendedora(nome=nome_v, id=nome_v.lower().replace(' ', '_'))
        clientes_da_vez = [c for c in todos_clientes if c.vendedora_responsavel == nome_v]

        disparador = DisparadorController(vendedora_obj)
        disparador.iniciar_disparo(clientes_da_vez)

        print(f'<<< Finalizado lote da {nome_v}! Memória RAM Liberada.')

if __name__ == '__main__':
    main()