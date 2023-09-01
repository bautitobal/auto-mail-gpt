import openai
from my_tokens import OPENAI_API_KEY
openai.api_key = OPENAI_API_KEY

def obtener_respuesta_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
