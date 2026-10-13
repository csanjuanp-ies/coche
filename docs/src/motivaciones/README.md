# Cap 01 - Motivaciones
El desarrollo del IOT está movilizando de recursos humanos para su desarrollo. La incorporación de cualificaciones relacionadas con el IOT y la IA se presentan fundamentales en el alumnado que estudia programación hoy en día.

La incoropración de esta práctica permite mezclar ambos campos de studio y dotar al alumnado de una visión generalista de lo que se puede llegar a hacer.

El proyecto se abordará en dos fases diferentes:
1. En la primera crearemos un gemelo virtual del coche, usandolo para entrentar la Red neuronal subyacente que tomará las decisiones posteriormente en el mundo real.
2. En una segunda fase, se comprobará sobre una plataforma hardware real el funcionamiento de la misma. El refinado de la toma de decisiones siempre se realizará sobre la simulación.

## El problema
Nos hemos planteado un problema que hoy en día está muyde moda en las noticas: el desplazamiento autónomo. Encontramos drones, robots de reparto, trenes, coches, taxis e incluso autobuses que empiezan a ser completamente autónomos.

En nuestro caso desarrollaremos un peuqeño coche dirigido por un microcontrolador para que sea capaz de desplazarse de una posición GPS a otra evitando los obstáculos que encuentre. No se harán uso de sistemas de guiado externo tales como Google Maps y otros, siendo los únicos datos que recibuirá el autómata los datos que sea capaz de leer del mundo a través de sus sensores, los datos que recoja del GPS y los datos de destino.

## Fase Uno: Simulación y entranamiento
En esta fase crearemos un gemelo virtual del coche, que utilizaremos para entrentar una red neuronal definida también por nosotros. Evaluaremos la efeictividad de la misma.

### Hardare
- Ordenador con tarjeta gráfica RTK con 8GB al menos

### Software
- Pyton 3.12 al menos
- un IDE

## Fase Dos: Implementación
Durante esta fase validaremos al fase uno en un entorno real.

### Hardware
- Microcontrolador capaz de ejecutar python: Arudino, ESP32, MiocroBit
- Elementos para crear el coche: Ruedas, motores, conectores, etc...
- Antena receptora GPS 3.3V basada en NEO-6M 

## Temporalización
| Fase         | Descripción               | Tiempo         |
| ------------ | ------------------------- | -------------- |
| Fase 1       | Creación del gemelo       | 1 mes          |
| Fase 1.1     | RRNN y entrenamiento      | 1 mes          |
| Fase 1.2     | Validación de la red      | 2 semanas      |
| Fase 2       | Validación en real        | 1 mes          |