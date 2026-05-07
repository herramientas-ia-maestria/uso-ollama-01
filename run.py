"""
"""

import requests

def uso_api_ollama(frase):
    prompt = f"""
Clasifica la siguiente frase en una sola categoría.

Categorías permitidas:
deportes, crónica roja, política, economía, salud, educación, tecnología.
Cuando no tengas claro que categoría, usar: sin categoria
Responde únicamente con el nombre de la categoría.

Frase:
"{frase}"
"""

    respuesta = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        }
    )

    return respuesta.json()["response"].strip().lower()


def clasificar():
    archivo = open("data/noticias_cortas_500.csv", "r")
    lineas = archivo.readlines()
    lineas = [s.replace("\n", "") for s in lineas]
    lineas = [s.split("|") for s in lineas]
    lineas = lineas[0:]
    for l in lineas:
        print(l[1])
        print(l[3])
        print(uso_api_ollama(l[2]))
        print("--------------------")

if __name__ == "__main__":
    clasificar()
