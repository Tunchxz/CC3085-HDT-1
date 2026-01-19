# Inteligencia Artificial - HDT 1

## Descripción

Implementación de un Agente Reflejo Simple que simula un termostato inteligente. El agente percibe la temperatura del entorno y toma decisiones para mantenerla en un rango 18-25°C.

## Estructura del Proyecto

```
├── agent.py          # Clase Agent con lógica de decisión
├── enviorment.py     # Clase Environment que simula el entorno
├── main.py           # Ciclo principal Percepción/Acción
└── README.md         # Documentación
```

## Componentes

### Agente (agent.py)
Implementa la función de mapeo `f(estado) → acción`:
- **Temperatura < 18°C**: Acción "calentar"
- **Temperatura > 25°C**: Acción "enfriar"
- **18°C ≤ Temperatura ≤ 25°C**: Acción "esperar"

### Ambiente (enviorment.py)
Simula el entorno con:
- Temperatura inicial aleatoria (15-30°C)
- `get_percept()`: Devuelve la temperatura actual
- `update(action)`: Modifica la temperatura según la acción (+1 calentar, -1 enfriar)

### Main (main.py)
Ciclo de 10 iteraciones que ejecuta:
1. Percepción del estado actual
2. Decisión del agente
3. Actualización del entorno
4. Impresión de resultados

## Ejecución

```bash
python main.py
```

## Ejemplo de Salida

```
Paso 1: Temperatura (Estado Actual)= 27, Acción = enfriar, Nueva Temperatura = 26
Paso 2: Temperatura (Estado Actual)= 26, Acción = enfriar, Nueva Temperatura = 25
Paso 3: Temperatura (Estado Actual)= 25, Acción = esperar, Nueva Temperatura = 25
...
```

## Colaboradores

- Cristian Túnchez  

- Nadissa Vela
