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

## Ejemplo práctico: Simulación de colaboración entre agentes

Este ejemplo muestra cómo simular la colaboración entre un Product Manager, un Desarrollador y un Diseñador usando agentes en el proyecto.

### Archivos involucrados

- `src/a2a_test/agent_product_manager.py`: Simula la solicitud de una nueva funcionalidad.
- `src/a2a_test/agent_developer.py`: Simula la recepción de la solicitud y la petición de diseño.
- `src/a2a_test/agent_designer.py`: Simula la creación y compartición del diseño en Figma.

### Cómo probarlo

Ejecuta cada agente en la terminal, uno tras otro:

```wsl
python3 src/a2a_test/agent_product_manager.py
python3 src/a2a_test/agent_developer.py
python3 src/a2a_test/agent_designer.py
```

Verás cómo cada agente cumple su rol y colabora en el flujo de trabajo:

```wsl
[Product Manager] Solicita al desarrollador: Nueva funcionalidad: Pantalla de login
[Desarrollador] Recibe la solicitud y pide diseño al diseñador en Figma.
[Diseñador] Crea el diseño en Figma y lo comparte con el equipo.
```

## Implementación paso a paso del flujo de colaboración entre agentes

Este proyecto simula la colaboración entre tres roles clave en el desarrollo de una app móvil: Product Manager, Diseñador y Desarrollador, usando agentes que representan a cada uno.

### 1. Estructura de archivos

- `src/a2a_test/agent_product_manager.py`: Simula la solicitud de una funcionalidad al diseñador.
- `src/a2a_test/agent_designer.py`: Recibe la solicitud, desarrolla el diseño en Figma y lo comparte.
- `src/a2a_test/agent_developer.py`: Recibe el diseño, planifica la implementación y comunica al equipo.

### 2. Flujo de trabajo simulado

1. **El Product Manager solicita una funcionalidad:**
   - Ejecuta:

     ```bash
     python3 src/a2a_test/agent_product_manager.py
     ```

   - Salida esperada:

     ```wsl
     [Product Manager] Solicito al diseñador: Por favor desarrolla un diseño en Figma para una pantalla de inicio de sesión de una app móvil con dos roles: usuario y comercio. La autenticación debe ser con Supabase y Google.
     ```

2. **El Diseñador recibe la solicitud y crea el diseño:**
   - Ejecuta:

     ```bash
     python3 src/a2a_test/agent_designer.py
     ```

   - Salida esperada:

     ```wsl
     [Diseñador] Recibida la solicitud del Product Manager.
     [Diseñador] Desarrollo en Figma el diseño de una pantalla de inicio de sesión para una app móvil con dos roles: usuario y comercio.
     [Diseñador] El diseño contempla autenticación con Supabase y Google, y se comparte el enlace de Figma con el equipo.
     ```

3. **El Desarrollador recibe el diseño y planifica la implementación:**
   - Ejecuta:

     ```bash
     python3 src/a2a_test/agent_developer.py
     ```

   - Salida esperada:

     ```wsl
     [Desarrollador] Recibe el enlace de Figma con el diseño de la pantalla de inicio de sesión.
     [Desarrollador] Planifica la implementación de la autenticación con Supabase y Google para los roles usuario y comercio.
     [Desarrollador] Informa al Product Manager y al Diseñador que comenzará el desarrollo.
     ```

### 3. Personalización y crecimiento

- Puedes modificar los scripts para que los agentes intercambien mensajes automáticamente (por archivos, sockets, etc.).
- Integra APIs reales (Figma, Supabase, Google, Slack) para automatizar tareas y flujos.
- Agrega lógica de respuesta y validación para simular un flujo de trabajo más realista.

---

## Comunicación real entre agentes usando archivos

Este flujo simula la comunicación real entre agentes usando archivos de texto como canal de mensajes.

### 1. El Product Manager envía la solicitud al diseñador

```bash
python3 src/a2a_test/agent_product_manager.py
```

Esto crea el archivo `message_to_designer.txt` con la solicitud.

### 2. El Diseñador lee la solicitud y responde al desarrollador

```bash
python3 src/a2a_test/agent_designer.py
```

Esto lee `message_to_designer.txt`, muestra la solicitud, y crea `message_to_developer.txt` con el enlace de Figma.

### 3. El Desarrollador lee la respuesta y confirma al equipo

```bash
python3 src/a2a_test/agent_developer.py
```

Esto lee `message_to_developer.txt`, muestra el diseño recibido y crea `message_to_pm.txt` con la confirmación de inicio de desarrollo.

### 4. Verifica los archivos de mensajes

Puedes abrir los archivos `message_to_designer.txt`, `message_to_developer.txt` y `message_to_pm.txt` para ver el contenido de cada mensaje intercambiado.

---

Este flujo puede escalarse para usar sockets, bases de datos o APIs reales para una comunicación más avanzada entre agentes.

---

Esta simulación es una base para practicar y escalar la colaboración entre agentes en proyectos reales.

La carpeta principal para tus prácticas y ejemplos es ahora `src/a2a_test`.
El resto de la documentación y ejemplos hace referencia solo a esta carpeta.

---
