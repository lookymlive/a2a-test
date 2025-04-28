# Proyecto de ejemplo: a2a-test

Este proyecto es una prueba de integración y configuración del protocolo A2A (Agente a Agente) de Google, usando Python. Incluye ejemplos para organizar tu código y ejecutar pruebas tanto en Windows (PowerShell) como en WSL/Linux.

## ¿Para qué sirve este proyecto?

- Aprender a estructurar un proyecto Python moderno.
- Probar el protocolo A2A de Google entre agentes.
- Practicar la ejecución y gestión de dependencias multiplataforma (Windows/WSL).

## Estructura del proyecto

```
pyproject.toml
README.md
uv.lock
docs/
    windows_pwsh.md
    wsl_linux.md
src/
    a2a_test/
        __init__.py
        agent.py
    my_project/
        agent.py
        task_manager.py
```

## Pasos para configurar y ejecutar el proyecto

### 1. Crear los archivos necesarios

En Windows PowerShell:
```
New-Item -Path src\my_project\agent.py -ItemType File
New-Item -Path src\my_project\task_manager.py -ItemType File
```

En WSL/Linux:
```
touch src/my_project/agent.py

touch src/my_project/task_manager.py
```

### 2. Instalar dependencias

Si tienes `pyproject.toml`:
```
uv pip install -e .
```
O si tienes `requirements.txt`:
```
uv pip install -r requirements.txt
```

### 3. Ejecutar el ejemplo principal

```
python src/my_project/agent.py
```

Deberías ver en la terminal:
```
Hello from my-project!
```

### 4. Ejecutar el gestor de tareas (opcional)

```
python src/my_project/task_manager.py
```

Deberías ver:
```
Task manager running!
```

---

Consulta la carpeta `docs/` para guías detalladas según tu sistema operativo.
