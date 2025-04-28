# Guía para configurar y ejecutar el proyecto A2A en Windows (PowerShell)

## 1. Estructura del proyecto

Asegúrate de tener la siguiente estructura:

```pwsh
pyproject.toml
README.md
uv.lock
src/
    a2a_test/
        __init__.py
        agent.py
```

## 2. Crear archivos

Para crear archivos desde PowerShell:

```pwsh
New-Item -Path src\a2a_test\agent.py -ItemType File
```

## 3. Instalar dependencias

Si tienes `pyproject.toml`:

```pwsh
uv pip install -e .
```

O si tienes `requirements.txt`:

```pwsh
uv pip install -r requirements.txt
```

## 4. Ejecutar el agente

```pwsh
python src\a2a_test\agent.py
```

## 5. Notas

- Usa doble barra invertida `\` en rutas.
- Ejecuta PowerShell como administrador si tienes problemas de permisos.
- El archivo `agent.py` es el punto de entrada para pruebas A2A.
