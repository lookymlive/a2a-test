import sys

MESSAGE_FILE = "message_to_designer.txt"


def main():
    message = (
        "Por favor desarrolla un diseño en Figma para una pantalla de inicio de sesión "
        "de una app móvil con dos roles: usuario y comercio. La autenticación debe ser con Supabase y Google."
    )
    with open(MESSAGE_FILE, "w", encoding="utf-8") as f:
        f.write(message)
    print(f"[Product Manager] Solicitud enviada al diseñador: {message}")
    print(f"[Product Manager] Mensaje guardado en {MESSAGE_FILE}")


if __name__ == "__main__":
    main()
