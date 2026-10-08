from src.data.mundo import Mundo

mundo = Mundo(visualiazar_mapa=False, visualizar_datos=False)

iteraciones: list[int] = []

for _ in range(10):
    print("*"*80)
    mundo.inicializar_datos()
    print(mundo)
    iteraciones.append(mundo.run())

print("*"*80)
print("Iteraciones:",iteraciones)
