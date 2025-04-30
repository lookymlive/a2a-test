import os
import sys

MESSAGE_IN = "message_to_developer.txt"
MESSAGE_OUT = "message_to_pm.txt"


def main():
    if os.path.exists(MESSAGE_IN):
        with open(MESSAGE_IN, "r", encoding="utf-8") as f:
            respuesta = f.read()
        print(f"[Desarrollador] Recibe el diseño y detalles: {respuesta}")
        confirmacion = (
            "Implementación planificada. Se usará Supabase y Google para la autenticación de usuario y comercio. "
            "Aviso al Product Manager y al Diseñador que el desarrollo comenzará."
        )
        with open(MESSAGE_OUT, "w", encoding="utf-8") as f:
            f.write(confirmacion)
        print(
            f"[Desarrollador] Confirmación enviada y guardada en {MESSAGE_OUT}")
    else:
        print(
            f"[Desarrollador] No se encontró el mensaje del diseñador en {MESSAGE_IN}. Ejecuta primero el agente diseñador.")


if __name__ == "__main__":
    main()
