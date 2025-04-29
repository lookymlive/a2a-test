# Estructura del proyecto a2a-test

A continuación se detalla la estructura actual del proyecto y la función de cada archivo o carpeta:

```wsl
a2a-test/
│
├── pyproject.toml        # Configuración principal del proyecto Python, dependencias y build
├── README.md             # Documentación principal y guía de uso
├── uv.lock               # Archivo de bloqueo de dependencias generado por uv
│
├── docs/                 # Documentación adicional y guías específicas
│   ├── windows_pwsh.md   # Guía paso a paso para usar el proyecto en PowerShell (Windows)
│   ├── wsl_linux.md      # Guía paso a paso para usar el proyecto en WSL/Linux
│   └── wsl_setup.md      # Guía para instalar y configurar WSL Ubuntu en Windows
│
└── src/                  # Código fuente del proyecto
    └── a2a_test/         # Módulo principal para pruebas y ejemplos A2A
        ├── __init__.py   # Inicializa el paquete Python a2a_test
        └── agent.py      # Script principal de ejemplo y pruebas para el protocolo A2A
```

## Descripción de cada archivo/carpeta

- **pyproject.toml**: Define la configuración del proyecto, dependencias, scripts y sistema de build.
- **README.md**: Documentación principal, propósito y pasos de uso del proyecto.
- **uv.lock**: Archivo generado automáticamente para asegurar versiones exactas de dependencias.
- **docs/**: Carpeta con documentación adicional y guías detalladas para distintos entornos.
  - **windows_pwsh.md**: Guía para usuarios de PowerShell en Windows.
  - **wsl_linux.md**: Guía para usuarios de WSL/Linux.
  - **wsl_setup.md**: Instrucciones para instalar y configurar WSL Ubuntu.
- **src/**: Carpeta raíz del código fuente.
  - **a2a_test/**: Módulo principal del proyecto.
    - **_init__.py**: Permite que la carpeta sea reconocida como un paquete Python.
    - **agent.py**: Script de ejemplo para probar y practicar el protocolo A2A.

---

Esta estructura facilita la organización, pruebas y documentación del proyecto a2a-test.
