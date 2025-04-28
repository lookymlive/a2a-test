# Guía para configurar y ejecutar el proyecto A2A en WSL (Linux)

## 1. Estructura del proyecto

Asegúrate de tener la siguiente estructura:

```
pyproject.toml
README.md
uv.lock
src/
    a2a_test/
        __init__.py
        agent.py
```

## 2. Crear archivos

Para crear archivos desde WSL:

```
touch src/a2a_test/agent.py
```

## 3. Instalar dependencias

Si tienes `pyproject.toml`:

```
uv pip install -e .
```

O si tienes `requirements.txt`:

```
uv pip install -r requirements.txt
```

## 4. Ejecutar el agente

```
python3 src/a2a_test/agent.py
```

## 5. Notas

- Usa barra normal `/` en rutas.
- Puedes acceder a tu proyecto desde `/mnt/c/Users/usuario/Desktop/a2a-test`.
- El archivo `agent.py` es el punto de entrada para pruebas A2A.
