# Guía para instalar y configurar WSL Ubuntu en Windows

## 1. Instalar WSL y Ubuntu

1. Abre PowerShell como administrador y ejecuta:
   ```
   wsl --install
   ```
2. Reinicia tu computadora si es necesario.
3. Cuando se abra Ubuntu por primera vez, crea un usuario UNIX y una contraseña cuando te lo solicite.

## 2. Acceder a tu proyecto desde Ubuntu (WSL)

1. Abre la terminal de Ubuntu (WSL) desde el menú de inicio o ejecutando `wsl` en PowerShell.
2. Navega a la carpeta de tu proyecto en Windows:
   ```
   cd /mnt/c/Users/usuario/Desktop/a2a-test
   ```

## 3. Instalar dependencias y ejecutar el proyecto

1. Instala las dependencias del proyecto:
   ```
   uv pip install -e .
   ```
   O si tienes `requirements.txt`:
   ```
   uv pip install -r requirements.txt
   ```
2. Ejecuta el ejemplo principal:
   ```
   python3 src/my_project/agent.py
   ```
   Deberías ver:
   ```
   Hello from my-project!
   ```

## 4. Notas útiles
- Puedes crear archivos con comandos Linux, por ejemplo:
  ```
  touch src/my_project/agent.py
  ```
- Si quieres evitar el mensaje de bienvenida diario, ejecuta:
  ```
  touch ~/.hushlogin
  ```
- Los archivos de Windows están accesibles desde `/mnt/c/`.

---

Esta guía te ayudará a instalar, configurar y trabajar con WSL Ubuntu para tus proyectos Python en Windows.
