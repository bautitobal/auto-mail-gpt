from email_reader import leer_correos, obtener_contenido
from context_interpreter import obtener_respuesta_gpt
from email_sender import enviar_correo

def main():
    correos = leer_correos()

    for correo in correos:
        asunto, cuerpo = obtener_contenido(correo)
        prompt = f"Asunto: {asunto}\nMensaje: {cuerpo}\nRespuesta:"
        
        respuesta_gpt = obtener_respuesta_gpt(prompt)
        enviar_correo(correo["destinatario"], "Re: " + asunto, respuesta_gpt)

if __name__ == "__main__":
    main()
