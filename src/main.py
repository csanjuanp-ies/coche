from twin.mundo import Mundo

mundo = Mundo().hacer_simulado()
#.hacer_visualizar_datos().hacer_visualizar_mapa().hacer_visualizar_ruta()

iteraciones: list[int] = []

for _ in range(10):
    print("*"*80)
    mundo.inicializar_datos()  # obligaorio por las iteraciones
    print(mundo)
    iteraciones.append(mundo.run())

print("*"*80)
print("Iteraciones:",iteraciones)
