import requests
from urllib.parse import quote
from bs4 import BeautifulSoup
import random

# 🔍 Função para buscar no DuckDuckGo
def buscar_web(pergunta):
    url = f"https://html.duckduckgo.com/html/?q={quote(pergunta)}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.text, "html.parser")
    
    resultados = []
    for item in soup.find_all("a", class_="result__a")[:3]:
        resultados.append({
            "titulo": item.get_text(),
            "link": item["href"]
        })
    return resultados

# 📄 Função simples para resumir (versão básica)
def resumir_resultados(resultados, pergunta):
    if not resultados:
        return "Não encontrei nada sobre isso 😕"
    
    resposta = f"🔎 Encontrei algo sobre: {pergunta}\n\n"
    for i, res in enumerate(resultados, 1):
        resposta += f"{i}. {res['titulo']}\n   🔗 {res['link']}\n\n"
    resposta += "💡 Você pode clicar nos links para ler mais!"
    return resposta

# 🤖 Loop principal
print("🧠 IA com Busca Web — Digite 'sair' para encerrar")
while True:
    pergunta = input("\nVocê: ")
    if pergunta.lower() in ["sair", "tchau", "adeus"]:
        print("🧠 Até mais! 👋")
        break
    
    print("🔍 Buscando...")
    resultados = buscar_web(pergunta)
    print(resumir_resultados(resultados, pergunta))
