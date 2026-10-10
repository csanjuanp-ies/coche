from data.mundo import Mundo

mundo = Mundo(True, visualiazar_mapa=False, visualizar_datos=False, visualizar_ruta=False)

iteraciones: list[int] = []

for _ in range(10):
    print("*"*80)
    mundo.inicializar_datos()  # obligaorio por las iteraciones, sino no
    print(mundo)
    iteraciones.append(mundo.run())

print("*"*80)
print("Iteraciones:",iteraciones)
