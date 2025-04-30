import os
import sys

MESSAGE_IN = "message_to_designer.txt"
MESSAGE_OUT = "message_to_developer.txt"


def main():
    if os.path.exists(MESSAGE_IN):
        with open(MESSAGE_IN, "r", encoding="utf-8") as f:
            solicitud = f.read()
        print(f"[Diseñador] Solicitud recibida: {solicitud}")
        respuesta = (
            "Diseño en Figma creado para la pantalla de inicio de sesión con roles usuario y comercio, "
            "autenticación con Supabase y Google. Enlace de Figma: https://figma.com/proyecto-ejemplo"
        )
        with open(MESSAGE_OUT, "w", encoding="utf-8") as f:
            f.write(respuesta)
        print(
            f"[Diseñador] Respuesta enviada al desarrollador y guardada en {MESSAGE_OUT}")
    else:
        print(
            f"[Diseñador] No se encontró la solicitud en {MESSAGE_IN}. Ejecuta primero el agente Product Manager.")


if __name__ == "__main__":
    main()
