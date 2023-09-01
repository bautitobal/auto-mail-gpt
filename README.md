# Auto Mail GPT

auto-mail-gpt es un programa en Python que automatiza la respuesta de correos electrónicos utilizando la tecnología GPT para generar respuestas coherentes y contextuales.

## Funcionalidades

- Lee correos electrónicos entrantes y extrae el contenido relevante.
- Interactúa con la API de OpenAI para generar respuestas utilizando GPT-3.
- Envía respuestas generadas por correo electrónico a los remitentes originales.

## Configuración

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias requeridas ejecutando `pip install -r requirements.txt`.
3. Configura tus credenciales en el archivo `tokens.py` siguiendo el formato proporcionado en el ejemplo.

## Uso

1. Ejecuta el archivo `main.py` para iniciar el proceso de lectura y respuesta de correos.
2. El programa procesará los correos electrónicos entrantes, generará respuestas utilizando GPT y las enviará automáticamente.

## Credenciales

Asegúrate de completar correctamente las variables en el archivo `tokens.py`:

- `OPENAI_API_KEY`: Tu clave de API de OpenAI.
- `EMAIL_ADDRESS`: Tu dirección de correo electrónico.
- `EMAIL_PASSWORD`: Tu contraseña de acceso de la cuenta de correo.
- `SMTP_SERVER`: Dirección del servidor SMTP.
- `IMAP_SERVER`: Dirección del servidor IMAP.

## Advertencia de Seguridad

Este programa trata con información sensible. Mantén el archivo `tokens.py` seguro y no lo compartas en lugares públicos.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el programa, corrige errores o agregar nuevas características, no dudes en abrir un pull request.

## Licencia

Este proyecto está bajo la [Licencia MIT](LICENSE).

---

Cualquier contribución o mejora en la documentación es apreciada! ¡Diviértete automatizando tus respuestas de correo electrónico con Auto-Mail-GPT.
