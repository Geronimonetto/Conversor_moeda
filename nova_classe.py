from Valores import todas

def msg():
    print("*" * 40)
    print(f"{'SEJA BEM VINDO AO CONVERSOR DE MOEDA':^15}".center(40))
    print("*" * 40)
    print()

def mapeamento(args = {}):
    lista_valores = []
    for v in args.values():
        for c in v:
            if c == 'dinheiro':
                lista_valores.append(v['dinheiro'])
    return lista_valores

def modelando(args = {}):

    for n,v in enumerate(args.items()):
        print(f'{n+1} {v[0]}')
    print()


valor = mapeamento(todas)
