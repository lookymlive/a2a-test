# Cómo configurar Google Auth en Expo y Supabase

1. Registra tu app en Google Cloud Console y obtén el CLIENT_ID.
2. Configura el proveedor de Google en el panel de autenticación de Supabase.
3. Usa expo-auth-session para iniciar sesión con Google en tu app Expo.
4. Envía el token de Google a Supabase para autenticar al usuario.

Ejemplo básico de flujo:

- El usuario pulsa "Iniciar sesión con Google" en la app.
- Se abre el flujo OAuth de Google.
- Al finalizar, se obtiene el token y se envía a Supabase para autenticar.

> Puedes agregar aquí ejemplos de código y capturas de pantalla del flujo.
