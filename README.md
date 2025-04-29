# Proyecto de ejemplo: a2a-test

Este proyecto es una prueba de integración y configuración del protocolo A2A (Agente a Agente) de Google, usando Python. Incluye ejemplos para organizar tu código y ejecutar pruebas tanto en Windows (PowerShell) como en WSL/Linux.

## ¿Para qué sirve este proyecto?

- Aprender a estructurar un proyecto Python moderno.
- Probar el protocolo A2A de Google entre agentes.
- Practicar la ejecución y gestión de dependencias multiplataforma (Windows/WSL).

## Estructura del proyecto

```wls
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

```psh
New-Item -Path src\my_project\agent.py -ItemType File
New-Item -Path src\my_project\task_manager.py -ItemType File
```

En WSL/Linux:

```wsl
touch src/my_project/agent.py

touch src/my_project/task_manager.py
```

### 2. Instalar dependencias

Si tienes `

Si tienes `pyproject.toml`:

```wsl
uv pip install -e .
```

O si tienes `requirements.txt`:

``` wsl
uv pip install -r requirements.txt
```

### 3. Ejecutar el ejemplo principal

```wsl
python src/my_project/agent.py
```

Deberías ver en la terminal:

```wsl
Hello from my-project!
```

### 4. Ejecutar el gestor de tareas (opcional)

```wsl
python src/my_project/task_manager.py
```

Deberías ver:

```wsl
Task manager running!
```

---

Consulta la carpeta `docs/` para guías detalladas según tu sistema operativo.

## Diferencia entre pyproject.toml y requirements.txt

- **pyproject.toml**
  - Es el estándar moderno para definir la configuración de un proyecto Python.
  - Permite especificar dependencias, configuración de herramientas de construcción (build), metadatos del proyecto y más.
  - Es compatible con herramientas como Poetry, PDM, Hatch, uv, y pip (a partir de versiones recientes).
  - Permite la instalación editable (`uv pip install -e .`) y la gestión avanzada de entornos.
  - Recomendado para proyectos nuevos y para quienes buscan portabilidad y mejores prácticas.

- **requirements.txt**
  - Es el formato tradicional para listar dependencias de Python, una por línea.
  - Usado principalmente por pip y herramientas clásicas.
  - No incluye metadatos del proyecto ni configuración de build.
  - Sencillo y ampliamente soportado, ideal para proyectos simples o migraciones.

**Resumen:**

- Si tienes ambos archivos, normalmente `pyproject.toml` es el principal y `requirements.txt` puede usarse para compatibilidad o entornos legacy.
- Para proyectos nuevos, se recomienda usar `pyproject.toml`.

## Ejemplo práctico de uso

Puedes probar tu proyecto ejecutando el siguiente comando en WSL/Linux o PowerShell:

```wsl
python3 src/a2a_test/agent.py Copilot
```

Esto mostrará:

```wsl
Hello from Copilot!
```

Si no pasas ningún argumento, mostrará:

```wsl
Hello from a2a-test!
```

---

La carpeta principal para tus prácticas y ejemplos es ahora `src/a2a_test`.
El resto de la documentación y ejemplos hace referencia solo a esta carpeta.

---
